// Mirror the repository tree into the Imago Confluence space.
//
// Every tracked file (outside config.excludePrefixes, e.g. run directories) gets one page that embeds the file live through Git for Confluence;
// every directory gets one page with a live folder listing. Existing pages are never edited
// or deleted: this script only adds what is missing and reports what no longer exists.
// Exception, opt-in only: --prune-excluded moves pages whose path is under config.excludePrefixes to the
// Confluence trash (recoverable there; never purged). Nothing else is ever deleted.
//
// Environment: CONFLUENCE_EMAIL, CONFLUENCE_API_TOKEN (Atlassian API token for that user).
// Usage: node mirror.mjs [--dry-run] [--prune-excluded]
import { execSync } from 'node:child_process';
import { readFileSync, appendFileSync } from 'node:fs';
import { randomUUID } from 'node:crypto';

const cfg = JSON.parse(readFileSync(new URL('./config.json', import.meta.url), 'utf8'));
const dryRun = process.argv.includes('--dry-run');
const pruneExcluded = process.argv.includes('--prune-excluded');
const { CONFLUENCE_EMAIL, CONFLUENCE_API_TOKEN } = process.env;
if (!CONFLUENCE_EMAIL || !CONFLUENCE_API_TOKEN) { console.error('CONFLUENCE_EMAIL and CONFLUENCE_API_TOKEN are required'); process.exit(2); }
const auth = 'Basic ' + Buffer.from(`${CONFLUENCE_EMAIL}:${CONFLUENCE_API_TOKEN}`).toString('base64');
const EXT_FILE = cfg.appExtensionPrefix + 'gfcGitFile', EXT_FOLDER = cfg.appExtensionPrefix + 'gfcGitFolder';
const blobPrefix = `${cfg.repoUrl}/blob/${cfg.branch}/`, treePrefix = `${cfg.repoUrl}/tree/${cfg.branch}/`;
const summary = [];
const note = (s) => { console.log(s); summary.push(s); };

// ---------- Confluence API ----------
async function api(method, path, body) {
  const res = await fetch(`${cfg.baseUrl}${path}`, { method, headers: { Authorization: auth, Accept: 'application/json', 'Content-Type': 'application/json' }, body: body ? JSON.stringify(body) : undefined });
  const text = await res.text();
  if (!res.ok) throw new Error(`${method} ${path} -> ${res.status} ${text.slice(0, 300)}`);
  return text ? JSON.parse(text) : {};
}
async function listSpacePages() {
  const pages = [];
  let path = `/api/v2/spaces/${cfg.spaceId}/pages?limit=250&body-format=atlas_doc_format`;
  while (path) {
    const j = await api('GET', path);
    for (const p of j.results) {
      let macroUrls = [];
      try { macroUrls = JSON.parse(p.body.atlas_doc_format.value).content.filter(n => n.type === 'extension').map(n => n.attrs?.parameters?.guestParams?.url).filter(Boolean); } catch {}
      pages.push({ id: p.id, title: p.title, parentId: p.parentId, macroUrls });
    }
    path = j._links?.next ? j._links.next.replace(/^\/wiki/, '') : null;
  }
  return pages;
}

// ---------- ADF builders (identical to the pages created by hand) ----------
const text = (t, marks) => (marks ? { type: 'text', text: t, marks } : { type: 'text', text: t });
const code = (t) => text(t, [{ type: 'code' }]);
const para = (...c) => ({ type: 'paragraph', content: c });
const macro = (key, title, url, displayOptions) => ({ type: 'extension', attrs: { extensionType: 'com.atlassian.ecosystem', extensionKey: key, layout: 'default', parameters: { layout: 'extension', guestParams: { forceUpdate: randomUUID(), url, displayOptions }, forgeEnvironment: 'PRODUCTION', extensionId: `ari:cloud:ecosystem::extension/${key}`, extensionTitle: title } } });
const renderFormat = (p) => (p.endsWith('.md') ? 'markdown' : p.endsWith('.mermaid') ? 'mermaid' : 'source-code');
const fileDoc = (path) => ({ version: 1, type: 'doc', content: [
  para(text('Rendered live from '), text(path, [{ type: 'link', attrs: { href: blobPrefix + path } }]), text(' on '), code(cfg.branch), text('; cite as commit '), code(cfg.citeCommit), text('.')),
  macro(EXT_FILE, 'Share Git file', blobPrefix + path, `{:hh false, :e "content", :rf "${renderFormat(path)}"}`) ] });
const dirDoc = (path) => ({ version: 1, type: 'doc', content: [
  para(text('Folder '), code(path), text(' of the Imago corpus, listed live from '), code(cfg.branch), text('. Each file in it has its own child page; the listing below downloads the originals. Cite as commit '), code(cfg.citeCommit), text('.')),
  macro(EXT_FOLDER, 'Share Git folder', treePrefix + path, '{:hh false, :e "folder-downloadable", :rf nil}') ] });
const topDoc = (path) => ({ version: 1, type: 'doc', content: [
  para(text('Top-level folder '), code(path), text(' of the Imago corpus, added after the initial mirror. Contents are listed live from '), code(cfg.branch), text('; each file has its own child page. Cite as commit '), code(cfg.citeCommit), text('.')),
  macro(EXT_FOLDER, 'Share Git folder', treePrefix + path, '{:hh false, :e "folder-downloadable", :rf nil}') ] });

// ---------- Repository tree ----------
const excluded = (p) => (cfg.excludePrefixes ?? []).some(x => p.startsWith(x) || (p + '/').startsWith(x));
const files = execSync('git ls-files', { encoding: 'utf8' }).split('\n').filter(Boolean).filter(f => !f.startsWith('.github/') && !excluded(f));
const topOf = (p) => (p.includes('/') ? p.split('/')[0] : '.');
const dirs = new Set();
for (const f of files) { const parts = f.split('/'); for (let i = 2; i < parts.length; i++) dirs.add(parts.slice(0, i).join('/')); }
const tops = new Set(files.map(topOf));

// ---------- Compare ----------
const pages = (await listSpacePages()).filter(p => !cfg.ignorePageIds.includes(p.id));
const filePage = new Map(), dirPage = new Map();
for (const p of pages) for (const u of p.macroUrls) {
  if (u.startsWith(blobPrefix)) filePage.set(u.slice(blobPrefix.length), p);
  else if (u.startsWith(treePrefix)) { const d = u.slice(treePrefix.length); if (!dirPage.has(d) || p.parentId !== cfg.homePageId) dirPage.set(d, p); }
}
const topPage = { ...cfg.topFolderPages };
const titles = new Set(pages.map(p => p.title));
const relParts = (p) => (p.includes('/') ? p.split('/').slice(1) : [p]);
function uniqueTitle(path) {
  const parts = relParts(path);
  for (let k = 1; k <= parts.length; k++) { const t = parts.slice(-k).join(' / '); if (!titles.has(t)) { titles.add(t); return t; } }
  const t = `${topOf(path)} / ${parts.join(' / ')}`; titles.add(t); return t;
}
async function createPage(title, parentId, doc) {
  if (dryRun) return `dry-run-${Math.random().toString(36).slice(2, 8)}`;
  const j = await api('POST', '/api/v2/pages', { spaceId: cfg.spaceId, status: 'current', title, parentId, body: { representation: 'atlas_doc_format', value: JSON.stringify(doc) } });
  return j.id;
}

let created = 0;
// New top-level folders (rare): a page under the space home.
for (const t of [...tops].sort()) {
  if (t === '.' || topPage[t]) continue;
  const title = uniqueTitle(t.replace(/^(\d+)_/, '$1 — ').replace(/-/g, ' '));
  topPage[t] = await createPage(title, cfg.homePageId, topDoc(t));
  created++; note(`created top-level folder page "${title}" (${topPage[t]}) for ${t}`);
}
// Directories, shallowest first, so parents exist before children.
const parentIdFor = (path) => { const parent = path.includes('/') ? path.split('/').slice(0, -1).join('/') : '.'; return parent.includes('/') ? dirPage.get(parent)?.id : topPage[parent]; };
for (const d of [...dirs].sort((a, b) => a.split('/').length - b.split('/').length || a.localeCompare(b))) {
  if (dirPage.has(d)) continue;
  const parentId = parentIdFor(d); if (!parentId) { note(`SKIPPED directory ${d}: parent page missing`); continue; }
  const title = uniqueTitle(d); const id = await createPage(title, parentId, dirDoc(d));
  dirPage.set(d, { id, title }); created++; note(`created folder page "${title}" (${id}) for ${d}`);
}
// Files.
for (const f of files) {
  if (filePage.has(f)) continue;
  const parentId = parentIdFor(f); if (!parentId) { note(`SKIPPED file ${f}: parent page missing`); continue; }
  const title = uniqueTitle(f); const id = await createPage(title, parentId, fileDoc(f));
  filePage.set(f, { id, title }); created++; note(`created file page "${title}" (${id}) for ${f}`);
}
// Files or folders that vanished from the repository: report, never delete.
const gone = [...filePage.keys()].filter(f => !files.includes(f) && !excluded(f)).map(f => `file ${f} -> page ${filePage.get(f).id}`)
  .concat([...dirPage.keys()].filter(d => !dirs.has(d) && !tops.has(d) && !excluded(d)).map(d => `folder ${d} -> page ${dirPage.get(d).id}`));
for (const g of gone) note(`NO LONGER IN REPOSITORY (page left in place): ${g}`);

// Opt-in prune of pages under excluded prefixes: files first, then folders deepest-first, to the trash (no purge).
let pruned = 0;
if (pruneExcluded) {
  const targets = [...filePage.entries()].filter(([f]) => excluded(f)).map(([f, p]) => ({ kind: 'file', path: f, id: p.id }))
    .concat([...dirPage.entries()].filter(([d]) => excluded(d)).sort((a, b) => b[0].split('/').length - a[0].split('/').length).map(([d, p]) => ({ kind: 'folder', path: d, id: p.id })));
  for (const t of targets) {
    if (dryRun) { note(`DRY RUN: would move to trash ${t.kind} ${t.path} -> page ${t.id}`); pruned++; continue; }
    try { await api('DELETE', `/api/v2/pages/${t.id}`); pruned++; note(`moved to trash ${t.kind} ${t.path} -> page ${t.id}`); }
    catch (e) { note(`FAILED to trash ${t.kind} ${t.path} -> page ${t.id}: ${e.message}`); }
  }
}

note(`${dryRun ? 'DRY RUN: would create' : 'Created'} ${created} page(s)${pruneExcluded ? `; ${dryRun ? 'would trash' : 'trashed'} ${pruned} excluded page(s)` : ''}; ${files.length} tracked files, ${dirs.size} sub-folders, ${pages.length} pages in space${gone.length ? `; ${gone.length} page(s) point at removed paths` : ''}.`);
if (process.env.GITHUB_STEP_SUMMARY) appendFileSync(process.env.GITHUB_STEP_SUMMARY, `## Confluence mirror\n\n${summary.map(s => `- ${s}`).join('\n')}\n`);

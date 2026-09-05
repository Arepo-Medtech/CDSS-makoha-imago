// Headless mermaid.parse over .mermaid sources and blocks inlined in an .html (same method as 00_MANIFEST §5 DEF-001)
import { JSDOM } from "jsdom"; import fs from "fs"; import path from "path";
const dom = new JSDOM("<!DOCTYPE html><body></body>", { pretendToBeVisual: true });
globalThis.window = dom.window; globalThis.document = dom.window.document; globalThis.DOMPurify = { sanitize: s => s, addHook(){}, removeHook(){} };
const mermaid = (await import("mermaid")).default;
mermaid.initialize({ startOnLoad: false, securityLevel: "loose" });
const root = process.argv[2]; const results = [];
for (const f of fs.readdirSync(root).filter(x => x.endsWith(".mermaid"))) {
  const src = fs.readFileSync(path.join(root, f), "utf8");
  try { await mermaid.parse(src); results.push({file:f, kind:"source", result:"PASS"}); } catch (e) { results.push({file:f, kind:"source", result:"FAIL", error:String(e.message||e).slice(0,300)}); }
}
for (const f of fs.readdirSync(root).filter(x => x.endsWith(".html"))) {
  const html = fs.readFileSync(path.join(root, f), "utf8");
  const blocks = [...html.matchAll(/<pre class="mermaid"[^>]*>([\s\S]*?)<\/pre>/g)].map(m => m[1].replace(/&lt;/g,"<").replace(/&gt;/g,">").replace(/&amp;/g,"&").replace(/&quot;/g,'"'));
  let i = 0; for (const b of blocks) { i++; try { await mermaid.parse(b); results.push({file:f, kind:`inlined block ${i}`, result:"PASS"}); } catch (e) { results.push({file:f, kind:`inlined block ${i}`, result:"FAIL", error:String(e.message||e).slice(0,300)}); } }
  if (!blocks.length) results.push({file:f, kind:"inlined blocks", result:"NONE FOUND (selector <pre class=\"mermaid\">)"});
}
console.log(JSON.stringify({ tool: "mermaid " + JSON.parse(fs.readFileSync("node_modules/mermaid/package.json")).version + " via jsdom " + JSON.parse(fs.readFileSync("node_modules/jsdom/package.json")).version + " (node " + process.version + ")", results }, null, 1));

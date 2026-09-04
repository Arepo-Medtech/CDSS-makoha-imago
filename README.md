# Mākoha Imago — design corpus (v1.2)

Imago is the complete design record for **Mākoha**, Arepo Medtech's clinical decision support
system for registered health professionals. It holds the architecture, the research corpus, the
hardening directive, the register and contract schemas, the deployment and operations plans, the
regulatory posture for four jurisdictions, and the prompts that produced them. It is a set of
documents, not software: nothing in this repository runs, and nothing in it claims that anything
has been deployed.

The repository is the **source of truth** for design and posture. Other systems cite it; none of
them copy it.

## Where to read it

| Need | Go to |
|---|---|
| Read the documents, rendered, with the folder tree | [Imago space in Confluence](https://arepo-tech.atlassian.net/wiki/spaces/IMAGO/overview) — every folder and file here is a page there, rendered live from `main` |
| Cite a document | This repository, by document ID and commit (see *How to cite*) |
| Programme narrative and decisions | [Makoha space in Confluence](https://arepo-tech.atlassian.net/wiki/spaces/MAK) |
| Work items | Jira project **MAK** |
| The software being built from this design | [Arepo-Medtech/CDSS_Makoha](https://github.com/Arepo-Medtech/CDSS_Makoha) |

## Layout

| Folder | Contents | Standing |
|---|---|---|
| `00_MANIFEST.md` | Artifact manifest for the whole repository: inventory, availability report, production sequence, completeness audit, defect log, amendments A-001 to A-003. **Start here.** | Index; defers to the corpus MANIFEST in `03_` |
| `01_north-star-and-transformation` | MET-1 Metamorphosis Plan (North Star in §2) and MET-1.1 delta; MET-2 conflict and decision register with MET-2.1 delta; MET-3 traceability map; MET-4 gap analysis and roadmap | Proposed planning layer; edits no source |
| `02_cdss-stack-augmented` | The 21 original CDSS documents, each byte-exact with an additive annex: Primer 0, Architecture and Integration, Primers A to L, coder variants, harness, ecosystem report, complete stack, diagrams | Normative for the engine architecture |
| `03_makoha-butterfly-corpus` | The fifteen Mākoha research volumes (`corpus-md`), the corpus MANIFEST with its precedence law, the face primers (`butterfly-primers`), and sixteen published pages (`artifacts-html`) | Verbatim; zero edits permitted |
| `04_hardening` | Anti-Laziness Hardening Directive (MT2), HARDEN-2 class bars, HARDEN-3 wave worklist, HARDEN-1 coverage ledger seed | Standing order; the pass has **not** been run |
| `05_registers-and-contracts` | R29 and R30 register schemas and seeds, CONTRACT-ARG-1 argument contract | Proposed; ratification is DEC-02 |
| `06_repositories` | REPO-MAP v2 and skeletons for every planned repository (`repo-skeletons`) | Proposed; owners are DEC-09 |
| `07_deployment-and-operations` | DEPLOY-1 sequencing, DEPLOY-2 acceptance, OPS-1, GOV-1, SEC-1 | Retained and Proposed |
| `08_research` | RESEARCH-1 sources, verification and gaps RG-01 to RG-06 | Informative |
| `09_diagrams` | Four Mermaid sources and the rendered HTML successor page | Illustrative |
| `10_regulatory-execution` | REG-POSTURE (Australia), REG-NZ, REG-US, REG-EU, MAK-GOV Addendum G, REG-SPRINT plans, EXEC-1 directive, FOLD-1 worklist, validator script | **ADVISORY_ONLY** until counsel attests; sequencing per EXEC-1 |
| `11_prompts` | Launch prompts per component and volume, and the survey-2 run record with its tools | Working material, not programme facts |

288 tracked files at the v1.2 baseline. The manifest's own file count describes the v1.1 build and
is extended by its amendments; the tracked tree is authoritative for what exists.

## Laws of the corpus

- **Append-only.** Nothing pre-existing is edited. A change arrives as a delta (`MET-1.1`,
  `REG-SPRINT-1.1`) or as a new version beside the old (`REG-POSTURE_v1.1` and `_v1.2`).
- **Precedence.** The corpus MANIFEST in `03_` governs the fifteen volumes; MAK-FFC v1.1 is host
  law for the corpus; REG-POSTURE governs regulatory content; Architecture §12.1 register laws and
  the doctrine ("ML proposes and tests; only arithmetic releases") are non-negotiable; EXEC-1
  governs sequencing.
- **Stable IDs.** Requirements, decisions, conflicts, gaps and findings carry IDs (`SPINE-3`,
  `DEC-07`, `C-11`, `G-08`, `REG-FIND-001`). Sections move between versions; IDs do not.
- **Honesty lines.** The hardening pass has not been executed. Regulatory content is advisory
  until counsel attests. Person-level owners and RTO/RPO remain to be defined. The manifest §4.4
  keeps the full list.

## How to cite

Cite by **document ID and commit**, never by page or section alone:

```
MET-2 · DEC-04 · 73460b3
```

`73460b3` is the v1.2 baseline commit that sealed the corpus. Later commits add tooling and
this file; they change no corpus content. To point at a later state, name the later commit.

## How to change it

1. Branch from `main`, add your delta or new version as a **new file**. Do not edit an existing one.
2. Open a pull request. `main` accepts changes only through pull requests.
3. Record the amendment in `00_MANIFEST.md` §7 onward, as A-001 to A-003 do.

On merge, the **Confluence mirror** action (`.github/workflows/confluence-mirror.yml`) creates an
Imago space page for every new file or folder. Existing pages already render the current file on
every view, so edits to content need no action at all. Removed paths are reported in the job
summary and left for a human to resolve.

## Provenance

Built 1 to 2 September 2026 from the CDSS document set, the Mākoha research corpus, the MT2
directive and the metamorphosis plan; placed under version control as v1.2 on 3 September 2026;
made public and mirrored to Confluence on 4 September 2026. Owner: Ken Lee, Arepo Medtech.

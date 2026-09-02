<!-- SKELETON — Proposed (DEC-09; Arch §10 mirrored). No code, build, or deployment is claimed. Every directory README states what its owning primer/annex requires; content lands only through that repo's own gauntlet. -->
# cdss-registry (Existing — Primer D; annex D10)
Signed fragment bundles + OPA gate policy; **signing keys never leave**. Passing fragments render verbatim inside the argument claim; SPINE-3 never alters fragment text. GPP interaction: `profile: GPP` stamps (GPP-11) are the only content the J-3 artifact serves.
Layout: `fragments/` (statement-level, signed, versioned; dose-bounds block per D8) · `policy/` (OPA five-gate policy) · `gateway/` (PR templates; pharmacist+clinician CODEOWNERS) · `signing/` (custody notes — keys in KMS/cosign, never in repo).

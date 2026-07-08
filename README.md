# Research Data Automation Tools

Public umbrella hub for small research software tools that turn chemistry and biophysics data workflows into inspectable, browser-local, or dependency-light calculations.

This hub is the public target for the resume entry `Research Data Automation Tools`. It links the already-public component repositories and keeps the recruiter-readable summary, component table, public-safety boundary, and resume anchors in one place.

## Recruiter-readable summary

I built a set of lightweight research automation tools that reduce repetitive chemistry data-processing work: titration planning, NMR T1 fitting, DOSY diffusion averaging, radial-distribution-function teaching simulations, and a public-safe AI-assisted literature/demo scout for aqueous photodimerization. The common theme is translating scientific inputs into transparent calculations, visual checks, and reproducible outputs that a researcher can inspect before making experimental decisions.

## Component tools

| Tool | Public URL | Public status | What it demonstrates | Notes for reviewers |
| --- | --- | --- | --- | --- |
| Photodimerization-in-Water Scout | https://github.com/ytheesh96/hhmi-photodimerization-scout | Public; no license detected during prep | Dependency-free Python scout loop that ranks public/demo candidate rows, preserves caveats, and emits explanation cards plus a visual summary | Public-safe proof artifact only; not a validated predictive model |
| Titration Calculator | https://github.com/ytheesh96/Titration-calculator | Public; MIT license | Browser app for titration planning, mass/stock-solution calculations, and concentration-change visualization | Emphasizes practical experiment setup and sanity checks |
| T1 Calculator | https://github.com/ytheesh96/T1-Calculator | Public; MIT license | NMR T1 relaxation fitting from CSV integrals with T1, M0, R2, interactive labels, and visualization | Shows scientific curve fitting workflow packaging |
| DOSY Calculator | https://github.com/ytheesh96/DOSY-Calculator | Public; MIT license | Browser-local DOSY diffusion analysis with species assignment, weighted-average diffusion constants, and propagated errors | Local processing keeps uploaded data in the browser |
| MD Simulator | https://github.com/ytheesh96/MD_Simulator | Public; MIT license | Interactive radial distribution function `g(r)` visualization for aggregated vs dispersed regimes | Teaching/demo tool for interpreting local structure |

## Link targets and anchors

Use these stable anchors for resume links or reviewer navigation:

- Hub root: `https://github.com/ytheesh96/research-data-automation-tools`
- Recruiter summary: `https://github.com/ytheesh96/research-data-automation-tools#recruiter-readable-summary`
- Component table: `https://github.com/ytheesh96/research-data-automation-tools#component-tools`
- Public-safety boundary: `https://github.com/ytheesh96/research-data-automation-tools#public-safety-boundary`
- Publishing gate: `https://github.com/ytheesh96/research-data-automation-tools#publish-checklist-approval-gate`

Preferred resume href: `https://github.com/ytheesh96/research-data-automation-tools`

## Recommended GitHub repository description

Public hub for research data automation tools: chemistry calculators, NMR/DOSY analysis, MD/RDF demos, and an AI-assisted photodimerization scout.

## Public-safety boundary

This hub should only describe and link to already-public repositories. It must not include unpublished research data, non-public lab notes, raw spectra, credentials, internal audit tables, local filesystem paths, or non-public employer/institutional details. The photodimerization scout should continue to state that it is a public-safe demo layer, not a validated predictive model.

## License recommendation for `hhmi-photodimerization-scout`

The four calculator/demo repositories already advertise MIT licensing. For consistency, add an MIT `LICENSE` file to `hhmi-photodimerization-scout` before making it a central component of this umbrella, assuming Vaitheesh has confirmed there are no institutional, employer, collaborator, publication, or third-party data restrictions. Keep its `NOTICE.md` and README public-data boundary. If the repo contains or links to publication-derived rows, the MIT license should cover only this repository's code, docs, and demo outputs; it should not imply relicensing of external source material.

## Publish checklist / approval gate

Publication gate used for the initial public release:

- [x] Vaitheesh approved the hub name `research-data-automation-tools` and public index target.
- [x] Create the remote repository or page only after explicit approval.
- [x] Add this README as the hub landing page.
- [x] Add `docs/index.md` for optional GitHub Pages use.
- [x] Add `PUBLIC_SAFETY_NOTES.md`, `PUBLISH_CHECKLIST.md`, and `RESUME_LINK_HANDOFF.md`.
- [x] Leave the umbrella repo without an added license unless separately approved.
- [x] Do not add a license to `hhmi-photodimerization-scout` without separate public/IP approval.
- [x] Re-run URL checks for all component repositories.
- [x] Re-run local public-safety scan for non-public notes, secrets, and local paths.
- [x] Use the resume hyperlink `https://github.com/ytheesh96/research-data-automation-tools` after the public page renders correctly.

## Verification performed during package prep

- Confirmed all five component GitHub URLs return HTTP 200.
- Queried public GitHub metadata: all five repositories are public; four calculator/demo repositories report MIT license metadata; `hhmi-photodimerization-scout` reports no GitHub license metadata.
- Cloned public repositories read-only for README/license inspection; no remote writes, visibility changes, pushes, or metadata edits were performed.
- Ran local package validation script to check required package files, component URLs, and forbidden private/local-path patterns.

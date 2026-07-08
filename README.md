# Research Data Automation Tools

A public index of small chemistry and biophysics software tools for experiment planning, data analysis, and teaching simulations.

## Research tools page

The GitHub Pages index for the collection is here:

<https://ytheesh96.github.io/research-data-automation-tools/>

Use the page as the browser-facing landing point. This repository keeps the index lightweight while each tool remains inspectable in its own public repository.

## What this collection is

These tools package repetitive research workflows into transparent, browser-local, or dependency-light software. The through-line is practical research productivity: scientific inputs go in, calculations and visual checks stay visible, and outputs remain easy to inspect before making experimental decisions.

Current areas covered:

- titration planning and stock-solution calculations
- NMR T1 relaxation fitting
- DOSY diffusion averaging and species assignment
- radial-distribution-function teaching simulations
- photodimerization experiment planning / public-safe triage

## Tools index

| Area | Tool | Source | What it helps with |
| --- | --- | --- | --- |
| Photochemistry planning | [Photodimerization Scout](https://github.com/ytheesh96/hhmi-photodimerization-scout) | `hhmi-photodimerization-scout` | Plans the next irradiation experiment from substrate character, medium, organizing media, and observed result |
| Chemistry planning | [Titration Calculator](https://github.com/ytheesh96/Titration-calculator) | `Titration-calculator` | Plans titrations, mass/stock-solution calculations, and concentration changes |
| NMR analysis | [T1 Calculator](https://github.com/ytheesh96/T1-Calculator) | `T1-Calculator` | Fits NMR T1 relaxation data from CSV integrals and visualizes fit quality |
| NMR diffusion analysis | [DOSY Calculator](https://github.com/ytheesh96/DOSY-Calculator) | `DOSY-Calculator` | Computes weighted-average diffusion constants with species assignments and propagated errors |
| Simulation / teaching | [MD Simulator](https://github.com/ytheesh96/MD_Simulator) | `MD_Simulator` | Visualizes radial distribution behavior for aggregated and dispersed regimes |

## Repository structure

```text
README.md      # repository overview
docs/index.md  # GitHub Pages tools index
```

## Public-data boundary

This repository is an index and portfolio hub. It does not contain private research data, unpublished spectra, raw lab notebooks, or hidden model outputs. Individual tools should keep their own public/private boundaries documented in their repositories.

## Maintaining the page

Update both places when adding or renaming tools:

1. `README.md` for the GitHub repository view.
2. `docs/index.md` for the GitHub Pages index.

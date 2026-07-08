# Research Data Automation Tools

Small research software tools for turning chemistry and biophysics workflows into inspectable, browser-local, or dependency-light calculations.

## Project overview

This collection packages repetitive research data-processing tasks into transparent tools: titration planning, NMR T1 fitting, DOSY diffusion averaging, radial-distribution-function teaching simulations, and an AI-assisted literature/demo scout for aqueous photodimerization.

The common theme is practical research productivity: scientific inputs go in, calculations and visual checks stay visible, and outputs remain easy to inspect before making experimental decisions.

## Component tools

| Tool | Public URL | What it demonstrates |
| --- | --- | --- |
| Photodimerization-in-Water Scout | https://github.com/ytheesh96/hhmi-photodimerization-scout | Dependency-free Python scout loop that ranks candidate rows, preserves caveats, and emits explanation cards plus a visual summary |
| Titration Calculator | https://github.com/ytheesh96/Titration-calculator | Browser app for titration planning, mass/stock-solution calculations, and concentration-change visualization |
| T1 Calculator | https://github.com/ytheesh96/T1-Calculator | NMR T1 relaxation fitting from CSV integrals with T1, M0, R2, interactive labels, and visualization |
| DOSY Calculator | https://github.com/ytheesh96/DOSY-Calculator | Browser-local DOSY diffusion analysis with species assignment, weighted-average diffusion constants, and propagated errors |
| MD Simulator | https://github.com/ytheesh96/MD_Simulator | Interactive radial distribution function `g(r)` visualization for aggregated vs dispersed regimes |

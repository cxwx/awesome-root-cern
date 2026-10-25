# Awesome ROOT (CERN) [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

A curated list of awesome [ROOT](https://root.cern/) libraries, tools, bindings, editor support, learning resources and data.

🌐 Also available as a website: <https://cxwx.github.io/awesome-root-cern/>

> `⭐` stars and `🗓` last-push date are refreshed automatically every week. 💤 = no activity for over a year; 🗄️ = repository archived.

[ROOT](https://root.cern/) is CERN's modular C++ toolkit for data processing, statistical analysis, visualisation and storage, born in 1995 and used across particle and nuclear physics. This list is about the ecosystem around it — language bindings, pure re-implementations of the file format, viewers, editors, training material and open data — mainly hosted on GitHub.

**Any pull request is welcome!**

## Contents

- [Official Resources](#official-resources)
- [Install & Containers](#install--containers)
- [Python Ecosystem](#python-ecosystem)
  - [I/O & Columnar Analysis](#io--columnar-analysis)
  - [Fitting & Statistics](#fitting--statistics)
- [Other Languages](#other-languages)
- [Viewers & Visualization](#viewers--visualization)
- [Editor & IDE Support](#editor--ide-support)
- [Notebooks & REPLs](#notebooks--repls)
- [Learning & Training](#learning--training)
- [Benchmarks & Core Libraries](#benchmarks--core-libraries)
- [Data](#data)
- [Outdated](#outdated)
- [Contribute](#contribute)

## Official Resources

- [root.cern](https://root.cern/) — Official website: downloads, manuals, release notes.
- [root-project/root](https://github.com/root-project/root) — Official source code; development happens on [GitLab](https://gitlab.cern.ch/root-project/root), this mirror publishes the releases. `⭐ 3326 · 🗓 2026-10`
- [ROOT Reference Guide](https://root.cern/doc/master/) — Complete class and function reference.
- [ROOT Manual](https://root.cern/manual/) — Official user guide, how-tos and concept chapters.
- [ROOT Forum](https://root-forum.cern.ch/) — Community Q&A, answered by the ROOT team.
- [root-project/open_projects](https://github.com/root-project/open_projects) — Browsable list of open projects to contribute to (GSoC & friends). `⭐ 1 · 🗓 2026-02`
- [root-project/web](https://github.com/root-project/web) — Source of the root.cern website. `⭐ 53 · 🗓 2026-10`

## Install & Containers

- [Homebrew](https://formulae.brew.sh/formula/root) — `brew install root` on macOS and Linux.
- [conda-forge/root-feedstock](https://github.com/conda-forge/root-feedstock) — ROOT on conda-forge: `conda install -c conda-forge root`. `⭐ 30 · 🗓 2026-09`
- [rootproject/root](https://hub.docker.com/r/rootproject/root) — Official prebuilt Docker images for every supported platform.
- [root-project/root-docker](https://github.com/root-project/root-docker) — Docker recipes used to build the official ROOT images. `⭐ 36 · 🗓 2026-08`

## Python Ecosystem

### I/O & Columnar Analysis

- [columnflow/columnflow](https://github.com/columnflow/columnflow) — Vertical analysis framework built on columnar tools (coffea). `⭐ 35 · 🗓 2026-10`
- [dask-contrib/dask-histogram](https://github.com/dask-contrib/dask-histogram) — Dask integration for boost-histogram, scaling histogramming out of uproot-fed workflows. `⭐ 25 · 🗓 2026-10`
- [iris-hep/func_adl](https://github.com/iris-hep/func_adl) — Functional Analysis Description Language: query TTrees (or xAOD) with composable functional expressions. `⭐ 10 · 🗓 2026-08`
- [scikit-hep/awkward](https://github.com/scikit-hep/awkward) — Manipulate arrays of jagged, nested data as easily as NumPy; the standard companion to uproot. `⭐ 988 · 🗓 2026-10`
- [scikit-hep/coffea](https://github.com/scikit-hep/coffea) — Columnar Object Framework For Effective Analysis, built on uproot + awkward + dask. `⭐ 146 · 🗓 2026-10`
- [scikit-hep/uproot5](https://github.com/scikit-hep/uproot5) — ROOT I/O in pure Python and NumPy: read and write TTrees and RNTuples without installing ROOT. `⭐ 273 · 🗓 2026-10`
- [ssl-hep/ServiceX](https://github.com/ssl-hep/ServiceX) — Service that delivers columnar data (uproot/xaod) from ROOT files as Arrow/Parquet streams. `⭐ 21 · 🗓 2026-10`

### Fitting & Statistics

- [GooFit/GooFit](https://github.com/GooFit/GooFit) — Massively-parallel likelihood fitting for GPU and multi-core, RooFit-style API (CUDA/OpenMP). `⭐ 145 · 🗓 2026-10`
- [scikit-hep/cabinetry](https://github.com/scikit-hep/cabinetry) — Build likelihoods from uproot/ROOT workspaces and run statistical inference with pyhf. `⭐ 33 · 🗓 2026-03`
- [scikit-hep/hepstats](https://github.com/scikit-hep/hepstats) — HEP statistics toolkit: fits, sWeights, significances, goodness-of-fit. `⭐ 85 · 🗓 2026-10`
- [scikit-hep/pyhf](https://github.com/scikit-hep/pyhf) — Pure-Python HistFactory likelihoods; a portable alternative to RooFit workspaces. `⭐ 304 · 🗓 2026-10`
- [zfit/zfit](https://github.com/zfit/zfit) — Model-independent Python fitting library designed as a RooFit alternative. `⭐ 205 · 🗓 2026-10`
- [RooUnfold](https://gitlab.cern.ch/RooUnfold/RooUnfold) — ROOT unfolding framework: response matrices, Bayesian, SVD, IDS and more.

## Other Languages

Bindings and independent re-implementations of the ROOT file format — most work without a ROOT installation.

- [ariostas/rntuple](https://github.com/ariostas/rntuple) — RNTuple I/O library in Rust. `⭐ 2 · 🗓 2025-12`
- [cbourjau/alice-rs](https://github.com/cbourjau/alice-rs) — ROOT I/O in Rust (the `root-io` crate), built to analyse ALICE open data. `⭐ 105 · 🗓 2023-05` 💤
- [go-hep/hep](https://github.com/go-hep/hep) — go-hep.org/x/hep monorepo; `groot` reads and writes ROOT files in pure Go. `⭐ 254 · 🗓 2025-10` 🗄
- [JuliaHEP/ROOT.jl](https://github.com/JuliaHEP/ROOT.jl) — Julia wrapper around libROOT for CERN ROOT compatibility. `⭐ 52 · 🗓 2026-01`
- [JuliaHEP/UnROOT.jl](https://github.com/JuliaHEP/UnROOT.jl) — Native Julia reader (and RNTuple writer) for ROOT files, no dependence on ROOT or Python. `⭐ 121 · 🗓 2026-10`
- [kloimhardt/LisRoot](https://github.com/kloimhardt/LisRoot) — Lisp (Clojure) and YAMLScript wrapper around PyROOT. `⭐ 10 · 🗓 2024-06` 💤
- [m-dupont/oxyroot](https://github.com/m-dupont/oxyroot) — Reading and writing `.root` binary files in pure Rust. `⭐ 12 · 🗓 2024-10` 💤
- [odakahirokazu/RubyROOT](https://github.com/odakahirokazu/RubyROOT) — Ruby binding of ROOT. `⭐ 7 · 🗓 2026-08`
- [wavewave/HROOT](https://github.com/wavewave/HROOT) — Haskell binding to the ROOT libraries. `⭐ 11 · 🗓 2023-07` 💤

## Viewers & Visualization

- [AlbertoPdRF/root-file-viewer](https://github.com/AlbertoPdRF/root-file-viewer) — VS Code extension to view ROOT files directly in the editor, rendered with JSROOT ([marketplace](https://marketplace.visualstudio.com/items?itemName=albertopdrf.root-file-viewer)). `⭐ 55 · 🗓 2026-10`
- [root-project/jsroot](https://github.com/root-project/jsroot) — JavaScript ROOT: interactive ROOT graphics and file browsing in the browser; also powers ROOT's web display. `⭐ 215 · 🗓 2026-10`
- [scikit-hep/uproot-browser](https://github.com/scikit-hep/uproot-browser) — Terminal (TUI) viewer for ROOT files, from the uproot team. `⭐ 78 · 🗓 2026-10`
- [ROOT RBrowser for VS Code](https://marketplace.visualstudio.com/items?itemName=CharlotteKnight.root-rbrowser) — Open a native ROOT RBrowser window from inside VS Code.
- [rntviewer](https://codeberg.org/silverweed/rntviewer) — Fast terminal viewer for RNTuple files.

## Editor & IDE Support

### Emacs

- [jaypmorgan/cern-root-mode](https://github.com/jaypmorgan/cern-root-mode) — Major mode for ROOT scripts and the Cling REPL in Emacs. `⭐ 18 · 🗓 2024-11` 💤

### Neovim/Vim

- [Vigemus/iron.nvim](https://github.com/Vigemus/iron.nvim) — Interactive REPLs over Neovim; supports ROOT by default. `⭐ 1366 · 🗓 2026-10`
- [metakirby5/codi.vim](https://github.com/metakirby5/codi.vim) — The interactive scratchpad for hackers; replace Cling with `root` to make it a ROOT REPL. `⭐ 3056 · 🗓 2023-02` 💤

## Notebooks & REPLs

- [jupyter-xeus/xeus-cling](https://github.com/jupyter-xeus/xeus-cling) — Jupyter kernel for C++ built on Cling. `⭐ 3297 · 🗓 2025-10`
- [root-project/cling](https://github.com/root-project/cling) — The C++ interpreter behind ROOT's REPL, also usable standalone. `⭐ 4201 · 🗓 2026-10`
- [JupyROOT](https://root.cern/manual/python/#jupyroot) — ROOT's built-in Jupyter integration; ships with ROOT.
- [SWAN](https://swan.cern.ch/) — CERN's service for interactive analysis notebooks with ROOT preinstalled.

## Learning & Training

- [root-project/training](https://github.com/root-project/training) — ROOT training material and tutorials. `⭐ 137 · 🗓 2024-07` 💤
- [root-project/student-course](https://github.com/root-project/student-course) — ROOT course for students. `⭐ 136 · 🗓 2026-07`
- [root-project/software-carpentry](https://github.com/root-project/software-carpentry) — ROOT material for Software Carpentry workshops. `⭐ 23 · 🗓 2024-11` 🗄
- [root-project/root-cpp-course](https://github.com/root-project/root-cpp-course) — A course about using ROOT in C++. `⭐ 2 · 🗓 2026-09`
- [Official tutorials](https://root.cern/doc/master/group__Tutorials.html) — The tutorial suite shipped with ROOT, browsable and runnable.

## Benchmarks & Core Libraries

- [root-project/veccore](https://github.com/root-project/veccore) — Portable SIMD vectorization library developed for ROOT's internals. `⭐ 88 · 🗓 2026-06`
- [root-project/rootbench](https://github.com/root-project/rootbench) — ROOT benchmark suite and performance monitoring. `⭐ 23 · 🗓 2026-10`
- [root-project/analysis-grand-challenge](https://github.com/root-project/analysis-grand-challenge) — Analysis Grand Challenge workflows exercised with ROOT/RDataFrame.

## Data

- [CERN Open Data](http://opendata.cern.ch/) — Open data from LHC experiments and more, largely distributed in ROOT format.
- [HEPData](https://www.hepdata.net/) — Repository for publication-related HEP data, with ROOT export.

## Outdated

Projects targeting ROOT versions before 6.26, kept for historical interest.

- [AstroROOT](https://www.isdc.unige.ch/astroroot/index) — An extension of ROOT 5.18 for astronomical data analysis.
- Coast — Part of [CORSIKA 7](https://www.iap.kit.edu/corsika/99.php); only works on ROOT 5. CORSIKA 8 may rewrite it.
- [diana-hep/root4j](https://github.com/diana-hep/root4j) — Pure-Java ROOT file reader. `⭐ 7 · 🗓 2020-10` 💤
- [rootpy/rootpy](https://github.com/rootpy/rootpy) — Pythonic interface to the ROOT libraries on top of PyROOT. `⭐ 205 · 🗓 2019-12` 💤
- [scikit-hep/root_numpy](https://github.com/scikit-hep/root_numpy) — The interface between ROOT and NumPy; replaced by uproot. `⭐ 134 · 🗓 2023-01` 🗄
- [scikit-hep/root_pandas](https://github.com/scikit-hep/root_pandas) — Load/save ROOT files as pandas DataFrames; superseded by uproot + awkward. `⭐ 111 · 🗓 2021-03` 🗄
- [scikit-hep/uproot3](https://github.com/scikit-hep/uproot3) — The uproot 3.x series, superseded by uproot 5. `⭐ 313 · 🗓 2021-02` 🗄

## Contribute

Contributions are welcome! Please read the [contribution guidelines](CONTRIBUTING.md) first.

- To add a project: open a PR with a one-line entry in the right section, linking the repo.
- The website is served by GitHub Pages from this same README via docsify — nothing extra to update.

## License

[MIT](LICENSE)

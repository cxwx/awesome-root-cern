<!-- *********************************************************************** -->
<!--                                                                         -->
<!--                                                      :::      ::::::::  -->
<!-- README.md                                          :+:      :+:    :+:  -->
<!--                                                  +:+ +:+         +:+    -->
<!-- By: chenxu <chenxu@mail.ustc.edu.cn>           +#+  +:+       +#+       -->
<!--                                              +#+#+#+#+#+   +#+          -->
<!-- Created: 2025/01/07 06:07:19 by chenxu            #+#    #+#            -->
<!-- Updated: 2025/01/07 06:11:03 by chenxu           ###   ########.fr      -->
<!--                                                                         -->
<!-- *********************************************************************** -->
<!-- cspell:ignore cern astroroot rootpy numpy repl repls pythonic -->
<!-- LTeX: enabled=false -->

# Awesome ROOT(cern) [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

[ROOT](https://root.cern.ch/), [Forum](https://root-forum.cern.ch/), [GitHub](https://github.com/root-project/root)

This repo is an opinionated list of awesome ROOT frameworks, libraries, software and resources.

**Any pull request is welcome!**

## Contents

- [Library](#library)
- [Editor Plugins](#editor-plugins)
- [Script](#script)
- [Data](#data)
- [Outdated](#outdated)

## Library

* [RubyROOT](https://github.com/odakahirokazu/RubyROOT)
    - Ruby binding of ROOT (CERN)
* [HROOT](https://github.com/wavewave/HROOT)
    - HROOT: Haskell binding to ROOT
* [ROOT.jl](https://github.com/JuliaHEP/ROOT.jl)
    - CERN ROOT compatiblility for Julia
* [UpROOT.jl](https://github.com/JuliaHEP/UpROOT.jl)
    - Julia package to access CERN ROOT files, wraps Python package uproot
* [groot](https://pkg.go.dev/go-hep.org/x/hep/groot)
    - Experimental, pure-Go package to read and write ROOT files, without having ROOT installed.
* [ROOT4J](https://github.com/diana-hep/root4j)
    - archived
* [root-io](https://docs.rs/root-io/latest/root_io/)
    - rust IO
* [alice-rs](https://github.com/cbourjau/alice-rs)
    - rust
* [uproot5](https://github.com/scikit-hep/uproot5)
    - ROOT I/O in pure Python and NumPy.
* [uproot-browser](https://github.com/scikit-hep/uproot-browser)
    - A TUI viewer for ROOT files
* [RooUnfold](https://gitlab.cern.ch/RooUnfold/RooUnfold)
    - ROOT unfolding framewrok


## Editor Plugins

### Emacs

* [cern-root-mode](https://github.com/jaypmorgan/cern-root-mode)
    - Major-mode for ROOT and the Cling REPL in Emacs

### VSCode

* [ROOT File Viewer]
  - ROOT File Viewer

### Neovim/Vim

* [Iron.nvim](https://github.com/Vigemus/iron.nvim)
  - Interactive Repls Over Neovim
  - support ROOT by default
* [codi.nvim](https://github.com/metakirby5/codi.vim)
  - The interactive scratchpad for hackers.
  - replace cling with ROOT

## Script

## Data

## Outdated

Base on ROOT Ver < 6.26

* [AstroROOT](https://www.isdc.unige.ch/astroroot/index)
    - an extension of ROOT for astronomical data analysis.
    - ROOT Ver 5.18
* Coast
    - part of [Corsika7](https://www.iap.kit.edu/corsika/99.php)
    - Only work on ROOT5
    - Corsika8 may rewrite coast
* [Rootpy](https://github.com/rootpy/rootpy)
    - A pythonic interface for the ROOT libraries on top of the PyROOT bindings.
* [root_numpy](https://github.com/scikit-hep/root_numpy)
    - The interface between ROOT and NumPy
    - replace by uproot
* [uproot3](https://github.com/scikit-hep/uproot3)
    - ROOT I/O in pure Python and NumPy.
* [root_pandas](https://github.com/scikit-hep/root_pandas)
    - A Python module for conveniently loading/saving ROOT files as pandas DataFrames

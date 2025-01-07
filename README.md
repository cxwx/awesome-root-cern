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
    - ![GitHub last commit](https://img.shields.io/github/last-commit/odakahirokazu/RubyROOT) ![GitHub Repo stars](https://img.shields.io/github/stars/odakahirokazu/RubyROOT)
* [HROOT](https://github.com/wavewave/HROOT)
    - HROOT: Haskell binding to ROOT
    - ![GitHub last commit](https://img.shields.io/github/last-commit/wavewave/HROOT) ![GitHub Repo stars](https://img.shields.io/github/stars/wavewave/HROOT)
* [ROOT.jl](https://github.com/JuliaHEP/ROOT.jl)
    - CERN ROOT compatiblility for Julia
    - ![GitHub last commit](https://img.shields.io/github/last-commit/JuliaHEP/ROOT.jl) ![GitHub Repo stars](https://img.shields.io/github/stars/JuliaHEP/ROOT.jl)
* [UpROOT.jl](https://github.com/JuliaHEP/UpROOT.jl)
    - Julia package to access CERN ROOT files, wraps Python package uproot
    - ![GitHub last commit](https://img.shields.io/github/last-commit/JuliaHEP/UpROOT.jl) ![GitHub Repo stars](https://img.shields.io/github/stars/JuliaHEP/UpROOT.jl)
* [groot](https://pkg.go.dev/go-hep.org/x/hep/groot)
    - Experimental, pure-Go package to read and write ROOT files, without having ROOT installed.


## Editor Plugins

### Emacs

* [cern-root-mode](https://github.com/jaypmorgan/cern-root-mode)
    - Major-mode for ROOT and the Cling REPL in Emacs
    - ![GitHub last commit](https://img.shields.io/github/last-commit/jaypmorgan/cern-root-mode) ![GitHub Repo stars](https://img.shields.io/github/stars/jaypmorgan/cern-root-mode)
* [uproot5](https://github.com/scikit-hep/uproot5)
    - ROOT I/O in pure Python and NumPy.
    - ![GitHub last commit](https://img.shields.io/github/last-commit/scikit-hep/uproot5) ![GitHub Repo stars](https://img.shields.io/github/stars/scikit-hep/uproot5)
* [uproot-browser](https://github.com/scikit-hep/uproot-browser)
    - A TUI viewer for ROOT files
    - ![GitHub last commit](https://img.shields.io/github/last-commit/scikit-hep/uproot-browser) ![GitHub Repo stars](https://img.shields.io/github/stars/scikit-hep/uproot-browser)

### VSCode

* [ROOT File Viewer]
  - ROOT File Viewer

### Neovim/Vim

* [Iron.nvim](https://github.com/Vigemus/iron.nvim)
  - Interactive Repls Over Neovim
  - support ROOT by default
    - ![GitHub last commit](https://img.shields.io/github/last-commit/Vigemus/iron.nvim) ![GitHub Repo stars](https://img.shields.io/github/stars/Vigemus/iron.nvim)
* [codi.nvim](https://github.com/metakirby5/codi.vim)
  - The interactive scratchpad for hackers.
  - replace cling with ROOT
    - ![GitHub last commit](https://img.shields.io/github/last-commit/metakirby5/codi.vim) ![GitHub Repo stars](https://img.shields.io/github/stars/metakirby5/codi.vim)

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
    - ![GitHub last commit](https://img.shields.io/github/last-commit/rootpy/rootpy) ![GitHub Repo stars](https://img.shields.io/github/stars/rootpy/rootpy)
* [root_numpy](https://github.com/scikit-hep/root_numpy)
    - The interface between ROOT and NumPy
    - replace by uproot
    - ![GitHub last commit](https://img.shields.io/github/last-commit/scikit-hep/root_numpy) ![GitHub Repo stars](https://img.shields.io/github/stars/scikit-hep/root_numpy)
* [uproot3](https://github.com/scikit-hep/uproot3)
    - ROOT I/O in pure Python and NumPy.
    - ![GitHub last commit](https://img.shields.io/github/last-commit/scikit-hep/uproot3) ![GitHub Repo stars](https://img.shields.io/github/stars/scikit-hep/uproot3)
* [root_pandas](https://github.com/scikit-hep/root_pandas)
    - A Python module for conveniently loading/saving ROOT files as pandas DataFrames
    - ![GitHub last commit](https://img.shields.io/github/last-commit/scikit-hep/root_pandas) ![GitHub Repo stars](https://img.shields.io/github/stars/scikit-hep/root_pandas)



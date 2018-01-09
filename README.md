# J-PET layers controller

Transforms list-mode ASCII data from 3-layer scanner geometry (see [GOJA output](https://github.com/JPETTomography/j-pet-gate-tools/tree/master/examples/goja "GOJA output") description) into 1-layer.

The default parameters implies [big barrell](http://koza.if.uj.edu.pl/petwiki/index.php/Simulated_geometries#Laboratory_geometry_-_3_layers.2C_192_strips_.28big_barell.29 "JPET Wiki") geometry, with the options to perform TOF adjustment (since LORs, redefined to 1-layer, are of different lengths). An arbitrary layer ID which the data will be remapped to could be chosen, with the 1st one as the default.

## Prerequisites

The application is written in Python 2.7 (exact version Python 2.7.13), with the addition of the following packages:

* numpy (tested for 1.11.3)
* pandas (tested for 0.19.2)

## Usage

The generic usage is as follows:
```
$ python reduce_multilayer.py <input_file> [-o <output_file>] [-l <layer ID>] [-with_tof]
```
Here, ```<layer ID>``` could be set as 1, 2 or 3, the flag ```-with_tof``` forces all hit times to be recalculated in order to match new LORs lengths. It is also better to turn off warnings during the execution:
```
$ python -W ignore reduce_multilayer.py SOME_INPUT_ASCII_DATA -l 2 -with_tof
```
(!) IMPORTANT: the application implies that hit times are in ps, and not ns, as described in [GOJA description](https://github.com/JPETTomography/j-pet-gate-tools/tree/master/examples/goja "see GOJA output").

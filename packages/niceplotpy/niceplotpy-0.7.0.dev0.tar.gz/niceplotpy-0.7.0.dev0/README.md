# A python module to make nice looking plots so I don't re-do the same thing all the time.

## Installation

To install, navigate to your local niceplot repo and do:

```python
pip install -e .
```

## Dependencies: 

Niceplot uses the [atlasify](https://atlasify.readthedocs.io) and [uproot](https://uproot.readthedocs.io) packages.

## Usage: 

After installation, the the module can be used with:

```python
niceplot CONFIG_FILE
```
Where the `CONFIG_FILE` includes all information on which plots to make, variables to plot, etc. For an example config file, see: [example_configs/GMSB.yaml](https://gitlab.cern.ch/jwuerzin/nice-plot/-/blob/master/example_configs/GMSB.yaml).

Currently supported plot types are: `1dratio` and `2dhist`.

## ToDo:

- Implement automatic mask handling
- Add more options for plots:
  - 2dplot with custom z-axis
  - data/MC plots
- Switch to [mplhep](https://mplhep.readthedocs.io/en/latest/) for style?
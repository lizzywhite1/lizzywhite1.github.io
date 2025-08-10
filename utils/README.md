# Utils Directory

This directory contains utility scripts and documentation for managing interactive plots in the Jekyll blog.

## Files

- `generate_plot.py` - Helper script to generate and move interactive plots
- `INTERACTIVE_PLOTS_SETUP.md` - Comprehensive setup guide for interactive plots
- `README.md` - This file

## Usage

### Generating Interactive Plots

```bash
# From the utils directory
python generate_plot.py interactive_plot.py

# With custom output name
python generate_plot.py my_plot_script.py my_custom_plot
```

### Directory Structure

```
utils/
├── generate_plot.py              # Plot generation helper
├── INTERACTIVE_PLOTS_SETUP.md    # Setup documentation
└── README.md                     # This file

plots/
├── interactive_plot.py           # Main plot generation script
└── [other plot scripts]          # Additional plot scripts

assets/plots/
├── orthogonal_projection_3d.html # Generated HTML plots
├── orthogonal_projection_2d.html
└── [other generated plots]       # Additional generated plots
```

## Workflow

1. Create plot scripts in the `../plots/` directory
2. Run `generate_plot.py` from the `utils/` directory
3. Plots are automatically moved to `../assets/plots/`
4. Include plots in blog posts using the Jekyll include

## Dependencies

Make sure you have the required Python packages installed:
```bash
pip install plotly numpy
``` 
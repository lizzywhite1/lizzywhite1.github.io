# Plots Directory

This directory contains Python scripts for generating interactive Plotly visualizations for the Jekyll blog.

## Files

- `interactive_plot.py` - Main script for orthogonal projection visualization
- `README.md` - This file

## Available Plots

### Orthogonal Projection Visualization (`interactive_plot.py`)

Creates two interactive visualizations:

1. **3D Orthogonal Projection** - Shows a 2D subspace in 3D space with:
   - Subspace S (light blue plane) spanned by basis functions φ₀(x) = 1 and φ₁(x)
   - Vector y (green arrow) representing target values
   - Orthogonal projection ŷ = Proj_S(y) (orange arrow)
   - Residual vector (purple arrow) orthogonal to the subspace

2. **2D Vector Decomposition** - Shows vector decomposition in 2D space

## Usage

### Direct Execution
```bash
# From the plots directory
python interactive_plot.py
```

### Using the Helper Script
```bash
# From the utils directory
python generate_plot.py interactive_plot.py
```

## Output

The script generates:
- `orthogonal_projection_3d.html` - 3D interactive visualization
- `orthogonal_projection_2d.html` - 2D interactive visualization

These files are automatically moved to `../assets/plots/` when using the helper script.

## Creating New Plots

1. Create a new Python script in this directory
2. Use Plotly to create interactive visualizations
3. Generate HTML output using `fig.write_html("filename.html")`
4. Use the helper script to move files to the assets directory

## Example Template

```python
import plotly.graph_objects as go
import numpy as np

def create_my_plot():
    fig = go.Figure()
    # Add your plot elements here
    return fig

if __name__ == "__main__":
    fig = create_my_plot()
    fig.write_html("my_plot.html")
```

## Dependencies

- `plotly` - For interactive visualizations
- `numpy` - For numerical computations 
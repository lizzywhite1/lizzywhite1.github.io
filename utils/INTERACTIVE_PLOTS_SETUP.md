# Interactive Plots Setup for Jekyll Blog

This guide explains how to set up and use interactive Plotly plots in your Jekyll blog.

## What We've Set Up

1. **Interactive Plot Script** (`../plots/interactive_plot.py`) - Creates Plotly visualizations
2. **Jekyll Include** (`../_includes/interactive_plot.html`) - Embeds plots in blog posts
3. **Assets Directory** (`../assets/plots/`) - Stores HTML plot files
4. **Helper Script** (`generate_plot.py`) - Automates plot generation and placement
5. **Utils Directory** (`../utils/`) - Contains helper scripts and documentation

## How It Works

Instead of showing static code blocks, your blog now displays **interactive 3D plots** that readers can:
- Rotate and zoom
- Hover over elements for details
- Interact with legends
- View from different angles

## Current Implementation

Your blog post now includes this line:
```liquid
{% include interactive_plot.html plot_file="assets/plots/orthogonal_projection_3d.html" width="800" height="600" caption="Interactive 3D visualization showing the orthogonal projection of vector y onto subspace S spanned by basis functions φ₀(x) = 1 and φ₁(x). The plot demonstrates how the least squares solution corresponds to finding the orthogonal projection." %}
```

This will render as an interactive 3D plot showing:
- **Subspace S** (light blue plane) - The 2D subspace spanned by basis functions
- **Vector y** (green arrow) - The true target values
- **ŷ = Proj_S(y)** (orange arrow) - The orthogonal projection (least squares prediction)
- **Residual** (purple arrow) - The difference between y and its projection

## Creating New Interactive Plots

### Method 1: Using the Helper Script
```bash
# Navigate to utils directory
cd utils

# Generate and move plots automatically
python generate_plot.py interactive_plot.py

# With custom output name
python generate_plot.py my_plot_script.py my_custom_plot
```

### Method 2: Manual Process
1. Create a Python script using Plotly
2. Generate HTML: `fig.write_html("my_plot.html")`
3. Move to assets: `mv my_plot.html ../assets/plots/`
4. Include in blog: `{% include interactive_plot.html plot_file="assets/plots/my_plot.html" %}`

## Example: Creating a New Plot

```python
import plotly.graph_objects as go
import numpy as np

def create_my_plot():
    # Your plot code here
    fig = go.Figure()
    # ... add traces, layout, etc.
    return fig

if __name__ == "__main__":
    fig = create_my_plot()
    fig.write_html("my_new_plot.html")
```

Then run:
```bash
cd utils
python generate_plot.py my_plot_script.py
```

## Including in Blog Posts

### Basic Usage
```liquid
{% include interactive_plot.html plot_file="assets/plots/orthogonal_projection_3d.html" %}
```

### With Custom Size
```liquid
{% include interactive_plot.html plot_file="assets/plots/orthogonal_projection_3d.html" width="1000" height="700" %}
```

### With Caption
```liquid
{% include interactive_plot.html plot_file="assets/plots/orthogonal_projection_3d.html" caption="This plot shows the geometric interpretation of linear regression." %}
```

## Available Plots

- `orthogonal_projection_3d.html` - 3D orthogonal projection visualization
- `orthogonal_projection_2d.html` - 2D vector decomposition

## Benefits

1. **Interactive**: Readers can explore the visualization
2. **Educational**: Better understanding of complex concepts
3. **Professional**: Modern, engaging blog content
4. **Responsive**: Works on different devices
5. **Fast**: Plots load quickly as embedded HTML

## Troubleshooting

### Plot Not Showing
- Check that the HTML file exists in `../assets/plots/`
- Verify the path in the include statement
- Ensure Jekyll is building the site correctly

### Plot Too Large/Small
- Adjust `width` and `height` parameters in the include
- Consider responsive design for mobile devices

### Performance Issues
- Keep plot complexity reasonable
- Consider lazy loading for multiple plots
- Optimize data size in plots

## Next Steps

1. **Test the current plot** by building your Jekyll site
2. **Create additional plots** for other concepts in your blog
3. **Customize the styling** in `../_includes/interactive_plot.html`
4. **Add more interactive features** like animations or sliders

## Dependencies

Make sure you have these Python packages installed:
```bash
pip install plotly numpy
```

The plots are now ready to use in your Jekyll blog! 🎉 
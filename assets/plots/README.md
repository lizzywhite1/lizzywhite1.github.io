# Interactive Plots for Jekyll Blog

This directory contains interactive Plotly HTML plots that can be embedded in Jekyll blog posts.

## Available Plots

- `orthogonal_projection_3d.html` - 3D visualization of orthogonal projection in linear regression
- `orthogonal_projection_2d.html` - 2D vector decomposition visualization

## How to Use

### In Jekyll Blog Posts

Use the `interactive_plot.html` include to embed plots:

```liquid
{% include interactive_plot.html plot_file="assets/plots/orthogonal_projection_3d.html" width="800" height="600" caption="Your caption here" %}
```

### Parameters

- `plot_file`: Path to the HTML plot file (relative to site root)
- `width`: Width of the iframe (default: 800)
- `height`: Height of the iframe (default: 600)
- `caption`: Optional caption text below the plot

## Creating New Interactive Plots

1. Create a Python script using Plotly
2. Generate HTML output using `fig.write_html("filename.html")`
3. Place the HTML file in this directory
4. Use the include tag in your blog post

## Example Usage in Blog Post

```markdown
Here's an interactive visualization of the orthogonal projection:

{% include interactive_plot.html plot_file="assets/plots/orthogonal_projection_3d.html" width="800" height="600" caption="Interactive 3D visualization showing orthogonal projection in linear regression." %}
```

## Features

- **Interactive**: Users can rotate, zoom, and hover over elements
- **Responsive**: Plots adapt to different screen sizes
- **Embedded**: Plots are embedded as iframes for better performance
- **Customizable**: Width, height, and captions can be customized 
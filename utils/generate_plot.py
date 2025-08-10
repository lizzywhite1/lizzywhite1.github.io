#!/usr/bin/env python3
"""
Helper script to generate interactive plots and move them to the correct location for Jekyll.
"""

import os
import sys
from pathlib import Path

def generate_and_move_plot(script_name, output_name=None):
    """
    Generate a plot from a Python script and move it to the assets/plots directory.
    
    Args:
        script_name (str): Name of the Python script to run
        output_name (str): Optional custom name for the output HTML file
    """
    # Get the current directory (now in utils folder)
    current_dir = Path.cwd()
    assets_dir = current_dir.parent / "assets" / "plots"
    
    # Ensure assets directory exists
    assets_dir.mkdir(parents=True, exist_ok=True)
    
    # Run the script (handle both relative and absolute paths)
    print(f"Running {script_name}...")
    
    # Check if script is in plots directory
    plots_dir = current_dir.parent / "plots"
    script_path = plots_dir / script_name
    
    if script_path.exists():
        # Run from plots directory
        os.system(f"cd '{plots_dir}' && python {script_name}")
        # Find HTML files in plots directory
        html_files = list(plots_dir.glob("*.html"))
    else:
        # Try running from current directory
        os.system(f"python {script_name}")
        # Find HTML files in current directory
        html_files = list(current_dir.glob("*.html"))
    
    if not html_files:
        print("No HTML files found. Make sure your script generates HTML output.")
        return
    
    # Move files to assets directory
    for html_file in html_files:
        if output_name and html_file.name.startswith("orthogonal_projection"):
            # Use custom name if provided
            new_name = output_name
            if not new_name.endswith('.html'):
                new_name += '.html'
        else:
            new_name = html_file.name
            
        destination = assets_dir / new_name
        html_file.rename(destination)
        print(f"Moved {html_file.name} to {destination}")
    
    print(f"\nPlots are now available in {assets_dir}")
    print("You can include them in your blog posts using:")
    print(f"{{% include interactive_plot.html plot_file=\"assets/plots/{new_name}\" width=\"800\" height=\"600\" %}}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_plot.py <script_name> [output_name]")
        print("Example: python generate_plot.py interactive_plot.py")
        sys.exit(1)
    
    script_name = sys.argv[1]
    output_name = sys.argv[2] if len(sys.argv) > 2 else None
    
    # Check if script exists in plots directory
    current_dir = Path.cwd()
    plots_dir = current_dir.parent / "plots"
    script_path = plots_dir / script_name
    
    if not script_path.exists() and not os.path.exists(script_name):
        print(f"Script {script_name} not found in plots directory or current directory!")
        print(f"Checked locations:")
        print(f"  - {script_path}")
        print(f"  - {os.path.abspath(script_name)}")
        sys.exit(1)
    
    generate_and_move_plot(script_name, output_name) 
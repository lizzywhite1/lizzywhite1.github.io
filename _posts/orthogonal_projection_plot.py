import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
import matplotlib.patches as mpatches

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def do_3d_projection(self, renderer=None):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        return np.min(zs)

def create_orthogonal_projection_plot():
    """
    Create an educational plot showing:
    - A 2D subspace S in 3D space spanned by basis vectors [1, 0, 0] and [0, 1, 0]
    - A vector y not in the subspace pointing from origin
    - The orthogonal projection of y onto the subspace S
    - The residual vector (y - projection)
    """
    
    # Set up the figure
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Define the basis vectors for the subspace S
    # In the context of linear regression, these would be the feature vectors
    phi_0 = np.array([1, 0, 0])  # First basis vector (constant term)
    phi_1 = np.array([0, 1, 0])  # Second basis vector (first feature)
    
    # Define the vector y (target values in linear regression)
    y = np.array([2, 3, 4])
    
    # Calculate the orthogonal projection of y onto the subspace S
    # This is equivalent to the least squares solution
    # Projection = (y·φ₀)φ₀ + (y·φ₁)φ₁
    proj_y = np.dot(y, phi_0) * phi_0 + np.dot(y, phi_1) * phi_1
    
    # Calculate the residual vector (orthogonal to the subspace)
    residual = y - proj_y
    
    # Create the subspace plane
    # Generate points in the subspace spanned by phi_0 and phi_1
    u = np.linspace(-1, 3, 20)
    v = np.linspace(-1, 3, 20)
    U, V = np.meshgrid(u, v)
    
    # Points in the subspace: s = u*phi_0 + v*phi_1
    X = U * phi_0[0] + V * phi_1[0]
    Y = U * phi_0[1] + V * phi_1[1]
    Z = U * phi_0[2] + V * phi_1[2]
    
    # Plot the subspace as a semi-transparent plane
    ax.plot_surface(X, Y, Z, alpha=0.3, color='lightblue', label='Subspace S')
    
    # Plot the basis vectors
    ax.quiver(0, 0, 0, phi_0[0], phi_0[1], phi_0[2], 
              color='red', arrow_length_ratio=0.1, linewidth=3, label='φ₀(x) = 1')
    ax.quiver(0, 0, 0, phi_1[0], phi_1[1], phi_1[2], 
              color='blue', arrow_length_ratio=0.1, linewidth=3, label='φ₁(x)')
    
    # Plot the vector y
    ax.quiver(0, 0, 0, y[0], y[1], y[2], 
              color='green', arrow_length_ratio=0.1, linewidth=3, label='y')
    
    # Plot the orthogonal projection
    ax.quiver(0, 0, 0, proj_y[0], proj_y[1], proj_y[2], 
              color='orange', arrow_length_ratio=0.1, linewidth=3, label='Proj_S(y)')
    
    # Plot the residual vector (from projection to y)
    ax.quiver(proj_y[0], proj_y[1], proj_y[2], residual[0], residual[1], residual[2], 
              color='purple', arrow_length_ratio=0.1, linewidth=3, label='Residual')
    
    # Add a dashed line from y to its projection to show the distance
    ax.plot([y[0], proj_y[0]], [y[1], proj_y[1]], [y[2], proj_y[2]], 
            'k--', alpha=0.7, linewidth=2)
    
    # Add text annotations
    ax.text(y[0] + 0.2, y[1] + 0.2, y[2] + 0.2, 'y', fontsize=12, fontweight='bold')
    ax.text(proj_y[0] + 0.2, proj_y[1] + 0.2, proj_y[2] + 0.2, 'ŷ', fontsize=12, fontweight='bold')
    ax.text(phi_0[0] + 0.2, phi_0[1] + 0.2, phi_0[2] + 0.2, 'φ₀', fontsize=12, fontweight='bold')
    ax.text(phi_1[0] + 0.2, phi_1[1] + 0.2, phi_1[2] + 0.2, 'φ₁', fontsize=12, fontweight='bold')
    
    # Set axis limits and labels
    ax.set_xlim([-1, 4])
    ax.set_ylim([-1, 4])
    ax.set_zlim([-1, 5])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Orthogonal Projection in Linear Regression\n2D Subspace S in 3D Space', 
                 fontsize=14, fontweight='bold', pad=20)
    
    # Add legend
    legend_elements = [
        mpatches.Patch(color='lightblue', alpha=0.3, label='Subspace S'),
        mpatches.Patch(color='red', label='φ₀(x) = 1 (constant term)'),
        mpatches.Patch(color='blue', label='φ₁(x) (first feature)'),
        mpatches.Patch(color='green', label='y (target vector)'),
        mpatches.Patch(color='orange', label='ŷ = Proj_S(y) (prediction)'),
        mpatches.Patch(color='purple', label='Residual (y - ŷ)')
    ]
    ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1.15, 1))
    
    # Add explanatory text
    explanation = """
    Geometric Interpretation of Linear Regression:
    
    • The subspace S is spanned by the basis functions φ₀(x) = 1 and φ₁(x)
    • Vector y represents the true target values
    • ŷ = Proj_S(y) is the orthogonal projection (least squares prediction)
    • The residual vector (y - ŷ) is orthogonal to the subspace S
    • Minimizing ||y - ŷ||² is equivalent to finding the orthogonal projection
    
    This visualization shows why the least squares solution
    corresponds to the orthogonal projection of y onto S.
    """
    
    # Add text box with explanation
    ax.text2D(0.02, 0.02, explanation, transform=ax.transAxes, fontsize=10,
              bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))
    
    # Set viewing angle for better visualization
    ax.view_init(elev=20, azim=45)
    
    plt.tight_layout()
    return fig, ax

def create_additional_visualization():
    """
    Create a second plot showing the relationship between the vectors
    and the projection matrix concept
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # First subplot: Vector decomposition
    ax1.set_aspect('equal')
    
    # Define vectors
    y = np.array([3, 4])
    phi_0 = np.array([1, 0])
    phi_1 = np.array([0, 1])
    
    # Projection
    proj_y = np.dot(y, phi_0) * phi_0 + np.dot(y, phi_1) * phi_1
    residual = y - proj_y
    
    # Plot vectors
    ax1.quiver(0, 0, phi_0[0], phi_0[1], angles='xy', scale_units='xy', scale=1, 
               color='red', label='φ₀ = [1, 0]')
    ax1.quiver(0, 0, phi_1[0], phi_1[1], angles='xy', scale_units='xy', scale=1, 
               color='blue', label='φ₁ = [0, 1]')
    ax1.quiver(0, 0, y[0], y[1], angles='xy', scale_units='xy', scale=1, 
               color='green', label='y = [3, 4]')
    ax1.quiver(0, 0, proj_y[0], proj_y[1], angles='xy', scale_units='xy', scale=1, 
               color='orange', label='ŷ = Proj_S(y)')
    ax1.quiver(proj_y[0], proj_y[1], residual[0], residual[1], angles='xy', scale_units='xy', scale=1, 
               color='purple', label='Residual')
    
    # Add grid and labels
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim([-1, 5])
    ax1.set_ylim([-1, 5])
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_title('2D Vector Decomposition\nOrthogonal Projection', fontweight='bold')
    ax1.legend()
    
    # Second subplot: Projection matrix visualization
    ax2.set_aspect('equal')
    
    # Create a grid of points to show the projection transformation
    x = np.linspace(-2, 4, 20)
    y = np.linspace(-2, 4, 20)
    X, Y = np.meshgrid(x, y)
    
    # Apply projection matrix P = Φ(Φ^T Φ)^(-1) Φ^T
    # For our simple case with orthonormal basis, P = φ₀φ₀^T + φ₁φ₁^T
    P = np.outer(phi_0, phi_0) + np.outer(phi_1, phi_1)
    
    # Apply projection to all points
    points = np.vstack([X.ravel(), Y.ravel()])
    projected_points = P @ points
    X_proj = projected_points[0].reshape(X.shape)
    Y_proj = projected_points[1].reshape(Y.shape)
    
    # Plot original points and their projections
    ax2.scatter(X, Y, c='lightblue', alpha=0.3, s=10, label='Original points')
    ax2.scatter(X_proj, Y_proj, c='orange', alpha=0.6, s=10, label='Projected points')
    
    # Draw some example projection lines
    for i in range(0, len(x), 4):
        for j in range(0, len(y), 4):
            ax2.plot([X[i, j], X_proj[i, j]], [Y[i, j], Y_proj[i, j]], 
                    'k-', alpha=0.2, linewidth=0.5)
    
    # Add basis vectors
    ax2.quiver(0, 0, phi_0[0], phi_0[1], angles='xy', scale_units='xy', scale=1, 
               color='red', linewidth=3, label='φ₀')
    ax2.quiver(0, 0, phi_1[0], phi_1[1], angles='xy', scale_units='xy', scale=1, 
               color='blue', linewidth=3, label='φ₁')
    
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim([-2, 4])
    ax2.set_ylim([-2, 4])
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_title('Projection Matrix P\nP = Φ(Φ^T Φ)^(-1) Φ^T', fontweight='bold')
    ax2.legend()
    
    plt.tight_layout()
    return fig

if __name__ == "__main__":
    # Create the main 3D plot
    fig1, ax1 = create_orthogonal_projection_plot()
    plt.savefig('orthogonal_projection_3d.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # Create the additional 2D visualization
    fig2 = create_additional_visualization()
    plt.savefig('orthogonal_projection_2d.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("Plots created successfully!")
    print("Files saved as:")
    print("- orthogonal_projection_3d.png")
    print("- orthogonal_projection_2d.png") 
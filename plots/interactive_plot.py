import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from plotly.subplots import make_subplots

def create_interactive_orthogonal_projection():
    """
    Create an interactive Plotly visualization showing:
    - A 2D subspace S in 3D space spanned by basis vectors [1, 0, 0] and [0, 1, 0]
    - A vector y not in the subspace pointing from origin
    - The orthogonal projection of y onto the subspace S
    - The residual vector (y - projection)
    """
    
    # Define the basis vectors for the subspace S
    phi_0 = np.array([1, 0, 0])  # First basis vector (constant term)
    phi_1 = np.array([0, 1, 0])  # Second basis vector (first feature)
    
    # Define the vector y (target values in linear regression)
    y = np.array([2, 3, 4])
    
    # Calculate the orthogonal projection of y onto the subspace S
    proj_y = np.dot(y, phi_0) * phi_0 + np.dot(y, phi_1) * phi_1
    
    # Calculate the residual vector (orthogonal to the subspace)
    residual = y - proj_y
    
    # Create the subspace plane
    u = np.linspace(-1, 3, 20)
    v = np.linspace(-1, 3, 20)
    U, V = np.meshgrid(u, v)
    
    # Points in the subspace: s = u*phi_0 + v*phi_1
    X = U * phi_0[0] + V * phi_1[0]
    Y = U * phi_0[1] + V * phi_1[1]
    Z = U * phi_0[2] + V * phi_1[2]
    
    # Create the 3D plot
    fig = go.Figure()
    
    # Add the subspace plane
    fig.add_trace(go.Surface(
        x=X, y=Y, z=Z,
        colorscale='Blues',
        opacity=0.3,
        showscale=False,
        name='Subspace S',
        hovertemplate='Subspace S<br>'
    ))
    
    # Add basis vectors
    fig.add_trace(go.Scatter3d(
        x=[0, phi_0[0]], y=[0, phi_0[1]], z=[0, phi_0[2]],
        mode='lines+markers',
        line=dict(color='red', width=8),
        marker=dict(size=5),
        name='φ₀(x) = 1 (constant term)',
        hovertemplate='φ₀(x) = 1<br>Constant term<br>'
    ))
    
    fig.add_trace(go.Scatter3d(
        x=[0, phi_1[0]], y=[0, phi_1[1]], z=[0, phi_1[2]],
        mode='lines+markers',
        line=dict(color='blue', width=8),
        marker=dict(size=5),
        name='φ₁(x) (first feature)',
        hovertemplate='φ₁(x)<br>First feature<br>'
    ))
    
    # Add vector y
    fig.add_trace(go.Scatter3d(
        x=[0, y[0]], y=[0, y[1]], z=[0, y[2]],
        mode='lines+markers',
        line=dict(color='green', width=8),
        marker=dict(size=5),
        name='y (target vector)',
        hovertemplate='y<br>Target vector<br>'
    ))
    
    # Add orthogonal projection
    fig.add_trace(go.Scatter3d(
        x=[0, proj_y[0]], y=[0, proj_y[1]], z=[0, proj_y[2]],
        mode='lines+markers',
        line=dict(color='orange', width=8),
        marker=dict(size=5),
        name='ŷ = Proj_S(y) (prediction)',
        hovertemplate='ŷ = Proj_S(y)<br>Least squares prediction<br>'
    ))
    
    # Add residual vector
    fig.add_trace(go.Scatter3d(
        x=[proj_y[0], y[0]], y=[proj_y[1], y[1]], z=[proj_y[2], y[2]],
        mode='lines+markers',
        line=dict(color='purple', width=8, dash='dash'),
        marker=dict(size=5),
        name='Residual (y - ŷ)',
        hovertemplate='Residual<br>y - ŷ<br>'
    ))
    
    # Add text annotations
    fig.add_trace(go.Scatter3d(
        x=[y[0] + 0.2], y=[y[1] + 0.2], z=[y[2] + 0.2],
        mode='text',
        text=['y'],
        textposition='middle center',
        textfont=dict(size=16, color='green'),
        showlegend=False,
        hoverinfo='skip'
    ))
    
    fig.add_trace(go.Scatter3d(
        x=[proj_y[0] + 0.2], y=[proj_y[1] + 0.2], z=[proj_y[2] + 0.2],
        mode='text',
        text=['ŷ'],
        textposition='middle center',
        textfont=dict(size=16, color='orange'),
        showlegend=False,
        hoverinfo='skip'
    ))
    
    # Update layout
    fig.update_layout(
        title={
            'text': 'Orthogonal Projection in Linear Regression<br>2D Subspace S in 3D Space',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20}
        },
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z',
            camera=dict(
                eye=dict(x=1.5, y=1.5, z=1.5)
            ),
            aspectmode='cube'
        ),
        width=800,
        height=600,
        showlegend=True,
        legend=dict(
            x=1.02,
            y=1,
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='black',
            borderwidth=1
        )
    )
    
    # Add explanation text
    fig.add_annotation(
        x=0.02,
        y=0.02,
        xref='paper',
        yref='paper',
        text="<b>Geometric Interpretation:</b><br>" +
             "• Subspace S is spanned by φ₀(x) = 1 and φ₁(x)<br>" +
             "• Vector y represents true target values<br>" +
             "• ŷ = Proj_S(y) is the orthogonal projection<br>" +
             "• Residual vector (y - ŷ) is orthogonal to S<br>" +
             "• Minimizing ||y - ŷ||² = finding orthogonal projection",
        showarrow=False,
        bgcolor='rgba(255,255,255,0.8)',
        bordercolor='black',
        borderwidth=1,
        font=dict(size=12)
    )
    
    return fig

def create_2d_decomposition_plot():
    """
    Create a 2D visualization showing vector decomposition
    """
    # Define vectors
    y = np.array([3, 4])
    phi_0 = np.array([1, 0])
    phi_1 = np.array([0, 1])
    
    # Projection
    proj_y = np.dot(y, phi_0) * phi_0 + np.dot(y, phi_1) * phi_1
    residual = y - proj_y
    
    fig = go.Figure()
    
    # Add vectors
    fig.add_trace(go.Scatter(
        x=[0, phi_0[0]], y=[0, phi_0[1]],
        mode='lines+markers',
        line=dict(color='red', width=5),
        marker=dict(size=8),
        name='φ₀ = [1, 0]'
    ))
    
    fig.add_trace(go.Scatter(
        x=[0, phi_1[0]], y=[0, phi_1[1]],
        mode='lines+markers',
        line=dict(color='blue', width=5),
        marker=dict(size=8),
        name='φ₁ = [0, 1]'
    ))
    
    fig.add_trace(go.Scatter(
        x=[0, y[0]], y=[0, y[1]],
        mode='lines+markers',
        line=dict(color='green', width=5),
        marker=dict(size=8),
        name='y = [3, 4]'
    ))
    
    fig.add_trace(go.Scatter(
        x=[0, proj_y[0]], y=[0, proj_y[1]],
        mode='lines+markers',
        line=dict(color='orange', width=5),
        marker=dict(size=8),
        name='ŷ = Proj_S(y)'
    ))
    
    fig.add_trace(go.Scatter(
        x=[proj_y[0], y[0]], y=[proj_y[1], y[1]],
        mode='lines+markers',
        line=dict(color='purple', width=5, dash='dash'),
        marker=dict(size=8),
        name='Residual'
    ))
    
    fig.update_layout(
        title='2D Vector Decomposition - Orthogonal Projection',
        xaxis_title='X',
        yaxis_title='Y',
        width=600,
        height=500,
        showlegend=True
    )
    
    return fig

if __name__ == "__main__":
    # Create the interactive plots
    fig_3d = create_interactive_orthogonal_projection()
    fig_2d = create_2d_decomposition_plot()
    
    # Save as HTML files
    fig_3d.write_html("orthogonal_projection_3d.html")
    fig_2d.write_html("orthogonal_projection_2d.html")
    
    print("Interactive plots created successfully!")
    print("Files saved as:")
    print("- orthogonal_projection_3d.html")
    print("- orthogonal_projection_2d.html") 
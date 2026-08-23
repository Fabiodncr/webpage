import numpy as np
import plotly.graph_objects as go

from pathlib import Path
cartella = Path(__file__).parent
percorso_html = cartella / "grafico.html"


t = np.linspace(0, 10, 200)
x = np.cos(t)
y = np.sin(t)
z = t

fig = go.Figure()

curve = go.Scatter3d(
    x=x, y=y, z=z,
    mode='lines',
    name='curva'
)

point = go.Scatter3d(
    x=[x[0]],
    y=[y[0]],
    z=[z[0]],
    mode='markers',
    marker=dict(size=6, color='red'),
    name='punto'
)

fig.add_trace(curve)
fig.add_trace(point)

frames = []
for i in range(len(t)):
    frames.append(go.Frame(
        data=[
            go.Scatter3d(x=x, y=y, z=z),  # curva fissa
            go.Scatter3d(x=[x[i]], y=[y[i]], z=[z[i]])  # punto mobile
        ],
        name=str(i)
    ))

fig.frames = frames

fig.update_layout(
    paper_bgcolor='#1e293b',
    title="Curva 3D con punto mobile",
    scene=dict(
        xaxis_title="X",
        yaxis_title="Y",
        zaxis_title="Z"
    ),
    sliders=[{
        "steps": [
            {
                "method": "animate",
                "args": [[i], {
                    "mode": "immediate",
                    "frame": {"duration": 0, "redraw": True},
                    "transition": {"duration": 0}
                }],
                "label": f"{t[i]:.2f}"
            }
            for i in range(len(t))
        ],
        "currentvalue": {"prefix": "t = "}
    }]
)
fig.show()
fig.write_html(percorso_html)
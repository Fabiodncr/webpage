import numpy as np
import plotly.graph_objects as go
import plotly.subplots as sp


from pathlib import Path
cartella = Path(__file__).parent
percorso_html = cartella / "grafico.html"

t = np.linspace(0, 10, 200)

x = np.cos(t)
y = np.sin(t)

fig = sp.make_subplots(
    rows=3, cols=1,
    specs=[[{"type": "scatter"}],
           [{"type": "scatter"}],
           [{"type": "scatter"}]],
    row_heights=[0.25, 0.25, 0.5]
)

curve_1 = go.Scatter(
    x=t, y=x,
    mode='lines'
)

curve_2 = go.Scatter(
    x=t, y=y,
    mode='lines'
)

curve_3 = go.Scatter(
    x=x, y=y,
    mode='lines'
)

point_1 = go.Scatter(
    x=[t[0]],
    y=[x[0]],
    mode='markers',
    marker=dict(size=6, color='red')
)
point_2 = go.Scatter(
    x=[t[0]],
    y=[y[0]],
    mode='markers',
    marker=dict(size=6, color='red')
)
point_3 = go.Scatter(
    x=[x[0]],
    y=[y[0]],
    mode='markers',
    marker=dict(size=6, color='red')
)

fig.add_trace(curve_1,  row=1, col = 1)
fig.add_trace(point_1,  row=1, col = 1)
fig.add_trace(curve_2, row = 2, col = 1)
fig.add_trace(point_2, row = 2, col = 1)
fig.add_trace(curve_3, row = 3, col = 1)
fig.add_trace(point_3, row = 3, col = 1)

frames = []
for i in range(len(t)):
    frames.append(go.Frame(
        data=[
            go.Scatter(x=t, y=x),
            go.Scatter(x=[t[i]], y=[x[i]]),
            go.Scatter(x=t, y=y),
            go.Scatter(x=[t[i]], y=[y[i]]),
            go.Scatter(x=x, y=y),
            go.Scatter(x=[x[i]], y=[y[i]])
        ],
        name=str(i)
    ))

fig.frames = frames

fig.update_layout(
    title="CAZZI",
    paper_bgcolor='#1e293b',
    height=650,
    width=600,
    xaxis1=dict(range=[0, 10]),
    xaxis2=dict(range=[0, 10]),      
    xaxis3=dict(range=[-1.1, 1.1]),            
    yaxis1=dict(range=[-1.1, 1.1]),       
    yaxis2=dict(range=[-1.1, 1.1]),      
    yaxis3=dict(range=[-1.1, 1.1]), 
    uirevision=True,
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

fig.update_yaxes(
    scaleanchor="x3",
    scaleratio=1,
    row=3,
    col=1
)

fig.show()
fig.write_html(percorso_html)
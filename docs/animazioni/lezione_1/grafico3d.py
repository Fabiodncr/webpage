import numpy as np
import plotly.graph_objects as go

BG = "#021502"
CHALK = "#f2efe6"
GRID = "rgba(242,239,230,0.15)"
GIALLO = "#ffd166"

# Curva: x = cos t, y = sin t, z = t
N = 80
ts = np.linspace(0, 4 * np.pi, N)
xs, ys, zs = np.cos(ts), np.sin(ts), ts

# Traccia 0: curva intera (tenue)
# Traccia 1: tratto già percorso (si aggiorna)
# Traccia 2: punto mobile (si aggiorna)
fig = go.Figure(
    data=[
        go.Scatter3d(x=xs, y=ys, z=zs, mode="lines",
                     line=dict(color="rgba(242,239,230,0.35)", width=3),
                     hoverinfo="skip"),
        go.Scatter3d(x=xs[:1], y=ys[:1], z=zs[:1], mode="lines",
                     line=dict(color=CHALK, width=6), hoverinfo="skip"),
        go.Scatter3d(x=xs[:1], y=ys[:1], z=zs[:1], mode="markers",
                     marker=dict(color=GIALLO, size=7), hoverinfo="skip"),
    ],
    frames=[
        go.Frame(
            name=str(k),
            traces=[1, 2],   # aggiorna solo tratto percorso e punto
            data=[
                go.Scatter3d(x=xs[:k + 1], y=ys[:k + 1], z=zs[:k + 1]),
                go.Scatter3d(x=xs[k:k + 1], y=ys[k:k + 1], z=zs[k:k + 1]),
            ],
        )
        for k in range(N)
    ],
)

asse = dict(
    backgroundcolor=BG, showbackground=True,
    gridcolor=GRID, zerolinecolor=CHALK, linecolor=CHALK, color=CHALK,
)

fig.update_layout(
    paper_bgcolor=BG,
    font=dict(family="Caveat, cursive", color=CHALK, size=18),
    showlegend=False,
    margin=dict(l=0, r=0, t=0, b=0),
    scene=dict(
        bgcolor=BG,
        xaxis=dict(asse, title="x", range=[-1.5, 1.5]),
        yaxis=dict(asse, title="y", range=[-1.5, 1.5]),
        zaxis=dict(asse, title="z", range=[0, 4 * np.pi]),
        aspectmode="manual",
        aspectratio=dict(x=1, y=1, z=1.6),
        camera=dict(eye=dict(x=1.7, y=1.7, z=0.8)),
    ),
    updatemenus=[dict(
        type="buttons", direction="left", showactive=False,
        x=0.02, y=0.02, xanchor="left", yanchor="bottom",
        bgcolor=BG, bordercolor=CHALK, font=dict(color=CHALK),
        buttons=[
            dict(label="▶", method="animate",
                 args=[None, dict(frame=dict(duration=40, redraw=True),
                                  fromcurrent=True, transition=dict(duration=0))]),
            dict(label="❚❚", method="animate",
                 args=[[None], dict(frame=dict(duration=0, redraw=False),
                                    mode="immediate", transition=dict(duration=0))]),
        ],
    )],
    sliders=[dict(
        x=0.15, y=0.02, xanchor="left", yanchor="bottom", len=0.8,
        pad=dict(t=0, b=0),
        bgcolor="rgba(242,239,230,0.25)", bordercolor=CHALK,
        activebgcolor=GIALLO, tickcolor=CHALK,
        font=dict(color=CHALK),
        currentvalue=dict(visible=False),
        steps=[
            dict(
                method="animate",
                label=f"{ts[k]:.1f}" if k % 10 == 0 else "",
                args=[[str(k)], dict(mode="immediate",
                                     frame=dict(duration=0, redraw=True),
                                     transition=dict(duration=0))],
            )
            for k in range(N)
        ],
    )],
)

html = fig.to_html(
    full_html=False,
    include_plotlyjs="cdn",
    default_width="100%",
    default_height="100%",
    auto_play=False,
    config={"displayModeBar": False, "responsive": True},
)

pagina = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Caveat&display=swap" rel="stylesheet">
<style>
  html, body {{ margin: 0; height: 100%; background: {BG}; overflow: hidden; }}
</style>
</head>
<body>
{html}
</body>
</html>"""

with open("elica.html", "w", encoding="utf-8") as f:
    f.write(pagina)

print("Fatto: elica.html creato")
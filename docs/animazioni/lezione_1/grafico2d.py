import numpy as np
import plotly.graph_objects as go
from pathlib import Path

cartella = Path(__file__).parent
percorso_html = cartella / "grafico2d.html"

# Colori (BG = sfondo del tema scuro di VitePress)
BG = "#021502"
CHALK = "#f2efe6"
GRID = "rgba(242,239,230,0.12)"

x = np.linspace(-3, 3, 400)
fig = go.Figure()

fig.add_scatter(x=x, y=np.sin(x), mode="lines",
                line=dict(width=2.5, color=CHALK), name="sin(x)")

fig.update_layout(
    paper_bgcolor=BG,
    plot_bgcolor=BG,
    font=dict(family="Georgia, serif", color=CHALK, size=18),
    xaxis=dict(gridcolor=GRID, zerolinecolor=CHALK, linecolor=CHALK, showline=True),
    yaxis=dict(gridcolor=GRID, zerolinecolor=CHALK, linecolor=CHALK, showline=True),
    showlegend=False,
    margin=dict(l=40, r=20, t=60, b=40),
)
fig.show(),

html = fig.to_html(
    full_html=False,
    include_plotlyjs="cdn",
    default_width="100%",
    default_height="100%",
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

with open("grafico2d.html", "w", encoding="utf-8") as f:
    f.write(pagina)
# theme/plotly_theme.py
import plotly.io as pio
import plotly.express as px

def apply_plotly_theme():
    # base template
    pio.templates["ba_theme"] = pio.templates["plotly_white"]

    # customize
    pio.templates["ba_theme"].layout.update(
        font=dict(family="Segoe UI, Arial, sans-serif", size=14, color="#2E2E2E"),
        title=dict(font=dict(size=20, color="#003366", family="Segoe UI, Arial"), x=0.02),
        colorway=["#1F77B4","#FF7F0E","#2CA02C","#9467BD","#D62728","#17BECF","#8C564B"],
        paper_bgcolor="#FAFAFA",
        plot_bgcolor="#FAFAFA",
        xaxis=dict(showgrid=True, gridcolor="#E6E6E6", zeroline=False),
        yaxis=dict(showgrid=True, gridcolor="#E6E6E6", zeroline=False),
        margin=dict(l=40, r=40, t=60, b=40),
        legend=dict(
            bgcolor="rgba(255,255,255,0.9)",
            bordercolor="#DDDDDD",
            borderwidth=1,
            font=dict(size=12),
        ),
        hoverlabel=dict(bgcolor="white", font_size=12, font_family="Segoe UI"),
    )

    # make default everywhere
    pio.templates.default = "ba_theme"
    px.defaults.template = "ba_theme"
    px.defaults.height = 450
    px.defaults.color_continuous_scale = "Blues"


#!/usr/bin/env python3
"""
Build the Student Retention dashboard as an interactive HTML.
"""
from ctypes.wintypes import SHORT

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from pathlib import Path

# COLOR MAP FOR PLOT (2,1)
REASON_COLORS = {
    "Admin Withdraw":    "#ADD8E6",  # light blue
    "EXP CAN'...":     "#F77E24",  # orange
    "Elementar...":   "#014B86",  # dark blue
    "Enroll in Ot...":   "#62C0DD",  # sky blue
    "HOME SCHOOLING":    "#BACB1F",  # yellow-green
    "OTHER (U...":   "#8DC63F",  # light green
    "Transferre...":    "#522D80",  # purple
}

# COLOR MAP FOR PLOT (2,2)
REASON_COLORS2 = {
    "ADMIN WITHDRAW":    "#ADD8E6",  # light blue
    "EXP CAN'T RET":     "#F77E24",  # orange
    "Elementary With":   "#014B86",  # dark blue
    "Enroll in Other":   "#62C0DD",  # sky blue
    "HOME SCHOOLING":    "#f7ec24",  # yellow-green
    "OTHER (UNKNOWN)":   "#8DC63F",  # light green
    "Transferred to":    "#522D80",  # purple
}


def main():
    # 1. Locate project root and data folder
    project_root = Path(__file__).resolve().parents[1]
    data_dir = project_root / "data"
    output_dir = project_root / "outputs"
    output_dir.mkdir(parents=True, exist_ok=True)

    # 2. Load data files
    kpi = pd.read_json(data_dir / "retention_kpi.json", typ="series")
    comp_df = pd.read_csv(data_dir / "student_composition.csv")
    school_df = pd.read_csv(data_dir / "retention_by_school.csv")
    district_df = pd.read_csv(data_dir / "district_withdrawals.csv")
    pie_df = pd.read_csv(data_dir / "pie_data.csv")

    # 3. Create a 2x2 subplot figure
    fig = make_subplots(
        rows=2, cols=2,
        specs=[[{"type":"xy"},{"type":"xy"}],
               [{"type":"domain"},{"type":"xy"}]],
        column_widths=[0.4,0.6],        # first column 40%, second 60%
        row_heights=[0.33, 0.67],       # first row 33%, second 67%
        subplot_titles=(
            "<b>STUDENT RETENTION KPI</b>",
            "<b>RETENTION BY SCHOOL</b>",
            "<b>TOP WITHDRAWAL REASONS</b>",
            "<b>DISTRICT WITHDRAWALS</b>",


        )
    )
# Repositioning Annotations
    # Annotation 0 → “STUDENT RETENTION KPI” (row 1, col 1)
    fig.layout.annotations[0].update(
        x=0.02,  # 2% from left paper edge
        y=0.98,  # 98% up the paper
        xanchor="left",
        yanchor="top",
        font=dict(size=16)
    )

    # Annotation 1 → “RETENTION BY SCHOOL” (row 1, col 2)
    fig.layout.annotations[1].update(
        x=0.42 + 0.02,  # start of col 2 + small inset
        y=0.98,
        xanchor="left",
        yanchor="top",
        font=dict(size=16)
    )

    # Annotation 2 → “DISTRICT WITHDRAWALS” (row 2, col 1)
    fig.layout.annotations[2].update(
        x=0.02,
        y=0.55,  # mid‐cell for the second row
        xanchor="left",
        yanchor="top",
        font=dict(size=16)
    )

    # Annotation 3 → “TOP WITHDRAWAL REASONS” (row 2, col 2)
    fig.layout.annotations[3].update(
        x=0.42 + 0.02,
        y=0.55,
        xanchor="left",
        yanchor="top",
        font=dict(size=16)
    )

    fig.update_layout(
        width=1500, # These lines make the entire figure a landscape style view
        height=800,
        margin=dict(l=20, r=20, t=100, b=20),
        plot_bgcolor="white",
    )


    # ───────────────────────────────────────────────────────────────────────────
    # DRAW BOXES AROUND EACH SUBPLOT USING RECTANGLE SHAPES
    # ───────────────────────────────────────────────────────────────────────────
    '''
    cw, ch = 0.4, 0.33  # column width of col1, row height of row1
    boxes = [
        # (x0, x1, y0, y1)
        (0.0, cw, 1 - ch, 1.0),  # row1, col1
        (cw, 1.0, 1 - ch, 1.0),  # row1, col2
        (0.0, cw, 0.0, 1 - ch),  # row2, col1
        (cw, 1.0, 0.0, 1 - ch),  # row2, col2
    ]

    for x0, x1, y0, y1 in boxes:
        fig.add_shape(
            type="rect",
            xref="paper", yref="paper",
            x0=x0, x1=x1, y0=y0, y1=y1,
            line=dict(color="black", width=1),
            fillcolor="rgba(0,0,0,0)"  # transparent
        )
    '''

    #4a. Top-left: KPI annotation + horizontal bar
    # - Bar chart of Returning vs New

    comp_df = comp_df.iloc[::-1]        # This reverses the order of the rows so that the graphic matches the image.
    fig.add_trace(                      # Note that [::-1] is start (not specified), stop (not specified), and step = -1 (step backwards)
        go.Bar(
            x=comp_df["Count"],
            y=comp_df["Category"],
            orientation="h",
            marker_color="#9DE2F3",
            text=[f"{c/1000:.1f}K" for c in comp_df["Count"]],
            textposition="inside",
            showlegend=False,
        ),
        row=1, col=1
    )

    # - Big KPI % annotation at top-left
    fig.add_annotation(
        text=(
            f"<b><span style='color:#9DE2F3'>{int(kpi['retention_rate'])}%</span>"
            f"<br><span style='font-size:18px; color:rgba(128, 128, 128, 0.6)'>Retention</span></b>"
        ),
        xref="x domain", yref="y domain",
        x=-0.7, y=0.5,       # position above the bar chart
        showarrow=False,
        font=dict(size=36),
        align="right"
    )

    fig.update_xaxes(
        row=1, col=1,
        domain=[0.18,0.40], # This adjusts the top-left bar graph to only go from 30% to 98% of the top-left subplot.
        tickvals=[0, 2000],
        ticktext=["0K", "2K"],
        showgrid=False,
        gridcolor="gray",
        gridwidth=1,
        griddash="dash",
        ticklabelstandoff=50, # This moves the ticklabels below the graph
    )

    fig.update_yaxes(
        row=1, col=1,
        domain=[0.8,0.88],
        tickfont=dict(color="rgba(128, 128, 128, 0.6)"), # The last number here is the opacity
        ticklabelstandoff=10,
    )

    fig.add_shape( # This code adds the gray dashed line at the 2K mark on the x-axis.
        type="line",  # Note that yref had to be y domain instead of y1 to fix this.
        xref="x1", yref="y domain",
        x0=2000, x1=2000,
        y0=-.9, y1=1.5,
        line=dict(color="rgba(128, 128, 128, 0.15)", dash="dash"),
        layer="above",
    )

    fig.add_shape(  # This code adds the gray dashed line at the 2K mark on the x-axis.
        type="line",  # Note that yref had to be y domain instead of y1 to fix this.
        xref="x1", yref="y domain",
        x0=0, x1=0,
        y0=-.9, y1=1.5,
        line=dict(color="rgba(128, 128, 128, 0.15)", dash="dash"),
        layer="above",
    )

###
# SUBPLOT (1,2) = RETENTION BY SCHOOL
###

    fig.add_trace(
        go.Bar(
            x=school_df["Campus"],
            y=school_df["Retention Rate"],
            marker_color="#3BD2E5",
            text=[f"{r}%" for r in school_df["Retention Rate"]],
            textposition="inside",
            insidetextfont=dict(color="white", size=12, family="Arial, sans-serif"),
            showlegend=False,
        ),
        row=1,col=2
    )


    fig.update_xaxes(
        row=1, col=2,
        domain=[0.45,0.98],
        tickfont=dict(size=10),
        showgrid=False,
        zeroline=False,
    )
    fig.update_yaxes(
        row=1, col=2,
        domain=[0.70, 0.9],
        range=[0,100],
        showgrid=False,
        zeroline=False,
        showticklabels=False,
    )

###
# SUBPLOT (2,1) TOP WITHDRAWAL REASONS (PIE CHART)
###

    fig.add_trace(
        go.Pie(
            labels=pie_df["Reason"],
            values=pie_df["Percentage"],
            marker_colors=[REASON_COLORS[r] for r in pie_df["Reason"]],
            textinfo="percent",
            textposition="outside",
            sort=False,
            direction="clockwise",
            insidetextorientation="radial",
            showlegend=True,
        ),
    row=2, col=1
)

    fig.update_traces(
        selector=dict(type="pie"),
        domain=dict(x=[0.02, 0.35], y=[0.15, 0.45]),
        pull=[0,0,0,0,0],
        textposition="outside",
        textfont=dict(size=14),
    )

    fig.update_layout(
        legend=dict(
            orientation="h",

            # paper coords:
            xref="paper",
            yref="paper",

            # line up left edge with pie (0.02) and bottom edge at y=0.05
            x=0.001,
            y=0.05,
            xanchor="left",
            yanchor="bottom",

            # let each entry size itself to its text
            itemsizing="constant",
            # if you still want a hard max width, itemwidth can help,
            # but often you can omit it now:
             itemwidth=30,

            # small gap between each item
            tracegroupgap=0,

            font=dict(size=9.8),
            itemclick=False,
            itemdoubleclick=False,
        )
    )

###
# SUBPLOT (2,2) DISTRICT WITHDRAWALS
###

    # First, define the calendar order of months so bars appear left-to-right
    MONTH_ORDER = [
        "August", "September", "October", "November", "December",
        "January", "February", "March", "April",
    ]

    # Pivot district_df so each Reason is its own column:
    pivot = (
        district_df
        .groupby(["Year", "Month", "Reason"], as_index=False)["Count"]
        .sum()
        .pivot(index=["Year", "Month"], columns="Reason", values="Count")
        .fillna(0)
        .reset_index()
    )

    # Create a single string index for plotting and sort it by our MONTH_ORDER
    pivot["MonthYear"] = pivot["Month"] + " " + pivot["Year"].astype(str)
    pivot = pivot.set_index("MonthYear").loc[
        [m + " 2022" for m in MONTH_ORDER[:5]] + # August-December 2022
        [m + " 2023" for m in MONTH_ORDER[5:]]   # Jan-Apr 2023
    ].reset_index()

    # Now add one go.Bar trace per Reason, stacking them:
    for Reason in [
        "ADMIN WITHDRAW",
        "Elementary With",
        "Enroll in Other",
        "EXP CAN'T RET",
        "HOME SCHOOLING",
        "OTHER (UNKNOWN)",
        "Transferred to",
    ]:
        fig.add_trace(
            go.Bar(
                x=pivot["MonthYear"],
                y=pivot[Reason],
                name=Reason,
                marker_color=REASON_COLORS2[Reason],
                marker_line_width=0,
                showlegend=False,
            ),
            row=2, col=2
        )

    # Configure the stack:
    fig.update_layout(
        barmode="stack",
        width=1500,
        height=800,
        margin=dict(l=20, r=20, t=100, b=160),

    )

    # Annotate the total on top of each bar:
    totals = pivot.drop(columns=["Year", "Month"]).set_index("MonthYear").sum(axis=1)
    for i, m in enumerate(pivot["MonthYear"]):
        fig.add_annotation(
            x=m,
            y=totals.loc[m] + 2,    # this places the annotation a little above the bar
            text=str(int(totals.loc[m])),
            showarrow=False,
            row=2, col=2,
            font=dict(size=12),
        )

    # Tidy up the axes:
    fig.update_xaxes(
        row=2, col=2,
        domain=[0.48, 0.9],  # same as your other domain settings
        tickmode="array",
        tickvals=pivot["MonthYear"],
        ticktext=["August", "Septem..", "October", "Novem..", "Decem..", "January", "February", "March", "April"],
        tickangle=-90,
        tickfont=dict(size=10),
        showgrid=False,
        zeroline=False,
    )
    fig.update_yaxes(
        row=2, col=2,
        domain=[0.15, 0.5],
        range=[0, totals.max() * 1.1],
        showgrid=True,
        gridcolor="lightgray",
        griddash="dot",
        zeroline=False,
        title_text="",  # or “Count” if you like
        tickvals = [0, 50, 100],
        ticklabelstandoff = 30
    )

    legend_y = 0.3
    legend_x_start = 0.91
    legend_gap = 0.055

    reasons = list(REASON_COLORS2.items())

    for i, (label, color) in enumerate(reasons):
        fig.add_annotation(
            x=legend_x_start,
            y=legend_y - i * legend_gap, # invisible data point
            xanchor="left",
            xref="paper",
            yref="paper",
            showarrow=False,
            font=dict(size=11, color="black"),
            text=f"<span style='font-size: 20px; color:{color}'>{u'\u25CF'}</span> {label}",
            yshift = 60
            )

    # floating "2022" under Aug-Dec
    fig.add_annotation(
        text="2022",
        x=0.597, y=0.02,  # pick the midpoint category
        xref="paper",
        yref="paper",
        showarrow=False,
        font=dict(size=11)
    )

    # floating "2023" under Jan-Apr
    fig.add_annotation(
        text="2023",
        x=0.818, y=0.02,
        xref="paper",
        yref="paper",
        showarrow=False,
        font=dict(size=11)
    )

    # Draw a vertical dashed line after April at the bottom of the bar plot
    fig.add_shape(
        type="line",
        xref="paper",
        yref="paper",
        x0=0.9,
        x1=0.9,
        y0=0.02,
        y1=.4748,
        line=dict(
            color="rgba(128,128,128,0.3)",
            dash="dot",
            width=1
        ),
        layer="above"
    )

    # draw a vertical dashed line at the split point (e.g. just before "January 2023"):
    fig.add_shape(
        type="line",
        xref="paper",
        yref="paper",
        x0=0.713,
        x1=0.713,
        y0=0.02,
        y1=.15,
        line=dict(
            color="rgba(128,128,128,0.3)",
            dash="dot",
            width=1
        ),
        layer="above"
    )

    # Draw a vertical dashed line before August at the bottom of the bar plot
    fig.add_shape(
        type="line",
        xref="paper",
        yref="paper",
        x0=0.48,
        x1=0.48,
        y0=0.02,
        y1=.15,
        line=dict(
            color="rgba(128,128,128,0.3)",
            dash="dot",
            width=1
        ),
        layer="above"
    )

    # Draw a horizontal dashed line next to the zero on the bar plot
    fig.add_shape(
        type="line",
        xref="paper",
        yref="paper",
        x0=0.46,
        x1=0.9,
        y0=0.15,
        y1=.15,
        line=dict(
            color="rgba(128,128,128,0.3)",
            dash="dot",
            width=1
        ),
        layer="above"
    )

    # Draw a horizontal dashed line next to the 50 on the y-axis
    fig.add_shape(
        type="line",
        xref="paper",
        yref="paper",
        x0=0.46,
        x1=0.479,
        y0=0.3124,
        y1=.3124,
        line=dict(
            color="rgba(128,128,128,0.3)",
            dash="dot",
            width=1
        ),
        layer="above"
    )

    # Draw a horizontal dashed line next to the 100 on the y-axis
    fig.add_shape(
        type="line",
        xref="paper",
        yref="paper",
        x0=0.46,
        x1=0.479,
        y0=0.4748,
        y1=.4748,
        line=dict(
            color="rgba(128,128,128,0.3)",
            dash="dot",
            width=1
        ),
        layer="above"
    )

    fig.write_html(output_dir / "retention_dashboard_preview.html")

if __name__ =="__main__":
    main()
from src import constants
import plotly.graph_objects as go

def plot_field(fig: go.Figure):
    fig.add_shape(
        type="rect",
        x0=constants.END_ZONE_WIDTH,
        y0=0,
        x1=constants.FIELD_LENGTH - constants.END_ZONE_WIDTH,
        y1=constants.FIELD_WIDTH,
        line=dict(
            width=0,
        ),
        fillcolor=constants.FIELD_COLOR,
    )

def plot_left_end_zone(fig: go.Figure):
    fig.add_shape(
        type="rect",
        x0=0,
        y0=0,
        x1=constants.END_ZONE_WIDTH,
        y1=constants.FIELD_WIDTH,
        line=dict(
            width=0,
        ),
        fillcolor=constants.END_ZONE_COLOR,
    )

def plot_right_end_zone(fig: go.Figure):
    fig.add_shape(
        type="rect",
        x0=constants.FIELD_LENGTH - constants.END_ZONE_WIDTH,
        y0=0,
        x1=constants.FIELD_LENGTH,
        y1=constants.FIELD_WIDTH,
        line=dict(
            width=0,
        ),
        fillcolor=constants.END_ZONE_COLOR,
    )

def plot_yard_lines(fig: go.Figure):
    for x in range(
        int(constants.END_ZONE_WIDTH),
        int(constants.FIELD_LENGTH - constants.END_ZONE_WIDTH + constants.YARD_LINE_STEP),
        int(constants.YARD_LINE_STEP),
    ):
        fig.add_shape(
            type="line",
            x0=x,
            y0=0,
            x1=x,
            y1=constants.FIELD_WIDTH,
            line=dict(
                color=constants.YARD_LINE_COLOR,
                width=constants.YARD_LINE_WIDTH,
            ),
        )


def plot_hash_marks(fig: go.Figure):
    for x in range(
        int(constants.END_ZONE_WIDTH),
        int(constants.FIELD_LENGTH - constants.END_ZONE_WIDTH),
        int(constants.YARD),
    ):
        fig.add_shape(
            type="line",
            x0=x,
            y0=0,
            x1=x,
            y1=constants.HASH_MARK_LENGTH,
            line=dict(
                color=constants.YARD_LINE_COLOR,
                width=constants.YARD_LINE_WIDTH,
            ),
        )

        fig.add_shape(
            type="line",
            x0=x,
            y0=constants.FIELD_WIDTH - constants.HASH_MARK_LENGTH,
            x1=x,
            y1=constants.FIELD_WIDTH,
            line=dict(
                color=constants.YARD_LINE_COLOR,
                width=constants.YARD_LINE_WIDTH,
            )
        )

        fig.add_shape(
            type="line",
            x0=x,
            y0=constants.FIELD_WIDTH / 2 - constants.HASH_MARK_SEPARATION / 2 - constants.HASH_MARK_LENGTH,
            x1=x,
            y1=constants.FIELD_WIDTH / 2 - constants.HASH_MARK_SEPARATION / 2,
            line=dict(
                color=constants.YARD_LINE_COLOR,
                width=constants.YARD_LINE_WIDTH,
            ),
        )

        fig.add_shape(
            type="line",
            x0=x,
            y0=constants.FIELD_WIDTH / 2 + constants.HASH_MARK_SEPARATION / 2,
            x1=x,
            y1=constants.FIELD_WIDTH / 2 + constants.HASH_MARK_SEPARATION / 2 + constants.HASH_MARK_LENGTH,
            line=dict(
                color=constants.YARD_LINE_COLOR,
                width=constants.YARD_LINE_WIDTH,
            ),
        )

def plot_conversion_lines(fig: go.Figure):
    fig.add_shape(
        type="line",
        x0=constants.END_ZONE_WIDTH + constants.CONVERSION_LINE_DIST,
        y0=constants.FIELD_WIDTH / 2 - constants.CONVERSION_LINE_LENGTH / 2,
        x1=constants.END_ZONE_WIDTH + constants.CONVERSION_LINE_DIST,
        y1=constants.FIELD_WIDTH / 2 + constants.CONVERSION_LINE_LENGTH / 2,
        line=dict(
            color=constants.YARD_LINE_COLOR,
            width=constants.YARD_LINE_WIDTH,
        ),
    )

    fig.add_shape(
        type="line",
        x0=constants.FIELD_LENGTH - constants.END_ZONE_WIDTH - constants.CONVERSION_LINE_DIST,
        y0=constants.FIELD_WIDTH / 2 - constants.CONVERSION_LINE_LENGTH / 2,
        x1=constants.FIELD_LENGTH - constants.END_ZONE_WIDTH - constants.CONVERSION_LINE_DIST,
        y1=constants.FIELD_WIDTH / 2 + constants.CONVERSION_LINE_LENGTH / 2,
        line=dict(
            color=constants.YARD_LINE_COLOR,
            width=constants.YARD_LINE_WIDTH,
        ),
    )


def plot_annotations(fig: go.Figure):
    [fig.add_annotation(
        dict(
            x=x,
            y=constants.ANNOTATION_SEPARATION,
            text=string,
            showarrow=False,
            font=dict(
                size=constants.ANNOTATION_SIZE,
                color=constants.ANNOTATION_COLOR,
                family="Clarendon FS",
            ),
            xanchor="center",
            yanchor="middle",
        )
    )
        for x, string in zip(
            range(
                int(constants.END_ZONE_WIDTH + 2 * constants.YARD_LINE_STEP),
                int(constants.FIELD_LENGTH - constants.END_ZONE_WIDTH),
                int(2 * constants.YARD_LINE_STEP),
            ),
            [
                "1 0",
                "2 0",
                "3 0",
                "4 0",
                "5 0",
                "4 0",
                "3 0",
                "2 0",
                "1 0",
            ]
        )
    ]

    [fig.add_annotation(
        dict(
            x=x,
            y=constants.FIELD_WIDTH - constants.ANNOTATION_SEPARATION,
            text=string,
            showarrow=False,
            font=dict(
                size=constants.ANNOTATION_SIZE,
                color=constants.ANNOTATION_COLOR,
                family="Clarendon FS",
            ),
            xanchor="center",
            yanchor="middle",
            textangle=180,
        )
    )
        for x, string in zip(
            range(
                int(constants.END_ZONE_WIDTH + 2 * constants.YARD_LINE_STEP),
                int(constants.FIELD_LENGTH - constants.END_ZONE_WIDTH),
                int(2 * constants.YARD_LINE_STEP),
            ),
            [
                "1 0",
                "2 0",
                "3 0",
                "4 0",
                "5 0",
                "4 0",
                "3 0",
                "2 0",
                "1 0"
            ]
        )
    ]

def plot_border(fig: go.Figure):
    fig.add_shape(
        type="rect",
        x0=0,
        y0=0,
        x1=constants.FIELD_LENGTH,
        y1=constants.FIELD_WIDTH,
        line=dict(
            color=constants.BORDER_LINE_COLOR,
            width=constants.BORDER_LINE_WIDTH,
        ),
    )
import argparse
from pathlib import Path
import plotly.graph_objects as go
from src import constants
from src.utils import plotting


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a field image and save it."
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        default="/nfl/src/resources",
        help="Directory to save the image"
    )
    parser.add_argument(
        "--file_name",
        type=str,
        default="field.png",
        help="Filename for the field image"
    )
    return parser.parse_args()


def ensure_directory_exists(path: Path):
    path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

def draw(path: Path):
    ensure_directory_exists(
        path=path
    )

    fig = go.Figure()
    plotting.plot_field(fig)
    plotting.plot_left_end_zone(fig)
    plotting.plot_right_end_zone(fig)
    plotting.plot_yard_lines(fig)
    plotting.plot_hash_marks(fig)
    plotting.plot_conversion_lines(fig)
    plotting.plot_annotations(fig)
    plotting.plot_border(fig)

    fig.update_xaxes(    # cSpell: disable-line
        range=[
            -constants.FIELD_MARGIN,
            constants.FIELD_LENGTH + constants.FIELD_MARGIN
        ],
        visible=True,
    )
    fig.update_yaxes(    # cSpell: disable-line
        range=[
            -constants.FIELD_MARGIN,
            constants.FIELD_WIDTH + constants.FIELD_MARGIN
        ],
        visible=True,
    )

    fig.update_layout(
        width=constants.SCALE*(constants.FIELD_LENGTH + 2 * constants.FIELD_MARGIN),
        height=constants.SCALE*(constants.FIELD_WIDTH + 2 * constants.FIELD_MARGIN),
    )

    fig.write_image(
        file=path,
        scale=constants.SCALE,
    )

def main():
    args: argparse.Namespace = parse_arguments()
    path: Path = Path(args.output_dir) / args.file_name
    if path.exists():
        print(f"File {path} exists.")
    else:
        print(f"File {path} does not exist. Drawing...")
        draw(path=path)

if __name__ == "__main__":
    main()

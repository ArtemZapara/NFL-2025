import argparse
from pathlib import Path
import plotly.graph_objects as go


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
    fig.write_image(
        file=path
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

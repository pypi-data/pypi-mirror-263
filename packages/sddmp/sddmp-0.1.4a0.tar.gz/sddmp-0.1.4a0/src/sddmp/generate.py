"""
This file is used to create static html files for displaying in GitHub Pages.

Usage:
    python create_html_files.py -i data -o docs
"""

import shutil

import argparse
import logging
from pathlib import Path
import pkg_resources

from sddmp.filesystem import FileSystem
from sddmp.outputs import DirectoryPage, ReferencePage

logger = logging.getLogger(__name__)


def _parse_cli():
    parser = argparse.ArgumentParser(
        description="Create static html files for displaying in GitHub Pages."
    )
    parser.add_argument(
        "-i",
        "--input",
        type=str,
        default="data",
        help="The input directory to create html files for.",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default="docs",
        help="The output directory for the html files.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Print verbose output.",
    )
    parser.add_argument(
        "--source_prefix",
        default="",
        help="The prefix to add to the source path when loading the static files",
    )
    return parser.parse_args()


def create_index(root_directory, output_directory):
    """
    Create a simple index page for navigating around the html files.

    THIS IS NOT A FINAL IMPLEMENTATION. This is just a quick and dirty way to create an index page.
    """
    # Create a simple html file that contains links to all of the directories.
    html = "<ul>"
    for my_directory in root_directory.all_descendants:
        html += (
            f'<li><a href="{my_directory.path}/index.html">{my_directory.path}</a></li>'
        )
    html += "</ul>"

    # Create the path to the html file.
    my_path = Path(output_directory) / "index.html"

    # Write the html file.
    with open(my_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Created index file at {my_path}")


if __name__ == "__main__":
    args = _parse_cli()

    # Set up logging.
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    fs = FileSystem()
    root = fs.read_directory(args.input)

    DirectoryPage.directory_structure = fs.get_directory_structure(root)["children"]
    ReferencePage.directory_structure = fs.get_directory_structure(root)["children"]

    # Delete the output directory if it exists.
    if Path(args.output).exists():
        logger.info("Deleting existing output directory at %s", args.output)
        for path in Path(args.output).glob("*"):
            if path.is_file():
                path.unlink()
            else:
                shutil.rmtree(path)
        Path(args.output).mkdir(exist_ok=True, parents=True)

    # Move the static directory to the output directory.
    source_dir = pkg_resources.resource_filename(__name__, "src/sddmp/outputs/static/")
    logger.info("Copying static files from %s to %s/static", source_dir, args.output)
    shutil.copytree(source_dir, Path(args.output) / "static")

    # Create a reference page
    reference = ReferencePage(args.input, args.output)
    reference.generate()

    # Start with the root and iterate recursively through all directories.
    # For each directory, create an html file.
    for directory in root.all_descendants:
        page = DirectoryPage(directory, args.output)
        page.generate()

    # Create an index to help navigate around
    create_index(root, args.output)

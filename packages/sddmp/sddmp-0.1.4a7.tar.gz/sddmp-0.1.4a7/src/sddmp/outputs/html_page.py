"""
This file contains the HTMLPage class, which is used as a base class for generating HTML pages.

This class is not intended to be used directly, but rather to be subclassed by classes that
generate specific types of HTML pages.
"""

from abc import ABC, abstractmethod
from pathlib import Path
import pkg_resources

from jinja2 import Environment, FileSystemLoader


class HTMLPage(ABC):
    """
    This is an abstract base class containing common methods and properties for generating HTML
    pages.
    """

    # Class Variable for storing the directory structure
    directory_structure = None

    def __init__(self, template_name: str, output_directory: Path):
        self.output_directory = output_directory
        template_dir = pkg_resources.resource_filename(__name__, "/templates")
        self.jinja_env = Environment(
            loader=FileSystemLoader(template_dir), autoescape=True
        )
        self.template = self.jinja_env.get_template(template_name)

    @abstractmethod
    def get_relative_path_to_root(self) -> str:
        """
        Returns the relative path from the this page's path to the root directory.

        Used to locate static files in the output directory.

        Returns:
            str: The relative path from this page's path to the root directory.
        """

    @abstractmethod
    def get_path(self) -> Path:
        """
        Returns the path to the HTML file.

        Returns:
            str: The path to the HTML file.
        """

    @abstractmethod
    def get_depth(self) -> int:
        """
        Returns the depth of the page in the directory structure.

        TODO: I honestly can't remember why we have both this and relative path to root
        """

    def generate(self, **kwargs) -> None:
        """
        Generate an HTML page.
        """
        html = self.template.render(
            directory_structure=self.directory_structure,
            relative_path_to_root=self.get_relative_path_to_root(),
            depth=self.get_depth(),
            **kwargs
        )

        # Create the directory for the html file if it does not exist.
        Path(self.get_path()).parent.mkdir(parents=True, exist_ok=True)

        # Write the html file.
        with open(self.get_path(), "w", encoding="utf-8") as f:
            f.write(html)

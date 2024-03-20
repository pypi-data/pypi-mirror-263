from pathlib import Path
import click
from .consultant import (
    export_consultant,
    get_consultants,
    add_consultant,
    check_consultant,
)
from .extract import get_dcs
from .init_src import copy_file, create_folder

OUTPUT_PATH = "outputs"
ASSET_PATH = "assets"


@click.group()
def main():
    pass


@main.command()
def init():
    folder_list = [
        "assets/Certifications",
        "assets/Icons",
        "assets/Logos",
        "assets/Profils",
        "templates",
        "config",
        "consultants",
    ]
    for folder in folder_list:
        create_folder(f"{folder}/")
    code_path = Path(__file__).parent
    copy_file(code_path / "assets/Logos", "assets/Logos", "logo_datalyo.png")  # noqa
    copy_file(code_path / "assets/Logos", "assets/Logos", "logo.png")  # noqa
    copy_file(code_path / "assets/Icons", "assets/Icons", "icon_chat.png")  # noqa
    copy_file(code_path / "assets/Icons", "assets/Icons", "icon_diploma.png")  # noqa
    copy_file(code_path / "assets/Icons", "assets/Icons", "icon_person.png")  # noqa
    copy_file(code_path / "assets/Icons", "assets/Icons", "icon_skill.png")  # noqa
    copy_file(code_path / "assets/Icons", "assets/Icons", "icon_star.png")  # noqa
    copy_file(
        code_path / "assets/Certifications",
        "assets/Certifications",
        "cert_psm.svg",  # noqa
    )
    copy_file(
        code_path / "assets/Certifications",
        "assets/Certifications",
        "cert_tableau.jpg",  # noqa
    )
    copy_file(
        code_path / "assets/Certifications",
        "assets/Certifications",
        "cert_talend.png",  # noqa
    )
    copy_file(code_path / "assets", "assets", "print.css")
    copy_file(code_path / "assets", "assets", "style.css")
    copy_file(code_path / "templates", "templates", "index.html")  # noqa
    copy_file(code_path / "config", "config", "anonyme.json")  # noqa
    print("fichiers prêt")


@main.group()
def consultant():
    pass


@consultant.command()
@click.argument("consultant")
def export(consultant):
    consultants_path = "consultants"
    dcs = get_dcs(consultants_path, consultant)
    export_consultant(dcs, OUTPUT_PATH, ASSET_PATH)


@consultant.command()
def list():
    get_consultants()


@consultant.command()
@click.argument("consultant")
def new(consultant):
    add_consultant(consultant)


@consultant.command()
@click.argument("consultant")
def check(consultant):
    check_consultant(consultant)


if __name__ == "__main__":
    main()

from pathlib import Path
import click
from .consultant import (
    export_consultant,
    get_consultants,
    add_consultant,
    check_consultant,
)
from .init_src import copy_file, create_folder


@click.group()
def main():
    pass


@main.command()
def init():
    folder_list = [
        "assets",
        "templates",
        "config",
        "consultants",
    ]
    for folder in folder_list:
        create_folder(f"{folder}/")
    code_path = Path(__file__).parent
    copy_file(code_path / "assets", "assets", "logo_datalyo.png")  # noqa
    copy_file(code_path / "assets", "assets", "logo.png")  # noqa
    copy_file(code_path / "assets", "assets", "icon_chat.png")  # noqa
    copy_file(code_path / "assets", "assets", "icon_diploma.png")  # noqa
    copy_file(code_path / "assets", "assets", "icon_person.png")  # noqa
    copy_file(code_path / "assets", "assets", "icon_skill.png")  # noqa
    copy_file(code_path / "assets", "assets", "icon_star.png")  # noqa
    copy_file(
        code_path / "assets",
        "assets",
        "cert_psm.svg",  # noqa
    )
    copy_file(
        code_path / "assets",
        "assets",
        "cert_tableau.png",  # noqa
    )
    copy_file(
        code_path / "assets",
        "assets",
        "cert_talend.png",  # noqa
    )

    copy_file(
        code_path / "assets",
        "assets",
        "EOR.png",  # noqa
    )

    copy_file(code_path / "assets", "assets", "style.css")
    copy_file(code_path / "templates", "templates", "index.html")  # noqa
    copy_file(code_path / "config", "config", "anonyme.json")  # noqa
    print("fichiers prêts")


@main.group()
def consultant():
    pass


@consultant.command()
@click.argument("consultant")
def export(consultant):
    if consultant == "all":
        consultant_list = get_consultants()
        for consul in consultant_list:
            export_consultant(consul)
    else:
        export_consultant(consultant)


@consultant.command()
def list():
    for consultant in get_consultants():
        print(consultant)


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

"""Create printable sheets based on a script json file."""
import argparse
import json
from pathlib import Path
import re
import sys

from rich import print
from rich.live import Live

from ..helpers.printable import Printable
from ..helpers.progress_group import setup_progress_group


def _parse_args():
    parser = argparse.ArgumentParser(
        prog="botc_tokens group",
        description='Create printable sheets based on a script json file.'
    )
    parser.add_argument('script', type=str,
                        help='the json file or directory containing the script info.')
    token_dir_default = 'tokens'
    parser.add_argument('--token-dir', type=str, default=token_dir_default,
                        help="Name of the directory in which to find the token images. Ignored if script is a "
                             f"directory. (Default: {token_dir_default})")
    output_dir_default = 'printables'
    parser.add_argument('-o', '--output-dir', type=str, default=output_dir_default,
                        help=f"Name of the directory in which to output the sheets. (Default: {output_dir_default})")
    parser.add_argument('--fixed-role-size', type=int, default=None,
                        help="The radius (in pixels) to allocate per role tokens. "
                             "(Default: The first token's largest dimension)")
    parser.add_argument('--fixed-reminder-size', type=int, default=None,
                        help="The radius (in pixels) to allocate per reminder tokens. "
                             "(Default: The first token's largest dimension)")
    padding_default = 0
    parser.add_argument('--padding', type=int, default=padding_default,
                        help=f"The padding (in pixels) between tokens. (Default: {padding_default})")
    paper_width_default = 2402
    parser.add_argument('--paper-width', type=int, default=paper_width_default,
                        help="The width (in pixels) of the paper to use for the tokens. "
                             f"(Default: {paper_width_default})")
    paper_height_default = 3152
    parser.add_argument('--paper-height', type=int, default=paper_height_default,
                        help="The height (in pixels) of the paper to use for the tokens. "
                             f"(Default: {paper_height_default})")
    args = parser.parse_args(sys.argv[2:])
    return args


def run():
    """Create printable sheets based on a script json file."""
    args = _parse_args()
    # Ensure the script file/directory exists
    script_path = Path(args.script)
    if not script_path.exists():
        print(f"[red]Error:[/] Unable to load script {args.script}")
        return 1

    # Read the script json file
    print(f"[green]Reading {args.script}...[/]")
    script = []
    if script_path.is_dir():
        script = [file.stem for file in script_path.rglob("*.png") if "Reminder" not in file.name]
        args.token_dir = str(script_path)
    else:
        with open(args.script, "r") as f:
            script = json.load(f)

    # Find all the token images
    token_files = Path(args.token_dir).rglob("*.png")
    role_images = []
    reminder_images = []
    print("[green]Finding Token Images...[/]")
    for img_file in token_files:
        if "Reminder" in img_file.name:
            reminder_images.append(img_file)
        else:
            role_images.append(img_file)

    if not role_images and not reminder_images:
        print("[yellow]Warning:[/] No token images found.")

    # Create the printable sheets
    print(f"[green]Creating sheets in {args.output_dir}...[/]", end="")
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    progress_group, overall_progress, step_progress = setup_progress_group()

    with Live(progress_group):
        overall_progress.add_task("Creating Sheets", total=None)
        step_task = step_progress.add_task("Adding roles")
        role_page = Printable(
            output_dir,
            basename="roles",
            page_width=args.paper_width,
            page_height=args.paper_height,
            padding=args.padding,
            diameter=args.fixed_role_size
        )
        reminder_page = Printable(
            output_dir,
            basename="reminders",
            page_width=args.paper_width,
            page_height=args.paper_height,
            padding=args.padding,
            diameter=args.fixed_reminder_size
        )
        for role in script:
            if isinstance(role, dict):
                continue  # Skip metadata
            role_name = role.lower().strip()
            step_progress.update(step_task, description=f"Adding {role_name.title()}")
            # See if we have tokens for this role
            role_file = next((t for t in role_images if role_name == t.stem.lower().replace("'", "")), None)
            reminder_regex = re.compile(f"{role_name}-reminder.*")
            reminder_files = (t for t in reminder_images if reminder_regex.match(t.stem.lower().replace("'", "")))
            if not role_file:
                print(f"[yellow]Warning:[/] No token found for {role_name}")
                continue
            role_page.add_token(role_file)
            for reminder in reminder_files:
                reminder_page.add_token(reminder)

        # Save the last pages
        step_progress.update(step_task, description="Saving pages")
        role_page.write()
        reminder_page.write()

        # Clean up
        role_page.close()
        reminder_page.close()

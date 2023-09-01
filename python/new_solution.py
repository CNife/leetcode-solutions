import re
from argparse import ArgumentParser
from pathlib import Path


def main(name: str, url: str, solution_dir: Path) -> None:
    num = int(re.findall(r"^\d+", name)[0])
    url_name = re.findall(r"problems/([^/]+)", url)[0]
    solution_path = solution_dir / f"{num}_{url_name.replace('-', '_')}.py"
    solution_path.write_text(f'"""\n{name}\n{url}\n"""\n', encoding="UTF-8")


def parse_args():
    parser = ArgumentParser(description="Create new solution")
    parser.add_argument("name", help="name of solution")
    parser.add_argument("url", help="url of solution")
    parser.add_argument("--dir", "-d", help="solution dir", type=Path, default=Path(__file__).parent / "src" / "code")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    main(args.name, args.url, args.dir)

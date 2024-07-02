import json
from pathlib import Path

import pytest


def get_files_to_check() -> list[Path]:
    root = Path(__file__).parent.parent
    files = []
    for f in root.glob("snippets/*.json"):
        files.append(f)

    return files


@pytest.fixture(scope="session")
def package_json() -> Path:
    return Path(__file__).parent.parent / "package.json"


def test_package_json_valid(package_json: Path) -> None:
    with package_json.open() as f:
        json.loads(f.read())


@pytest.mark.parametrize(
    "snippet_file",
    get_files_to_check(),
)
def test_snippets_is_valid_json(snippet_file: Path) -> None:
    with snippet_file.open() as f:
        json.loads(f.read())


def test_all_snippets_referenced(package_json: Path) -> None:
    all_paths = set(get_files_to_check())

    with package_json.open() as f:
        content = json.loads(f.read())
        snippets = content["contributes"]["snippets"]

        root = Path(__file__).parent.parent
        for snip in snippets:
            path: Path = root / snip["path"]
            # Assert the file actually exists
            assert path.is_file()
            all_paths.remove(path)

    if len(all_paths):
        assert False, f"Following files not in package.json: {all_paths}"

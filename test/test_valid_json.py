import json
from pathlib import Path

import pytest


def get_files_to_check() -> list[Path]:
    root = Path(__file__).parent.parent
    files = [root / "package.json"]
    for f in root.glob("snippets/*.json"):
        files.append(f)

    return files


@pytest.mark.parametrize(
    "snippet_file",
    get_files_to_check(),
)
def test_snippets_is_valid_json(snippet_file: Path) -> None:
    with snippet_file.open() as f:
        json.loads(f.read())

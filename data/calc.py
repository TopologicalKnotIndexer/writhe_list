"""Regenerate writhe records from the committed composite PD-code baseline."""

from ast import literal_eval
from pathlib import Path


HERE = Path(__file__).resolve().parent
INPUT_FILE = HERE / "com_pd_code_list.txt"
OUTPUT_FILE = HERE / "writhe_list.txt"


def parse_pd_record(line: str) -> tuple[str, list[list[int]]]:
    stripped = line.strip()
    if not (stripped.startswith("[") and stripped.endswith("]")):
        raise ValueError(f"malformed record: {line!r}")
    knot_name, raw_pd = stripped[1:-1].split("|", 1)
    value = literal_eval(raw_pd)
    if not isinstance(value, list):
        raise ValueError(f"PD code for {knot_name} is not a list")
    return knot_name, value


def generate_writhe_records(knot_factory=None) -> str:
    if knot_factory is None:
        from sage.all import Knot

        knot_factory = Knot
    output: list[str] = []
    for line in INPUT_FILE.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        knot_name, pd_code = parse_pd_record(line)
        writhe = knot_factory(pd_code).writhe()
        output.append(f"[{writhe}|{pd_code}|{knot_name}]")
    return "\n".join(output) + "\n"


if __name__ == "__main__":
    OUTPUT_FILE.write_text(generate_writhe_records(), encoding="utf-8")

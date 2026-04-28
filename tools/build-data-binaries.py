#!/usr/bin/env python3
"""Build little-endian Float64 binary tables from the CSV data files."""

from __future__ import annotations

import csv
import struct
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLICES = 600
TABLES = (
    ("data_dcc_notcm.csv", "data_dcc_notcm.f64", 2784),
    ("data_dcc_tcm.csv", "data_dcc_tcm.f64", 2784),
    ("data_tcm.csv", "data_tcm.f64", 144),
)


def build_table(csv_name: str, binary_name: str, expected_lines: int) -> None:
    source = ROOT / csv_name
    target = ROOT / binary_name
    pack_line = struct.Struct("<" + ("d" * SLICES)).pack
    line_count = 0

    with source.open(newline="") as csv_file, target.open("wb") as binary_file:
        reader = csv.reader(csv_file)
        for line_count, row in enumerate(reader, start=1):
            if len(row) < SLICES:
                raise ValueError(
                    f"{csv_name} line {line_count} has {len(row)} values; expected {SLICES}."
                )
            binary_file.write(pack_line(*(float(value) for value in row[:SLICES])))

    if line_count != expected_lines:
        target.unlink(missing_ok=True)
        raise ValueError(f"{csv_name} has {line_count} lines; expected {expected_lines}.")

    print(f"Wrote {target.name}")


def main() -> None:
    for csv_name, binary_name, expected_lines in TABLES:
        build_table(csv_name, binary_name, expected_lines)


if __name__ == "__main__":
    main()

#! /usr/bin/env python3

import argparse

from typing import Any

BOOL_KWARGS: dict[str, Any]

try:
    BOOL_KWARGS = {"type": bool, "action": argparse.BooleanOptionalAction}
except (ImportError, AttributeError):
    BOOL_KWARGS = {"action": "store_true"}


def _parse_cmd_line() -> dict[str, str | bool]:
    """
    Helper for parsing CLI call and displaying help message
    """
    parser = argparse.ArgumentParser(description="Upload corpus to LCP")
    # parser.add_argument("corpus", type=str, help="Input file or folder path")
    parser.add_argument(
        "-c",
        "--corpus",
        type=str,
        required=True,
        help="Corpus path (either a directory or a zip/7z/tar/tar.gz/tar.xz archive)",
    )
    parser.add_argument(
        "-k",
        "--api-key",
        type=str,
        required=True,
        help="API key",
    )
    parser.add_argument(
        "-s",
        "--secret",
        type=str,
        required=True,
        help="API key secret",
    )
    parser.add_argument(
        "-p",
        "--project",
        type=str,
        required=False,
        help="Project the corpus will be uploaded into",
    )
    parser.add_argument(
        "-j",
        "--json",
        type=str,
        required=False,
        help="JSON template filepath or raw JSON string. If not provided, the first JSON file found in the corpus data will be used.",
    )
    parser.add_argument(
        "-l",
        "--live",
        required=False,
        default=False,
        help="Use live system? If false, use test system.",
        **BOOL_KWARGS
    )
    parser.add_argument(
        "-v",
        "--vian",
        required=False,
        default=False,
        help="Upload to VIAN instead of LCP?",
        **BOOL_KWARGS
    )
    kwargs = vars(parser.parse_args())
    kwargs["template"] = kwargs.pop("json", False)
    return kwargs

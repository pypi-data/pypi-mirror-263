import argparse


def _parse_cmd_line():
    """
    Helper for parsing CLI call and displaying help message
    """
    parser = argparse.ArgumentParser(
        description="Convert input file (arg1) into output file (arg2)"
    )
    parser.add_argument(
        "-i", "--input", type=str, required=True, help="Input file path"
    )
    parser.add_argument("-o", "--output", type=str, help="Output file path")
    parser.add_argument(
        "-m",
        "--mode",
        type=str,
        nargs="?",
        choices=["normal", "upload"],
        default="normal",
        help="LCP upload ('upload') or not ('normal', default)")
    parser.add_argument(
        "-e", "--extension", type=str, help="Output format when output is a directory"
    )
    parser.add_argument(
        "-f", "--filter", required=False, type=str, help="Path to a Python filter file"
    )
    parser.add_argument(
        "-l", "--lua-filter", required=False, type=str, help="Path to a Lua filter file"
    )
    parser.add_argument(
        "-c",
        "--combine",
        required=False,
        type=bool,
        default=False,
        help="Combine into single file?",
        # action=argparse.BooleanOptionalAction,
    )
    kwargs = vars(parser.parse_args())
    kwargs["content"] = kwargs.pop("input")
    return kwargs

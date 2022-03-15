import argparse

FIELDS = ["date", "campaign", "clicks"]


def supported_fields(field):
    if field not in FIELDS:
        raise argparse.ArgumentTypeError(f"Error: Not supported field '{field}'")
    return field


parser = argparse.ArgumentParser(description="Parse CSV data")
parser.add_argument(
    "--fields", default=None, type=supported_fields, nargs="+", help="Fields to parse"
)

args = parser.parse_args()

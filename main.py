import logging

from fetcher.cli import args
from fetcher.helpers import FILE_URL, fetch_csv, parse_csv

logger = logging.Logger(__name__)


def main():
    try:
        csv_data = fetch_csv(FILE_URL)
    except Exception as exception:
        logger.error("Failed while fetching data due to %s", exception)
        return
    try:
        json_data = parse_csv(csv_data, args.fields)
    except Exception as exception:
        logger.error("Failed while parsing the data due to %s", exception)
        return

    logger.info("Data collected and parsed")
    print(json_data)


if __name__ == "__main__":
    main()

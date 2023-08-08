#!/usr/bin/env python3
import logging
import logging.config

import yaml


def configure_logging() -> None:
    with open("logging.yaml", "r") as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)


def main() -> int:
    configure_logging()

    try:
        1 / 0
    except Exception as e:
        logging.error("Hello info!", exc_info=e, extra={"test": "value"})

    return 0


if __name__ == "__main__":
    exit(main())

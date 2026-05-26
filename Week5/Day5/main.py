import logging 

from cli import build_parser
from logging_config import setup_logging

def main():
    setup_logging()

    parser = build_parser()
    args = parser.parse_args()

    try:
        args.func(args)
    except ValueError as error:
        logging.warning(str(error))
        print("Ошибка:", error)

if __name__ == "__main__":
    main()
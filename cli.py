from dotenv import load_dotenv
import argparse
import logging
from db.init import init_from_json

load_dotenv()
logging.basicConfig(level=logging.DEBUG)

parser = argparse.ArgumentParser(
    prog="Warframe-Market-Recorder", 
    description="""
        A tool to record the price of every items in warframe market.
    """
)
subparsers = parser.add_subparsers(title="subcommands", dest="subparser_name", required=True)

# db subcommand
parser_db = subparsers.add_parser("db", help="database maniplation, including initialization")
subparsers_db = parser_db.add_subparsers(title="subcommands", dest="subparser_db_name", required=True)
# db-init subcommand
parser_db_init = subparsers_db.add_parser("init", help="initialize the database")
parser_db_init.add_argument("data", metavar="JSON_DATA_PATH", help="path to the warframe-items' All.json")


if __name__ == "__main__":
    args = parser.parse_args()
    print(args)

    if args.subparser_name == "db":
        if args.subparser_db_name == "init":
            init_from_json(args.data)
        else:
            pass
    else:
        pass

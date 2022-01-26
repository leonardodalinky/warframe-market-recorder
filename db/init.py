import json

import migrate.versioning.api as mapi
from sqlalchemy import MetaData
from sqlalchemy.orm import Session
from tqdm import tqdm
import logging

from . import *
from .models import Item


def init_from_json(json_path: str):
    logging.info("Initiating database from json data.")
    logging.debug("Loading json data.")
    with open(json_path, "r", encoding="utf8") as fp:
        data = json.load(fp)
    logging.debug("Reseting the database.")
    rebuild_database()
    logging.debug("Adding items.")
    with Session(engine) as sess:
        sess: Session
        for item_json in tqdm(data):
            item = Item()
            item.load_json_dict(item_json)
            sess.add(item)
        sess.commit()


def rebuild_database():
    metadata = MetaData()
    metadata.reflect(engine)
    metadata.drop_all(engine)
    mapi.version_control(os.getenv("DB_URL"), MIGRATE_REPO, version=0)
    mapi.upgrade(os.getenv("DB_URL"), MIGRATE_REPO, version=REPO_VERSION)

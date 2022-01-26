from sqlalchemy import *
from migrate import *

meta = MetaData()
item_table = Table("items", meta,
    Column("id", Integer, primary_key=True),
    Column("category", Integer),
    Column("tradable", Boolean),
    Column("type", VARCHAR(128)),
    Column("uniqueName", VARCHAR(128), unique=True, nullable=False),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    item_table.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    item_table.drop()

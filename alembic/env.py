from alembic import context

from sqlalchemy import pool

from sqlalchemy.ext.asyncio import async_engine_from_config 

from sqlalchemy.engine import Connection   

from src.config import settings
from src.database import Base

import src.models.feeds
import src.models.noticias
import src.models.envio

import asyncio

from logging.config import fileConfig

config = context.config 


if config.config_file_name is not None:
    fileConfig(config.config_file_name)
    
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

target_metadata = Base.metadata

def run_migrations_offline(config):
    context.configure(config.get_main_option(url="sqlalchemy.url", target_metadata=target_metadata))

    with context.begin_transaction():
        context.run_migrations()

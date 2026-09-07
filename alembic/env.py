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


__version__ = '0.1.0'

from mpt.model import Analysis, Config
from mpt import database as db

db.persist()
analysis = Analysis()
# config = Config()

from sqlalchemy import create_engine
from src.loaders.load_env import DATABASE_URL

engine = create_engine(DATABASE_URL)
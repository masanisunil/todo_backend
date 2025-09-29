import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "vercel-secret")

    # ✅ Correct SQLAlchemy URL (removed supa=... part)
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg2://postgres.nrzuezbqjswglqyjlkbc:6fpet6vS5arlNQZy@aws-1-us-east-1.pooler.supabase.com:6543/postgres?sslmode=require"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

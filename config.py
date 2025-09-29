import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "vercel-secret")

    
    # ✅ FIX: use postgresql:// instead of postgres://
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "Database_URL",
        "postgresql://postgres.rgasykfchkmuxacuopso:aPRzlGNG2kk19RmH@aws-1-us-east-1.pooler.supabase.com:6543/postgres?sslmode=require")
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

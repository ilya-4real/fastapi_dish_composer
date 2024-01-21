from dotenv import load_dotenv
import os


load_dotenv()

LOGGING_LEVEL = "INFO"
MONGO_USER = os.environ.get("MONGO_USER")
MONGO_PASSWORD = os.environ.get("MONGO_PASSWORD")
MONGO_HOST = os.environ.get("MONGO_HOST")
MONGO_PORT = os.environ.get("MONGO_PORT")

JWT_SECRET = str(os.environ.get("JWT_SECRET"))
JWT_ALGORITHM = str(os.environ.get("JWT_ALGORITHM"))

MONGO_URI = f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}"

from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    FLASK_DEBUG = os.getenv("FLASK_DEBUG")
    FLASK_APP = os.getenv("FLASK_APP")
    FLASK_RUN_PORT = os.environ.get("FLASK_RUN_PORT")
    QDRANT_KEY = os.getenv("QDRANT_KEY")
    OPENAI_KEY = os.getenv("OPENAI_KEY")
    CLUSTER_URL = os.getenv("CLUSTER_URL")
    REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

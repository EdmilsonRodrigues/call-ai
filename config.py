from dotenv import load_dotenv
import os


if os.path.exists(".env"):
    load_dotenv(".env")


VERSION = "0.0.1"

BASE_API_URL = os.getenv("BASE_API_URL", "")


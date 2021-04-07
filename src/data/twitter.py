import tweepy

import osfrom dotenv import load_dotenv

load_dotenv()

GCP_PROJECT_ID = os.getenv('')
SERVICE_ACCOUNT_FILE = os.getenv('SERVICE_ACCOUNT_FILE')
STORAGE_BUCKET_NAME = os.getenv('STORAGE_BUCKET_NAME')
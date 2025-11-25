import os, sys

# adjust this path to point to the folder that contains app.py
HERE = os.path.dirname(__file__)
APP_FOLDER = os.path.join(HERE, "Personel-Diary-With-Sentiment-Analysis-main", "Personel-Diary-With-Sentiment-Analysis-main")
sys.path.insert(0, APP_FOLDER)

# import the Flask app object from app.py
from app import app  # assumes your Flask instance is named `app`

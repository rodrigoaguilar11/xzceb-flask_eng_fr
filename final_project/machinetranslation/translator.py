import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv
import sys

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

#instance of the IBM Watson Language translator
auth = IAMAuthenticator(apikey)
lt = LanguageTranslatorV3(version="2018-05-01", authenticator=auth)
lt.set_service_url(url)

def english_to_french(english_text):
    #write the code here
    translate = lt.translate(text=english_text, model_id="en-fr").get_result()
    french_text = translate ["translations"][0]["translation"]
    return french_text

def french_to_english(french_text):
    #write the code here
    translate = lt.translate(text=french_text, model_id="fr-en").get_result()
    english_text = translate ["translations"][0]["translation"]
    return english_text

print("English to French:")
print(english_to_french("Thanks"))

print("French to English:")
print(french_to_english("Merci"))

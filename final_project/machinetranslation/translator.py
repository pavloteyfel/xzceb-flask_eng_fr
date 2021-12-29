"""IMB Watson based module for english to frensh and frensh to english translations"""
import os

from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3, ApiException
from dotenv import load_dotenv


load_dotenv()

apikey = os.environ["apikey"]
url = os.environ["url"]

authenticator = IAMAuthenticator(apikey)

language_translator = LanguageTranslatorV3(
    version="2018-05-01", authenticator=authenticator
)

language_translator.set_service_url(url)


def translation_model(text, model):
    """General function for translating any text based on IBM watson models"""
    try:
        response = language_translator.translate(text=text, model_id=model).get_result()
    except ApiException as error:
        return f"Error occured during calling the API: {error}"
    return response.get("translations")[0].get("translation")


def english_to_french(text):
    """
    Parameters:
        text (str): english text

    Returns:
        french translation
    """
    return translation_model(text, "en-fr")


def french_to_english(text):
    """
    Parameters:
        text (str): french text

    Returns:
        english translation
    """
    return translation_model(text, "fr-en")

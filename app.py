import requests
from googletrans import Translator, exceptions

def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    params = {"type": "single"}  # Demander une blague courte

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Vérifie si l'appel API a réussi

        data = response.json()
        translator = Translator()

        if data.get("type") == "single":
            joke = data.get("joke")
            # Traduire la blague en français
            joke_fr = translator.translate(joke, src="en", dest="fr").text
            print("Blague : ", joke_fr)
        else:
            setup = data.get("setup")
            delivery = data.get("delivery")
            # Traduire les deux parties en français
            setup_fr = translator.translate(setup, src="en", dest="fr").text
            delivery_fr = translator.translate(delivery, src="en", dest="fr").text
            print("Blague (intro) : ", setup_fr)
            print("Blague (fin) : ", delivery_fr)

    except requests.exceptions.RequestException as e:
        print("Erreur lors de la récupération de la blague :", e)
    except exceptions.TranslatorError as e:
        print("Erreur de traduction :", e)

if __name__ == "__main__":
    get_joke()

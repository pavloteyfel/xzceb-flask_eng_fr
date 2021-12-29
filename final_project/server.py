from machinetranslation import translator
from flask import Flask, render_template, request

app = Flask("Web Translator")
ERROR_MSG = "Please, write at least one character long text."


@app.route("/englishToFrench")
def english_to_french():
    text_to_translate = request.args.get("textToTranslate")
    if not text_to_translate:
        return ERROR_MSG
    return translator.english_to_french(text_to_translate)


@app.route("/frenchToEnglish")
def french_to_english():
    text_to_translate = request.args.get("textToTranslate")
    if not text_to_translate:
        return ERROR_MSG
    return translator.french_to_english(text_to_translate)


@app.route("/")
def renderIndexPage():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

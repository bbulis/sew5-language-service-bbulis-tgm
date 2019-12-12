import web
import pycld2 as cld2
import json

# Zuweisung der Endpunkte zu einer bestimmten Klasse
urls = (
    '/detect', 'detect'
)
app = web.application(urls, globals())


class detect:
    def GET(self):
        """
        Wenn ein GET Request durchgeführt wird so holt sich die Methode alle Daten aus der der Anfrage und gibt diese an die Erkennungsmethode  weiter
        :return:
        """
        data = web.input('text')
        print(data)
        text = str(data['text'])
        print(text)
        web.header('Content-Type', 'application/json')
        return self.get_translation(text)

    def get_translation(self, text):
        """
        Methode erkennt um welche Sprache es sich handelt und gibt dies zurück als JSON Objekt
        :param text:
        :return:
        """
        isReliable, textBytesFound, details = cld2.detect(text)

        response = json.dumps(
            {"reliable": isReliable, "language": details[0][0], "short": details[0][1], "prob": details[0][2]})
        return response


if __name__ == "__main__":
    app.run()

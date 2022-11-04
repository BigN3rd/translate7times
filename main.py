#pip install libretranslatepy
from libretranslatepy import LibreTranslateAPI

def mumbo() :
    spanish = lt.translate(str(originaltext), "en", "es")
    french = lt.translate(str(spanish), "es", "fr")
    russian = lt.translate(str(french), "fr", "ru")
    german = lt.translate(str(russian), "ru", "de")
    italian = lt.translate(str(german), "de", "it")
    chinese = lt.translate(str(italian), "it", "zh")
    japanese = lt.translate(str(chinese), "zh", "ja")
    english = lt.translate(str(japanese), "ja", "en")
    print(english)

lt = LibreTranslateAPI("https://translate.argosopentech.com/")
originaltext = input("What would you like to be translated 7 times: ")
mumbo()

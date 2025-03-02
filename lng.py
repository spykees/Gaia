import json
import os
from dotenv import load_dotenv

class Lng:
    def __init__(self, default_lang='en'):
        load_dotenv()
        self.translations = {}
        self.default_lang = os.getenv('LANGUAGE', default_lang)
        self.load_translations()

    def load_translations(self):
        for filename in os.listdir('./lng'):
            if filename.endswith('.json'):
                lang = filename[:-5]
                with open(os.path.join('./lng', filename), 'r', encoding='utf-8') as f:
                    self.translations[lang] = json.load(f)

    def translate(self, key, lang=None, **kwargs):
        lang = lang or self.default_lang
        translation = self.translations.get(lang, {}).get(key, key)
        return translation.format(**kwargs)

lng = Lng()
translate = lng.translate

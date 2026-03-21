import json
import os


class I18n:
    _instance = None
    _path: str | None = None
    _lang: str | None = None
    _back_lang: str = "en"
    _translation: dict | None = None
    _back_translation: dict | None = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def set_path(cls, lang_path: str):
        cls._path = lang_path

    @classmethod
    def set_lang(cls, lang: str, back_lang: str = _back_lang):
        cls._lang = lang
        cls._back_lang = back_lang
        if cls._path is not None:
            path = os.path.join(cls._path, f"{lang}.json")
            back_path = os.path.join(cls._path, f"{back_lang}.json")
            if os.path.exists(path):
                with open(path, "r", encoding="utf-8") as f:
                    trans = json.load(f)
                cls._translation = trans
            if os.path.exists(back_path):
                with open(back_path, "r", encoding="utf-8") as f:
                    trans = json.load(f)
                cls._back_translation = trans

    @classmethod
    def t(cls, key: str) -> str:
        if cls._translation is None:
            if cls._back_translation is None:
                return ""
            return cls._back_translation.get(key, "")
        return cls._translation.get(key, cls._back_translation.get(key, ""))

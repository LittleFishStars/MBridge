import gettext
from functools import lru_cache

from tool.config import Config


@lru_cache(maxsize=7)
def get_i18n(language=Config().get("language"), domain='text'):
    localedir = 'locale'
    trans = gettext.translation(
        domain=domain,
        localedir=localedir,
        languages=[language],
        fallback=True
    )
    return trans.gettext

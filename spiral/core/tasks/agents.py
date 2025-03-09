from tokeo.ext.appshare import app  # noqa: F401
from spiral.core import tasks


def count_words_timer(url=''):
    app.log.info(f'Timer start with url: {url}')
    tasks.actors.count_words.send(url)

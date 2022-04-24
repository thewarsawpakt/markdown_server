from bottle import route, run, Response, error, HTTPError
from markdown2 import Markdown
import os

HOST = "127.0.0.1"
PORT = 8000
PAGE_DIR = os.path.join(os.path.realpath(__file__[0:-7]), "pages")
MARKDOWN_EXTENSIONS = ["fenced-code-blocks"]

markdown = Markdown(extras=MARKDOWN_EXTENSIONS)


def render_page(name):
    try:
        with open(os.path.join(PAGE_DIR, name), "r") as html:
            rendered = markdown.convert(html.read())
            return Response(rendered)
    except FileNotFoundError:
        raise HTTPError(status=404)


@route('/page/<name>')
def page(name):
    return render_page(name)


@error(404)
def error_404(err):
    return "Sorry, page not found."


if __name__ == "__main__":
    run(host=HOST, port=PORT)

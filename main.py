from bottle import route, run, template, Response, error, HTTPError
from markdown2 import Markdown

PAGE_DIR = "./pages/"
MARKDOWN_EXTENSIONS = ["fenced-code-blocks"]

markdown = Markdown(extras=MARKDOWN_EXTENSIONS)

def render_page(name):
    try:
        with open(PAGE_DIR+name, "r") as html:
            rendered = markdown.convert(html.read())
            return Response(rendered)
    except FileNotFoundError:
        raise HTTPError(status=404)

error(404)
def error_404(error):
    return "Page not found, sorry.", error

@route('/page/<name>')
def page(name):
    return render_page(name)

run(host="0.0.0.0", port=8080)

from flask import Flask, Markup, render_template_string
from flask_flatpages import FlatPages, pygmented_markdown

app = Flask(__name__)
blogs = FlatPages(app)

def prerender_jinja(text):
    return pygmented_markdown(render_template_string(Markup(text)))

app.config['FLATPAGES_ROOT'] = 'blog'
app.config['FLATPAGES_EXTENSION'] = '.md'
app.config['FLATPAGES_HTML_RENDERER'] = prerender_jinja

app.config['FREEZER_DESTINATION'] = 'gh-pages'
app.config['FREEZER_DESTINATION_IGNORE'] = [
    '.git*', 'CNAME', '.gitignore', 'readme.md', 'requirement.txt'
]
app.config['FREEZER_RELATIVE_URLS'] = True

from views import *

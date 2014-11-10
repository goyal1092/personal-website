from flask import Flask, render_template

app = Flask(__name__)

app.config['FREEZER_DESTINATION'] = 'gh-pages'
app.config['FREEZER_DESTINATION_IGNORE'] = [
    '.git*', 'CNAME', '.gitignore', 'readme.md', 'requirement.txt'
]
app.config['FREEZER_RELATIVE_URLS'] = True

from views import *

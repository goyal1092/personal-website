from flask import render_template
from app import app
from app import blogs

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

def page_list(pages, limit=None):
    p_list = (p for p in pages if 'published' in p.meta)
    p_list = sorted(p_list, reverse=True, key=lambda p: p.meta['published'])
    return p_list[:limit]

@app.route('/blog.html')
def blog_index():
    blog_list = page_list(blogs)
    return render_template('blog-index.html', blog_list=blog_list)

@app.route('/blog/<path:path>.html')
def blog_detail(path):
    blog = blogs.get_or_404(path)
    return render_template('blog-detail.html', blog=blog)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/404.html')
def static_404():
    return render_template('404.html')

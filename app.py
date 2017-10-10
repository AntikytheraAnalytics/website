import os
import markdown
from flask import render_template, send_from_directory, request, Markup, Flask
import re
app = Flask(__name__)

LINK_REGEX = re.compile("!\[(.+)\]\((.+)\)")

def get_content(article, path):
    md = markdown.Markdown(extensions = ['markdown.extensions.meta', 'markdown.extensions.fenced_code'])

    with open(path, 'r') as f: 
        data = f.read()
        if os.path.isdir("templates/articles/%s"%(article)):
            def replace_link(match):
                alt_text = match.group(1)
                link = match.group(2)
                return '![%s](%s/%s)'%(alt_text, article, link)
            data = LINK_REGEX.sub(replace_link, data)

        return md.convert(data)

def get_meta(path):
    md = markdown.Markdown(extensions = ['markdown.extensions.meta'])
    with open(path, 'r') as f: 
        md.convert(f.read())
    return md.Meta

def get_articles():
    files = os.listdir('templates/articles')
    articles = []
    paths = []
    for fname in files:
        if os.path.isdir('templates/articles/%s'%(fname)) and os.path.exists('templates/articles/%s/index.md'%(fname)):
            articles.append(fname)
            paths.append("templates/articles/%s/index.md"%(fname))
        elif fname[-3:] == '.md': 
            articles.append(fname)
            paths.append("templates/articles/%s"%(fname))

    return {article: path for article, path in zip(articles, paths)}           

    meta = map(lambda f: get_meta(f), paths)
    return {fname: meta for fname, meta in zip(articles, meta)}

def get_contents():
    return {article: get_meta(path) for article, path in get_articles().iteritems()}

def get_article(article):
    articles = get_articles()
    if article in articles:
        path = articles[article]
        meta = get_meta(path)
        if not 'title' in meta: meta['title'] = [article.replace('-', ' ').title(),]

        content = get_content(article, path)

        return meta, content
    else:
        False


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/insights")
def insights():
    return render_template('insights.html', articles=get_contents())

@app.route("/insights/<article>")
def article(article):
    result = get_article(article)
    if result:
        meta, content = result
        return render_template('article.html', content=content, meta=meta)
    else:
        return render_template('insights.html', articles = get_contents())

@app.route("/insights/<article>/<path:path>")
def article_resource(article, path):
    print(article, path)
    if article in get_articles():
        return send_from_directory("templates/articles/%s"%(article), path)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0')


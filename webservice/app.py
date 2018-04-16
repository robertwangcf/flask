from flask import Flask, render_template
from data import list_articles

app = Flask(__name__)
list_articles = list_articles()

@app.route('/')
def index():
	return render_template('home.html')


@app.route('/about')
def about():
	return render_template('about.html')


@app.route('/article/<string:id>')
def article(id):
	return render_template('article.html', id=id)

	
@app.route('/articles')
def articles():
	return render_template('articles.html', articles = list_articles)


if __name__ == '__main__':
	app.run(debug=True)
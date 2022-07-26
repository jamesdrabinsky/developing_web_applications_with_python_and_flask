from flask import Flask, escape, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html', company_name='TestDriven.io')


@app.route('/stocks/', methods=['GET'])
def stocks():
    return '<h2>Stock List...</h2>'


@app.route('/hello/<message>', methods=['GET'])
def hello_message(message):
    return f'<h1>Welcome {escape(message)}!</h1>'


@app.route('/blog_posts/<int:post_id>', methods=['GET'])
def display_blog_posts(post_id):
    return f'<h1>Blog Post #{post_id}...</h1>'



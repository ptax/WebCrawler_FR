from flask import Flask
from flask import render_template
from lib.factory.Storage import Storage as DocFactory
from lib.config.Yaml import Yaml as Config


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('admin/index.html')

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/home/')
@app.route('/home/<name>')
def home(name=None):
    return render_template('home.html', name=name)

@app.route('/gmaps/')
def gmaps_list():
    config = Config('./config/config.yml')

    factory = DocFactory(config.get('mongodb'))
    gmaps = factory.gmaps_collection()
    objects = gmaps.find({})
    count = objects.count()
    return render_template('gmaps/list.html', objects=objects, count=count)

@app.route('/wiki/')
def wiki_list():
    config = Config('./config/config.yml')

    factory = DocFactory(config.get('mongodb'))
    wiki = factory.wiki_collection()
    objects = wiki.find({'name': { '$exists': True, '$not': {'$size': 0} }})
    count = objects.count()
    return render_template('wiki/list.html', objects=objects, count=count)
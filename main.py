from flask import Flask, render_template
from app.main.views import main_blueprint
from app.posts.views import post_blueprint
from app.api.views import api_blueprint
from app.bookmarks.views import bookmarks_blueprint


app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.register_blueprint(main_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(api_blueprint)
app.register_blueprint(bookmarks_blueprint)
app.static_folder = app.root_path + '/static/'


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 400


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run()

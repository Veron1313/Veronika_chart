from flask import Flask, jsonify, request

from chart import spotify, db


def create_app():
    app = Flask(__name__)

    @app.route('/refresh', methods=['POST'])
    def refresh():
        musicians = spotify.parse()
        db.store(musicians)
        # TODO: check
        return jsonify(musicians), 200

    @app.route('/search', methods=['GET'])
    def search():
        author = request.args.get('author')
        musicians = db.search(author)
        # TODO: check
        return jsonify(musicians), 200

    return app

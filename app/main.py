from flask import Flask

from app.routes.map_route import map_blueprint

app = Flask(__name__)
app.register_blueprint(map_blueprint, url_prefix="/")



if __name__ == "__main__":
    app.run(port=5050)
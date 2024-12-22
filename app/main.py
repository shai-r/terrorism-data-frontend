from flask import Flask, jsonify
import requests
import webbrowser
import os

from app.services.map_service import map_of_average_casualties

app = Flask(__name__)


@app.route('/get_mean_casualties', methods=['GET'])
def get_mean_casualties():
    url = "http://127.0.0.1:5001/api/statistics/mean_casualties_by_area"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data)
        map_of_average_casualties(data)
        webbrowser.open(f'file://{os.path.join(os.getcwd(),  'htmls', 'average_by_region.html')}')
        return jsonify(data)
    else:
        return jsonify({"error": "Failed to retrieve data"}), 500


if __name__ == '__main__':
    app.run(port=5000)
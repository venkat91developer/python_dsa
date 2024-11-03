import networkx as nx
import os
import time
import osmnx as ox
from flask import Flask, request, jsonify
from flask_cors import CORS 
from app.MusicPlayer import MusicPlayer

app = Flask(__name__)
CORS(app, resources={"": {"origins": "*"}})
music_player = MusicPlayer()

@app.route('/createMusic', methods=['POST'])
def createMusic():
    music_data = request.form
    title = music_data.get('music_name')
    artist = music_data.get('music_artist')
    image = request.files.get('music_image')
    file = request.files.get('music_file')
    if not image or not file:
        return jsonify({'status': 'error', 'message': 'No files provided'}), 400
    upload_dir = 'uploads'
    os.makedirs(upload_dir, exist_ok=True)
    image_path = os.path.join(upload_dir, image.filename)
    file_path = os.path.join(upload_dir, file.filename)
    image.save(image_path)
    file.save(file_path)
    result = music_player.createMusic(title=title, artist=artist, image_path=image_path, file_path=file_path)
    return result


@app.route('/getMusic', methods=['GET'])
def getMusic():
    return music_player.getMusic()

if __name__ == '__main__':
    app.run(debug=True, port=5001)

import networkx as nx
import osmnx as ox
from flask import Flask, request, jsonify
from flask_cors import CORS  # Import Flask-CORS
from app.MusicPlayer import MusicPlayer  # Import from the app package


app = Flask(__name__)
CORS(app, resources={"": {"origins": "*"}})  # Enable CORS for the specific route

# Initialize MusicPlayer instance
music_player = MusicPlayer()

@app.route('/getMusic', methods=['GET'])
def getMusic():
    # Call the getMusic method of MusicPlayer instance
    return music_player.getMusic()

if __name__ == '__main__':
    app.run(debug=True, port=5001)

from flask import jsonify

class MusicPlayer:
    def __init__(self):
        pass
    
    def getMusic(self):

        return jsonify({'status': 'Inside function'}), 200 
from flask import jsonify
from app.Database.db import Database
import time
class Music:
    def __init__(self,music_id=None):
        self.music_id = music_id
class MusicPlayer:
    def __init__(self):
        self.db_conn = Database("dsa")
        if not self.db_conn.table_exists("music"):
            self.db_conn.create_table("music")
    def createMusic(self):
        pass
    def getMusic(self):

        return jsonify({'status': 'Inside function'}), 200 
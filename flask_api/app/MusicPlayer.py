from flask import jsonify
from app.Database.db import Database
import time
import random
import requests
import os
class Music:
    def __init__(self,music_id=None):
        self.music_id = music_id
class MusicPlayer:
    def __init__(self):
        self.db_conn = Database("dsa")
        if not self.db_conn.table_exists("music"):
            self.db_conn.create_table("music")
    def createMusic(self, title, artist, image_path, file_path):
        timestamp = int(time.time())
        self.db_conn.insert("music",
        {
        "id": timestamp, 
        "timestamp": timestamp, 
        "title": title,
        "artist":artist,
        "image_path":image_path,
        "file_path":file_path
        }
        )
        return {
            'status': 'success',
            'message': 'Music created successfully',
            'title': title,
            'artist': artist,
            'image_path': image_path,
            'file_path': file_path
        }
    def getMusic(self, play_audio=True):
        if play_audio:
            all_music = self.db_conn.fetch_all("music")
            return jsonify({
                "status":"success",
                "data":all_music
            }), 200
        else:
            return jsonify({'status': 'Inside function'}), 200
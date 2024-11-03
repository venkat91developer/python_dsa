import json
import os

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.file_path = os.path.join(os.path.dirname(__file__), f"{db_name}.json")
        self._load_database()
     
    def table_exists(self, table_name):
        return table_name in self.data

    def _load_database(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                self.data = json.load(file)
        else:
            self.data = {}
            self._save_database()

    def _save_database(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.data, file, indent=4)

    def create_table(self, table_name):
        if table_name not in self.data:
            self.data[table_name] = []
            self._save_database()
        else:
            print(f"Table '{table_name}' already exists.")

    def insert(self, table_name, record):
        if table_name in self.data:
            self.data[table_name].append(record)
            self._save_database()
        else:
            print(f"Table '{table_name}' does not exist.")

    def fetch_all(self, table_name):
        if table_name in self.data:
            return self.data[table_name]
        else:
            print(f"Table '{table_name}' does not exist.")
            return []

    def fetch_by_condition(self, table_name, condition):
        if table_name in self.data:
            return [record for record in self.data[table_name] if condition(record)]
        else:
            print(f"Table '{table_name}' does not exist.")
            return []

    def update(self, table_name, condition, update_data):
        if table_name in self.data:
            updated = False
            for record in self.data[table_name]:
                if condition(record):
                    record.update(update_data)
                    updated = True
            if updated:
                self._save_database()
            else:
                print("No records matched the condition.")
        else:
            print(f"Table '{table_name}' does not exist.")

    def delete(self, table_name, condition):
        if table_name in self.data:
            original_len = len(self.data[table_name])
            self.data[table_name] = [record for record in self.data[table_name] if not condition(record)]
            if len(self.data[table_name]) < original_len:
                self._save_database()
            else:
                print("No records matched the condition.")
        else:
            print(f"Table '{table_name}' does not exist.")

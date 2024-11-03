# Initialize the database
db = SimpleDatabase("my_database")

# Create a table
db.create_table("users")

# Insert records into the table
db.insert("users", {"id": 1, "name": "Alice", "age": 25})
db.insert("users", {"id": 2, "name": "Bob", "age": 30})

# Fetch all records
all_users = db.fetch_all("users")
print("All Users:", all_users)

# Fetch records with a condition
young_users = db.fetch_by_condition("users", lambda x: x['age'] < 30)
print("Young Users:", young_users)

# Update records with a condition
db.update("users", lambda x: x['id'] == 1, {"age": 26})

# Delete records with a condition
db.delete("users", lambda x: x['name'] == "Bob")

# Fetch all records after update and delete
all_users = db.fetch_all("users")
print("All Users after update and delete:", all_users)

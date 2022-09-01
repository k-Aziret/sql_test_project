# from config import *
# import mysql.connector

class Category():

	def __init__(self, cursor):
		self.cursor = cursor

	# def run_connect(self):
	# 	try:
	# 		connect = mysql.connector.connect(
	# 			host = DATABASE_HOST,
	# 			user = DATABASE_USER,
	# 			password = DATABASE_PASSWORD,
	# 			db = DATABASE_NAME,
	# 			autocommit = True
	# 		)
	# 		return connect.cursor()
	# 	except Exception as e:
	# 		print("Соеденение с базой не установлена")
	# 		exit(0)

	def create_table(self):
		# cursor = self.run_connect()
		query = """
			CREATE TABLE IF NOT EXISTS category(
			id INTEGER PRIMARY KEY AUTO_INCREMENT,
			name VARCHAR(50) NOT NULL UNIQUE
		);
		"""
		result = self.cursor.execute(query)
		# result = cursor.execute(query)
		return result

	def add_new_category(self, name):
		# cursor = self.run_connect()
		query = f"""
			INSERT INTO category(name) VALUES('{name}');
		"""
		result = self.cursor.execute(query)
		return result
	
	def delete_category(self, id):
		# cursor = self.run_connect()
		query = f"""
			DELETE FROM category WHERE id={id};
		"""
		result = self.cursor.execute(query)
		return result 
	
	def update_category(self, id, new_value):
		# cursor = self.run_connect()
		query = f"""
			UPDATE category SET name='{new_value}' WHERE id={id};
		"""
		result = self.cursor.execute(query)
		return result  

	def get_all_categories(self):
		# cursor = self.run_connect()
		query = f"""
			SELECT * FROM category;
		"""
		result = self.cursor.execute(query)
		return self.cursor.fetchall()

	def get_category_by_name(self, name):
		# cursor = self.run_connect()
		query = f"""
			SELECT * FROM category WHERE name='{name}';
		"""

		self.cursor.execute(query)
		return self.cursor.fetchone()

	def seach_movie(self, search_text):
		query = f"""
			SELECT * FROM movie WHERE name LIKE
		"""

	def _get_all_ids(self):
		query = f"""
			SELECT id FROM product; 
		"""
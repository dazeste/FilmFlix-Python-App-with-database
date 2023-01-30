from connect import *

def read():
	cursor.execute("SELECT * FROM film")
	rows = cursor.fetchall()

	# print("\n",rows)
	# print(type(rows))

	print("\nFilm List:")
	for record in rows:
		# print(type(record))
		print(record)

if __name__ == "__main__":
	read()

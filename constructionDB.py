import sqlite3
import bcrypt


connection = sqlite3.connect("user.db")

db = connection.cursor()

# db.execute("CREATE TABLE IF NOT EXISTS user (username text, password text)")


# db.execute("INSERT INTO user values('admin', ?)", (pswdHashed,))

db.execute("SELECT password from user WHERE username = 'admin'")

pwdFromDB = db.fetchall()[0][0]
print(pwdFromDB)
essaie = "admin".encode("utf-8")
print(bcrypt.checkpw(essaie, pwdFromDB))

connection.commit()
connection.close()
import sqlite3
from sqlite3.dbapi2 import connect
import datetime

def find_user_query(id, email, password):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    find_query = "SELECT * FROM users WHERE id=?"
    data_found = (cursor.execute(find_query, (id, ))).fetchone()
    if data_found:
        if email == data_found[1] and password == data_found[2]:
            string = "permitted"
        else:
            string = '*Wrong credentials*'
    else:
        string = '*No id found*'
    connection.close()
    return string

def blog_creating(id, date, content): #enters blog
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    enter_query = "INSERT INTO {} VALUES(?, ?, ?)".format(id)
    try:
        cursor.execute(enter_query, (date, content[0:30], content))
    except:
        return 
    connection.commit()
    connection.close()
    
def get_all_blogs(id):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    id_query = "SELECT * FROM {}".format(id)
    result = cursor.execute(id_query)
    entries = []
    for i in result:
        entries.append((i[0], i[1], i[2]))
    connection.close()
    return entries


def make_an_account(id, email, password):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    id_querry = "SELECT * FROM users WHERE id=?"
    result = cursor.execute(id_querry, (id, ))
    if result.fetchone():
        return "Id already exists. Use different id"

    email_querry = "SELECT * FROM users WHERE email=?"
    res = cursor.execute(email_querry, (email, ))
    if res.fetchone():
        return "Email already exists. Use different email"
    
    create_user_acc = "INSERT INTO users VALUES(?, ?, ?)"
    create_db = "CREATE TABLE {} (date text, title text, content title)".format(id)
    cursor.execute(create_user_acc, (id, email, password))
    cursor.execute(create_db)
    connection.commit()
    connection.close()
    return "done"
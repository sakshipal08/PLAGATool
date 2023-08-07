import sqlite3
importos

defcreateDabase():
    global conn, cursor
    cwd = os.getcwd()
    database_path = cwd+'\database\db.db'
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    print('Database Created')

defInsertData(name,email,password,mobile):
    cwd = os.getcwd()
    database_path = cwd+'\database\db.db'
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO `users` ("
                   "username,email,password,mobile) "
                   "VALUES(?, ?, ?, ?)",         (name,email,password,mobile))

    conn.commit()
    print('Inserted Data')

defread_cred(email,password):
    cwd = os.getcwd()
    database_path = cwd+'\database\db.db'
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute("SELECT username,email,password,mobile FROM users WHERE email ="+"'"+email+"'"+" and password ="+"'"+password+"'"+"")
    fetch = cursor.fetchone()
    print(fetch)
    return fetch

# createDabase()
import sqlite3
conn = sqlite3.connect('networkTables.db')
conn.text_factory = str
curs = conn.cursor()



#curs.execute("DELETE  FROM sessionKeyTable")
#conn.commit()

curs.execute("INSERT INTO sessionKeyTable (sessionKey, UUID) VALUES (?,?)", ("portakal", "A1DB1329",))
conn.commit()

curs.execute("SELECT *  FROM sessionKeyTable")
print curs.fetchall()
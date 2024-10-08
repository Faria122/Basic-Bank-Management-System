import mysql.connector 

mydb = mysql.connector.connect (
            host = "127.0.0.1",
            user = "root",
            password = "fahria",
            database = "bank"
)

# an object
cursor = mydb.cursor()

def db_query(str):
    cursor.execute(str)
    result = cursor.fetchall()
    return result 


def createcustomertable():
    cursor.execute ('''
             CREATE TABLE IF NOT EXISTS  customers(
                    username VARCHAR(20),
                    password VARCHAR (20),
                    name VARCHAR (20),
                    age INTEGER,
                    city VARCHAR(20),
                    balance INTEGER NOT NULL,
                    account_number INTEGER,
                    status BOOLEAN 
                    ); 
''')

mydb.commit()


if __name__ == "__main__":
    createcustomertable()
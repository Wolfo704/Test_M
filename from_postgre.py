import psycopg2
from constants import USER_PG, PASSWORD_PG, PORT_PG, HOST_PG

try:
    con = psycopg2.connect(
        dbname='test',
        user=USER_PG,
        password=PASSWORD_PG,
        host=HOST_PG,
        port=PORT_PG
    )
    print("База данных подключена")


    def load_from_db():
        print("working")
        return {}


    if __name__ == '__main__':
        load_from_db()

        with con.cursor as curs:
            curs.execute('SELECT * FROM users')
            data_base = curs.fetch()
        curs.close()
        con.close()

except:
    print('Can`t establish connection to database')

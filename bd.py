import pymysql, config

class Conexion:
    def __init__(self):
        self.conn = pymysql.connect(host=config.DB_HOST,
                                port=config.DB_PORT,
                                user=config.DB_USER,
                                password=config.DB_PASSWORD,
                                db=config.DB_NAME,
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.conn.cursor()

    def ejecutar(self, query, params=None):
        self.cursor.execute(query, params or ())
        self.conn.commit()
        return self.cursor

    def obtener(self, query, params=None):
        self.cursor.execute(query, params or ())
        return self.cursor.fetchall()

    def cerrar(self):
        self.cursor.close()
        self.conn.close()

def obtener_conexion():
    return pymysql.connect(host=config.DB_HOST,
                                port=config.DB_PORT,
                                user=config.DB_USER,
                                password=config.DB_PASSWORD,
                                db=config.DB_NAME)
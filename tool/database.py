import sqlite3

from tool.config import Config


class Database:
    def __init__(self, name: str):
        self.name = name
        self.conn = sqlite3.connect(f"{Config().get("data_path")}/{name}.db")
        self.conn.row_factory = sqlite3.Row
        self.cur = self.conn.cursor()

    def close(self):
        self.cur.close()
        self.conn.close()

    def execute(self, spl: str, params: tuple = ()):
        self.cur.execute(spl, params)

    def commit(self):
        self.conn.commit()

    def fetchall(self) -> list[dict]:
        return self.cur.fetchall()

    def fetchone(self) -> dict:
        return self.cur.fetchone()

    def fetchmany(self, size: int) -> list[dict]:
        return self.cur.fetchmany(size)

    def fetch(self, size: int = -1) -> list[dict] | None:
        if size < 1:
            return self.fetchall()
        if size == 1:
            return [self.fetchone()]
        return self.fetchmany(size)

    def rollback(self):
        self.conn.rollback()


class UserDatabase(Database):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        super().__init__("users")
        create = """
                 CREATE TABLE IF NOT EXISTS users
                 (
                     id
                     TEXT
                     PRIMARY
                     KEY
                     COMMENT
                     '节点ID',
                     name
                     TEXT
                     NOT
                     NULL
                     COMMENT
                     '名字',
                     pub_key
                     TEXT
                     NOT
                     NULL
                     COMMENT
                     '公钥',
                     fingerprint
                     TEXT
                     NOT
                     NULL
                     COMMENT
                     '验证指纹',
                 )
                 """
        self.cur.execute(create)

    def get(self, id: str) -> dict | None:
        self.cur.execute("SELECT * FROM users WHERE id = ?", (id,))
        return self.cur.fetchone()

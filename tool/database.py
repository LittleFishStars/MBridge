import sqlite3
from typing import Any

from tool.config import Config


class Database:
    def __init__(self, name: str):
        self.name = name
        self.conn = sqlite3.connect(f"{Config().get("data_path")}/{name}.db")
        self.cur = self.conn.cursor()

    def close(self):
        self.cur.close()
        self.conn.close()

    def execute(self, spl: str, params: tuple = ()):
        self.cur.execute(spl, params)

    def commit(self):
        self.conn.commit()

    def fetchall(self) -> list:
        return self.cur.fetchall()

    def fetchone(self) -> Any:
        self.cur.fetchone()

    def fetchmany(self, size: int) -> list:
        return self.cur.fetchmany(size)

    def fetch(self, size: int = -1) -> list | None:
        if size < 1:
            return self.fetchall()
        if size == 1:
            return [self.fetchone()]
        return self.fetchmany(size)

    def rollback(self):
        self.conn.rollback()


class UserDatabase(Database):
    def __init__(self):
        super().__init__("users")
        create = """
                 CREATE TABLE IF NOT EXISTS users
                 (
                     id
                     INTEGER
                     PRIMARY
                     KEY
                     AUTOINCREMENT,
                     name
                     TEXT
                     NOT
                     NULL,
                     pub_key
                     TEXT
                     UNIQUE
                     NOT
                     NULL
                 )
                 """
        self.cur.execute(create)

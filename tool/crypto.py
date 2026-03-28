import hashlib
import os.path
import time

from Crypto.PublicKey import RSA

from tool.config import Config


class Crypto:
    key_path = os.path.join(Config().get("data_path"), "crypto")
    public_key_path = os.path.join(key_path, "public_key.pem")
    private_key_path = os.path.join(key_path, "private_key.pem")

    _instance = None
    _public_key = None
    _private_key = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def get_rsa_pair(cls) -> tuple[bytes, bytes]:
        if cls._public_key is None and os.path.exists(cls.public_key_path):
            with open(cls.public_key_path, "rb") as f:
                cls._public_key = f.read()
        if cls._private_key is None and os.path.exists(cls.private_key_path):
            with open(cls.private_key_path, "rb") as f:
                cls._private_key = f.read()
        if cls._public_key is None or cls._private_key is None:
            key = RSA.generate(2048)
            cls._private_key = key.exportKey()  # 生成私钥
            cls._public_key = key.publickey().exportKey()  # 生成公钥
            if not os.path.exists(cls.key_path):
                os.makedirs(cls.key_path)
            with open(cls.public_key_path, "wb") as f:
                f.write(cls._public_key)
            with open(cls.private_key_path, "wb") as f:
                f.write(cls._private_key)
        return cls._public_key, cls._private_key

    @classmethod
    def get_public_key(cls) -> bytes:
        if cls._public_key is None:
            cls.get_rsa_pair()
        return cls._public_key

    @classmethod
    def get_private_key(cls) -> bytes:
        if cls._private_key is None:
            cls.get_rsa_pair()
        return cls._private_key

    @classmethod
    def get_id(cls) -> str:
        public_key, private_key = cls.get_rsa_pair()
        return hashlib.sha256(public_key).hexdigest()

    @classmethod
    def get_time_id(cls) -> str:
        return hashlib.sha256((cls.get_id() + str(int(time.time()))).encode()).hexdigest()

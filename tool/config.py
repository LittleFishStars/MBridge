import json
import os
from typing import Any


class Config:
    _instance = None
    _config: dict | None = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._load_config()
        return cls._instance

    @classmethod
    def _load_config(cls, config_path: str = "./config.json") -> dict[str, Any]:
        # 检查文件是否存在
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"配置文件不存在: {config_path}")

        # 读取并解析JSON
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                config = json.load(f)
            cls._config = config
            return config
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"JSON格式错误: {str(e)}", e.doc, e.pos)
        except Exception as e:
            raise Exception(f"加载配置失败: {str(e)}")

    @classmethod
    def get(cls, key: str, default: Any = None) -> Any:
        return cls._config.get(key, default)

    def __str__(self):
        return str(self._config)

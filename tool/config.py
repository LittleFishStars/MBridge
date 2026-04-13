import json
import os
from typing import Any


class Config:
    """配置管理类，采用单例模式"""
    # 单例实例
    _instance = None
    # 配置字典
    _config: dict | None = None

    def __new__(cls, *args, **kwargs):
        """创建单例实例
        
        Returns:
            Config: 配置管理实例
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._load_config()
        return cls._instance

    @classmethod
    def _load_config(cls, config_path: str = "./config.json") -> dict[str, Any]:
        """加载配置文件
        
        Args:
            config_path: 配置文件路径
            
        Returns:
            dict: 配置字典
            
        Raises:
            FileNotFoundError: 配置文件不存在
            json.JSONDecodeError: JSON格式错误
            Exception: 加载配置失败
        """
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
        """获取配置值
        
        Args:
            key: 配置键
            default: 默认值
            
        Returns:
            Any: 配置值
        """
        return cls._config.get(key, default)

    def __str__(self):
        """返回配置字符串表示
        
        Returns:
            str: 配置字符串
        """
        return str(self._config)
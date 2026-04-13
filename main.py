from loguru import logger
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.theme import Theme
from textual.widgets import Footer

from screen.control import Header
from screen.main_screen import MainScreen
from tool.config import Config
from tool.i18n import get_i18n

# 初始化国际化
_ = get_i18n()


class MBridgeApp(App):
    """MBridge应用主类"""
    # CSS文件路径
    CSS_PATH = "main.scss"
    # 应用绑定的快捷键
    BINDINGS = [
        Binding('ctrl+q', "quit", _("Quit")),
    ]

    def compose(self) -> ComposeResult:
        """组合应用界面组件"""
        yield Header()  # 顶部标题栏
        yield MainScreen()  # 主屏幕
        yield Footer(show_command_palette=False)  # 底部状态栏

    def on_mount(self) -> None:
        """应用挂载时执行的方法"""
        # 获取主题配置
        theme_config = Config().get("theme")
        # 如果是用户自定义主题
        if theme_config.get("is_user", False):
            theme_setting = theme_config.get("setting")
            # 注册自定义主题
            self.register_theme(Theme(
                name=theme_config.get("name"),
                primary=theme_setting.get("primary"),
                secondary=theme_setting.get("secondary"),
                accent=theme_setting.get("accent"),
                foreground=theme_setting.get("foreground"),
                background=theme_setting.get("background"),
                success=theme_setting.get("success"),
                warning=theme_setting.get("warning"),
                error=theme_setting.get("error"),
                surface=theme_setting.get("surface"),
                panel=theme_setting.get("panel"),
                dark=theme_setting.get("dark"),
                variables=theme_setting.get("variables"),
            ))
        # 设置应用主题
        self.theme = theme_config.get("name", "tokyo-night")


if __name__ == "__main__":
    # 配置日志格式
    logger_format = ("{time:YYYY-MM-DD HH:mm:ss} [{level: ^8}] "
                     "({file}:{line} | {thread.name}:{module}:{function}) {message}")
    # 移除默认日志
    logger.remove()
    # 添加文件日志
    logger.add(
        "log/{time:YYYY-MM-DD}.log",
        format=logger_format,
        rotation="00:00",  # 每天00:00分轮转日志
        enqueue=True,  # 异步写入
        level="TRACE",  # 日志级别
    )

    try:
        # 启动应用
        logger.info(f"Start MBridgeApp. Version {Config().get('version')})")
        app = MBridgeApp()
        app.run()
        logger.info("End MBridgeApp")
    except Exception as e:
        # 捕获并记录异常
        logger.error(f"Error: {e}")
        logger.info("ErrorEnd MBridgeApp")

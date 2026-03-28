from loguru import logger
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.theme import Theme
from textual.widgets import Footer

from screen.control import Header
from screen.main_screen import MainScreen
from tool.config import Config
from tool.i18n import get_i18n

_ = get_i18n()


class MBridgeApp(App):
    CSS_PATH = "main.scss"
    BINDINGS = [
        Binding('ctrl+q', "quit", _("Quit")),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield MainScreen()
        yield Footer(show_command_palette=False)

    def on_mount(self) -> None:
        theme_config = Config().get("theme")
        if theme_config.get("is_user", False):
            theme_setting = theme_config.get("setting")
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
        self.theme = theme_config.get("name", "tokyo-night")


if __name__ == "__main__":
    logger_format = ("{time:YYYY-MM-DD HH:mm:ss} [{level: ^8}] "
                     "({file}:{line} | {thread.name}:{module}:{function}) {message}")
    logger.remove()
    logger.add(
        "log/{time:YYYY-MM-DD}.log",
        format=logger_format,
        rotation="00:00",
        enqueue=True,
        level="TRACE",
    )

    logger.info("Starting MBridgeApp")
    app = MBridgeApp()
    app.run()
    logger.info("Ending MBridgeApp")

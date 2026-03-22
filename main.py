from textual.app import App, ComposeResult
from textual.theme import Theme
from textual.widgets import Footer

from screen.content import Content
from screen.control import Header
from tool.config import Config
from tool.i18n import I18n

I18n().set_path("./lang")
I18n().set_lang("en")


class MBridgeApp(App):
    CSS_PATH = "main.css"
    BINDINGS = [
        ('^Q', "quit", I18n().t("quit_text")),
        ('^S', "send_message", I18n().t("send_text"))
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Content()
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
    app = MBridgeApp()
    app.run()

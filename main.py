from textual.app import App, ComposeResult
from textual.theme import Theme
from textual.widget import Widget
from textual.widgets import Footer, Label

from config import Config
from i18n import I18n

I18n().set_path("./lang")
I18n().set_lang("en")


class Header(Widget):
    DEFAULT_CSS = """
        Header {
            layout: horizontal;
            position: absolute;
            align: left top;
            padding: 1 2;
            height: 3;
        }
        #title { text-style: bold; color: $text-primary; }
        #version { color: $text-secondary; }
    """

    def compose(self) -> ComposeResult:
        yield Label(I18n().t("title"), id="title")
        yield Label(" ")
        yield Label(f"v{Config().get("version")}", id="version")


class MBridgeApp(App):
    BINDINGS = [('^Q', "quit", I18n().t("quit_text"))]

    def compose(self) -> ComposeResult:
        yield Header()
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

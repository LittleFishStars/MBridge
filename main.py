from textual.app import App, ComposeResult, RenderResult
from textual.widget import Widget, Content
from textual.widgets import Footer

from config import Config


class Header(Widget):
    def render(self) -> RenderResult:
        return Content.from_markup(
            "[#84FFCC][bold]MBridge[/bold] [#84FFCC 64%]v$version[/][/]",
            version=Config().get("version")
        )


class MBridgeApp(App):
    BINDINGS = []
    CSS_PATH = "main.css"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()


if __name__ == "__main__":
    app = MBridgeApp()
    app.run()

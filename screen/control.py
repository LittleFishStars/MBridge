from datetime import datetime

from textual.app import ComposeResult, RenderResult
from textual.widget import Widget
from textual.widgets import Label
from textual.widgets._header import HeaderClockSpace

from tool.config import Config
from tool.i18n import I18n


class Header(Widget):
    DEFAULT_CSS = """
    Header {
        dock: top;
        layout: horizontal;
        padding: 1 3;
        width: 100%;
        height: 3;
    }
    #title { text-style: bold; color: $text-primary; }
    #version { color: $text-secondary; }
    HeaderClock { background: $background; }
    """

    def compose(self) -> ComposeResult:
        yield Label(I18n().t("title"), id="title")
        yield Label(" ")
        yield Label(f"v{Config().get("version")}", id="version")
        yield Clock()


class Clock(HeaderClockSpace):
    DEFAULT_CSS = """
    Clock {
        background: $background;
        content-align: center middle;
    }
    """

    def _on_mount(self, _) -> None:
        self.set_interval(1, callback=self.refresh, name="update clock")

    def render(self) -> RenderResult:
        return datetime.now().time().strftime("%X")

from datetime import datetime

from textual.app import ComposeResult, RenderResult
from textual.widget import Widget
from textual.widgets import Label
from textual.widgets._header import HeaderClockSpace

from tool.config import Config
from tool.i18n import get_i18n

_ = get_i18n()


class Header(Widget):
    DEFAULT_CSS = """
    #title { text-style: bold; color: $text-primary; }
    #version { color: $text-secondary; }
    """

    def compose(self) -> ComposeResult:
        yield Label(_("MBridge"), id="title")
        yield Label(" ")
        yield Label(f"v{Config().get("version")}", id="version")
        yield Clock()


class Clock(HeaderClockSpace):
    def _on_mount(self, _) -> None:
        self.set_interval(1, callback=self.refresh, name="update clock")

    def render(self) -> RenderResult:
        return datetime.now().time().strftime("%X")

from textual.app import ComposeResult
from textual.color import Color
from textual.widget import Widget
from textual.widgets import Label

from screen.chat_input import ChatInput
from tool.i18n import I18n


class Chat(Widget):
    DEFAULT_CSS = """
    #message { width: 100%; height: 3fr; }
    #input { height: 1fr; }
    """

    def compose(self) -> ComposeResult:
        yield Label(I18n().t("chat_title"), id="message")
        yield ChatInput("input", id="input")

    def on_mount(self) -> None:
        self.border_title = I18n().t("chat_title")

    def on_focus(self) -> None:
        self.styles.border = ("round", self.app.theme_variables.get("border"))
        self.styles.border_title_style = "bold"

    def on_blur(self) -> None:
        self.styles.border = ("round", (Color.parse(self.app.theme_variables.get("border")) +
                                        Color(0, 0, 0, 0.4)))
        self.styles.border_title_style = "none"

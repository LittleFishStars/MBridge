from textual.app import ComposeResult
from textual.color import Color
from textual.widget import Widget
from textual.widgets import Label

from screen.chat_input import ChatInput
from tool.i18n import get_i18n

_ = get_i18n()


class Chat(Widget):
    DEFAULT_CSS = """
    #message { width: 100%; height: 3fr; }
    #input { height: 1fr; }
    """

    def __init__(
            self,
            friend_name: str | None = None,
            friend_id: str | None = None
    ) -> None:
        super().__init__()
        self.friend_name = friend_name
        self.friend_id = friend_id

    def compose(self) -> ComposeResult:
        if self.friend_name is not None:
            yield Label("Chat", id="message")
            yield ChatInput("input", id="input")

    def on_mount(self) -> None:
        if self.friend_name is not None:
            self.border_title = self.friend_name

    def on_focus(self) -> None:
        self.styles.border = ("round", self.app.theme_variables.get("border"))
        self.styles.border_title_style = "bold"

    def on_blur(self) -> None:
        self.styles.border = ("round", (Color.parse(self.app.theme_variables.get("border")) +
                                        Color(0, 0, 0, 0.4)))
        self.styles.border_title_style = "none"

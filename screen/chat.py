from textual.app import ComposeResult
from textual.color import Color
from textual.widget import Widget

from screen.chat_input import ChatInput
from screen.chat_message import ChatMessage
from screen.message_list import MessageList
from tool.i18n import get_i18n

_ = get_i18n()


class Chat(Widget):
    DEFAULT_CSS = """
    MessageList { width: 100%; height: 3fr; }
    ChatInput { height: 1fr; }
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
            yield MessageList(
                ChatMessage("Hello MBridge", "00:00:00"),
                ChatMessage("Hello MBridge 1", "00:00:10", is_me=True)
            )
            yield ChatInput("input")

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

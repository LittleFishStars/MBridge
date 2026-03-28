from textual.app import ComposeResult
from textual.widget import Widget

from screen.chat_input import ChatInput
from screen.chat_message import ChatMessage, ChatMessageList
from tool.i18n import get_i18n

_ = get_i18n()


class Chat(Widget):
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
            yield ChatMessageList(
                ChatMessage("Hello MBridge", "00:00:00"),
                ChatMessage("Hello MBridge 1", "00:00:10", is_me=True)
            )
            yield ChatInput("input")

    def on_mount(self) -> None:
        if self.friend_name is not None:
            self.border_title = self.friend_name

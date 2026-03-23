from textual.app import ComposeResult
from textual.widget import Widget

from screen.chat import Chat
from screen.friend import Friend
from screen.friend_list import FriendList


class Content(Widget):
    DEFAULT_CSS = """
    Content {
        layout: grid;
        grid-size: 2 1;
        grid-columns: 1fr 3fr;
        padding: 0 2;
    }
    """
    _chat_widget: Chat | None

    def compose(self) -> ComposeResult:
        yield FriendList(
            Friend("Amy", "1"),
            Friend("Bob", "2"),
            Friend("Charlie", "3"),
        )
        self._chat_widget = Chat()
        yield self._chat_widget

    def on_friend_list_chat_changed(self, event: FriendList.ChatChanged) -> None:
        self._chat_widget.remove()
        self._chat_widget = Chat(event.name, event.id)
        self.mount(self._chat_widget)

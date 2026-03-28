from textual.app import ComposeResult
from textual.widget import Widget

from screen.chat import Chat
from screen.friend import FriendItem, FriendList


class MainScreen(Widget):
    _chat_widget: Chat | None

    def compose(self) -> ComposeResult:
        yield FriendList(
            FriendItem("Amy", "1"),
            FriendItem("Bob", "2"),
            FriendItem("Charlie", "3"),
        )
        self._chat_widget = Chat()
        yield self._chat_widget

    def on_friend_list_chat_changed(self, event: FriendList.ChatChanged) -> None:
        self._chat_widget.remove()
        self._chat_widget = Chat(event.name, event.id)
        self.mount(self._chat_widget)

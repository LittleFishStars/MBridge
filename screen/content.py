from textual.app import ComposeResult
from textual.widget import Widget

from screen.chat import Chat
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

    def compose(self) -> ComposeResult:
        yield FriendList()
        yield Chat()

from textual.binding import Binding
from textual.color import Color
from textual.message import Message
from textual.widgets import ListView

from screen.friend import Friend
from tool.i18n import get_i18n

_ = get_i18n()


class FriendList(ListView):
    BINDINGS = [
        Binding("enter", "select_cursor", _("Select")),
        Binding("up", "cursor_up", _("Cursor up")),
        Binding("down", "cursor_down", _("Cursor down")),
    ]
    DEFAULT_CSS = """
    FriendList {
        border: round $border 40%;
        padding: 0 1;
    }
    """

    class ChatChanged(Message):
        """自定义事件：更换聊天对象"""

        def __init__(self, name: str, id: str) -> None:
            super().__init__()
            self.name = name
            self.id = id

    def on_mount(self) -> None:
        self.border_title = _("FriendList")
        self.blur()

    def on_focus(self) -> None:
        self.styles.border = ("round", self.app.theme_variables.get("border"))
        self.styles.border_title_style = "bold"

    def on_blur(self) -> None:
        self.styles.border = ("round", (Color.parse(self.app.theme_variables.get("border")) +
                                        Color(0, 0, 0, 0.4)))
        self.styles.border_title_style = "none"

    def on_list_view_selected(self, event) -> None:
        friend: Friend = event.item
        self.post_message(self.ChatChanged(friend.friend_name, friend.friend_id))

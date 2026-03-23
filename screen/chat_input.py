from textual import events
from textual.binding import Binding
from textual.color import Color
from textual.message import Message
from textual.widgets import TextArea

from tool.i18n import get_i18n

_ = get_i18n()


class ChatInput(TextArea):
    BINDINGS = [
        Binding('ctrl+s', "send_message", _("Send")),
        Binding("ctrl+z", "undo", _("Undo")),
        Binding("ctrl+y", "redo", _("Redo")),
        Binding("shift+" + _("ArrowKey"), "", _("Cursor select")),
        Binding("ctrl+e", "expand", _("Expand") + "/" + _("Collapse")),
    ]
    _char_ch_en = {
        "：": ":",
        "；": ";",
        "。": ".",
        "，": ",",
        "！": "!",
    }
    _char_dch_en = {
        "（": "(",
        "【": "[",
        "“": "\"",
        "”": "\"",
        "‘": "'",
        "’": "'",
    }
    _char_den = {
        "(": "()",
        "[": "[]",
        "{": "{}",
        "'": "''",
        "\"": "\"\"",
    }
    _char_dch_den = {
        "（": "()",
        "【": "[]",
        "“": "\"\"",
        "”": "\"\"",
        "‘": "''",
        "’": "''",
    }
    _char_dch = {
        "（": "（）",
        "【": "【】",
        "“": "“”",
        "”": "“”",
        "‘": "‘’",
        "’": "‘’",
    }

    class SendMessage(Message):
        """自定义事件：发送消息"""

        def __init__(self, message: str):
            super().__init__()
            self.message = message

    def __init__(self, text: str, *, replace_double_char: bool = True, replace_chinese_char: bool = True, **kwargs):
        super().__init__(text, **kwargs)
        self.replace_double_char = replace_double_char
        self.replace_chinese_char = replace_chinese_char

    def _on_key(self, event: events.Key) -> None:
        if self.replace_double_char and self.replace_chinese_char:
            self.replace_char(event, self._char_ch_en)
            self.replace_char(event, self._char_den, offset=-1)
            self.replace_char(event, self._char_dch_den, offset=-1)
        elif self.replace_double_char:
            self.replace_char(event, self._char_den, offset=-1)
            self.replace_char(event, self._char_dch, offset=-1)
        elif self.replace_chinese_char:
            self.replace_char(event, self._char_ch_en)
            self.replace_char(event, self._char_dch_en)

    def replace_char(self, event: events.Key, char_set: dict[str, str], offset=0) -> None:
        if event.character in char_set:
            self.insert(char_set[event.character])
            if offset:
                self.move_cursor_relative(columns=offset)
            event.prevent_default()

    def on_mount(self) -> None:
        self.border_title = _("Input")

    def on_focus(self) -> None:
        self.styles.border = ("round", self.app.theme_variables.get("border"))
        self.styles.border_title_style = "bold"
        self.parent.on_focus()

    def on_blur(self) -> None:
        self.styles.border = ("round", (Color.parse(self.app.theme_variables.get("border")) +
                                        Color(0, 0, 0, 0.4)))
        self.styles.border_title_style = "none"
        self.parent.on_blur()

    def action_send_message(self):
        self.post_message(self.SendMessage(self.text))

    def action_expand(self) -> None:
        if self.styles.height.value == 1:
            self.styles.height = "12fr"
        else:
            self.styles.height = "1fr"

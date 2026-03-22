from textual.color import Color
from textual.widgets import ListView

from tool.i18n import I18n


class FriendList(ListView):
    def on_mount(self) -> None:
        self.border_title = I18n().t("friend_list_title")

    def on_focus(self) -> None:
        self.styles.border = ("round", self.app.theme_variables.get("border"))
        self.styles.border_title_style = "bold"

    def on_blur(self) -> None:
        self.styles.border = ("round", (Color.parse(self.app.theme_variables.get("border")) +
                                        Color(0, 0, 0, 0.4)))
        self.styles.border_title_style = "none"

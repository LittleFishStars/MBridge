from textual.widgets import ListView, ListItem


class MessageList(ListView):
    def __init__(
            self,
            *children: ListItem,
            name: str | None = None,
            id: str | None = None,
            classes: str | None = None
    ):
        super().__init__(
            *children,
            initial_index=None,
            name=name,
            id=id,
            classes=classes,
            disabled=True
        )

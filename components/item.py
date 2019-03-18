"""An item."""


class Item:
    """An item."""

    def __init__(self, use_function=None, **kwargs):
        """Constructor."""
        self.use_function = use_function
        self.function_kwargs = kwargs

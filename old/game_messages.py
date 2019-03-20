"""Messaging fun."""

import libtcodpy as libtcod

import textwrap


class Message:
    """A single message."""

    def __init__(self, text, color=libtcod.white):
        """Constructor."""
        self.text = text
        self.color = color


class MessageLog:
    """A log of messages."""

    def __init__(self, x, width, height):
        """Constructor."""
        self.messages = []
        self.x = x
        self.width = width
        self.height = height

    def add_message(self, message):
        """Add a message to the log."""
        # Split the message if necessary, among multiple lines
        new_msg_lines = textwrap.wrap(message.text, self.width)

        for line in new_msg_lines:
            # If the buffer is full, remove the first line to make room for the new one
            if len(self.messages) == self.height:
                del self.messages[0]

            # Add the new line as a Message object, with the text and the color
            self.messages.append(Message(line, message.color))

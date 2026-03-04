# 12) Logger with Class Counter
# Create Logger with:
# - class attribute: messages_logged
# - method: log(msg) increments counter


class Logger:
    messages_logged = 0

    def __init__(self, message: str) -> None:
        self._message = message
        Logger.messages_logged += 1

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, new_message: str):
        if new_message == "":
            raise ValueError("Message cannot be empty!")

        self._message = new_message

    def log(self):
        msgs = []
        msg = self.message
        msgs.append(msg)
        return msgs


if __name__ == "__main__":
    msg1 = Logger("salut")
    msg2 = Logger("sunt")
    msg3 = Logger("un")
    msg4 = Logger("test")
    print(msg1.log())

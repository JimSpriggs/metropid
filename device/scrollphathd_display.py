import scrollphathd

from device.display import Display


class ScrollPHatHDDisplay(Display):

    def __init__(self, logger):
        super().__init__(logger)
        self.message = None

    def set_message(self, message):
        if self.message is not None:
            if self.message == message:
                return
            scrollphathd.clear()
        print('Writing: '.format(message))
        scrollphathd.write_string(message, brightness=0.5)
        self.message = message

    def update_display(self):
        scrollphathd.show()
        scrollphathd.scroll()


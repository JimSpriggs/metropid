import scrollphathd

from device.display import Display


class ScrollPHatHDDisplay(Display):

    def __init__(self, logger):
        super().__init__(logger)

    def set_message(self, message):
        scrollphathd.write_string(message, brightness=0.5)

    def update_display(self):
        scrollphathd.show()
        scrollphathd.scroll()


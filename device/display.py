class Display:

    def __init__(self, logger):
        self.logger = logger

    def set_message(self, message):
        self.logger.info('Message: {}'.format(message))

    def update_display(self):
        pass
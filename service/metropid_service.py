class MetropidService:

    metrolink_data = {}
    prev_metrolink_data = {}

    def __init__(self, gateway, parser, logger):
        self.metrolink_data['message'] = 'Loading...'
        self.updated = True
        self.gateway = gateway
        self.parser = parser
        self.logger = logger

    def is_updated(self):
        return self.updated

    def check_for_update(self):
        # response = self.gateway.get_metrolinks()
        response = None

        self.metrolink_data = self.parser.parse(response)
        if self.metrolink_data != self.prev_metrolink_data:
            self.prev_metrolink_data = self.metrolink_data
            self.updated = True
        else:
            self.updated = False

    def get_update(self):
        return self.metrolink_data
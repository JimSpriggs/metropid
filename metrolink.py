#!/usr/bin/env python
import schedule
import logging
from parser.tfgm_response_parser import TfgmResponseParser
from gateway.tfgm_gateway import TfgmGateway
from service.metropid_service import MetropidService
from device.display import Display
from device.scrollphathd_display import ScrollPHatHDDisplay

logging.basicConfig(level = logging.DEBUG)
logger = logging.getLogger('metrolink')
tfgm_gateway = TfgmGateway()
tfgm_response_parser = TfgmResponseParser()
metropid_service = MetropidService(tfgm_gateway, tfgm_response_parser, logger)
display = ScrollPHatHDDisplay(logger)
#display = Display(logger)
updated = False

def check_for_updates():
    metropid_service.check_for_update()
    apply_updates()

def apply_updates():
    if metropid_service.is_updated():
        metrolink_data = metropid_service.get_update()
        display.set_message(metrolink_data['message'])

def run_scheduled():

    apply_updates()
    schedule.every(10).seconds.do(check_for_updates)

    while True:
        schedule.run_pending()
        display.update_display()

run_scheduled()
#check_for_updates()
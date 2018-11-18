import json

class TfgmResponseParser:

    example = '''{
  "@odata.context":"https://opendataclientapi.azurewebsites.net/odata/$metadata#Metrolinks","value":[
    {
      "Id":307,"Line":"Bury","TLAREF":"PRS","PIDREF":"PRS-TPTD01","StationLocation":"Prestwich","AtcoCode":"9400ZZMAPWC2","Direction":"Incoming","Dest0":"Piccadilly","Carriages0":"Double","Status0":"Due","Wait0":"7","Dest1":"Piccadilly","Carriages1":"Double","Status1":"Due","Wait1":"18","Dest2":"Piccadilly","Carriages2":"Double","Status2":"Due","Wait2":"30","Dest3":"","Carriages3":"","Status3":"","MessageBoard":"Unlimited travel before 7:30am between 1:00pm and 3:30pm and after 7:00pm on any week day just 3 pound with the Early Bird Plus. Buy on the get me there app by 7:00am. Visit tfgm/earlybird for info","Wait3":"","LastUpdated":"2018-11-18T19:57:20Z"
    }
  ]
}'''

    def parse(self, response):
        metdata = json.loads(response)
        message = ''
        if 'value' in metdata:
            values = metdata['value']
            for value in values:
                message += self.decode_trip(value, 0)
                message += self.decode_trip(value, 1)
                message += self.decode_trip(value, 2)
                message += self.decode_trip(value, 3)
            if message == '':
                if value['MessageBoard'] != '':
                    message = value['MessageBoard']
                else:
                    message = 'No trams'
        else:
            # unexpected response, better luck next time
            message = 'Connecting......   '

        return {
            'message': message
        }

    def decode_trip(self, value, index):
        msg = ''
        if value[f'Dest{index}'] is not None and value[f'Dest{index}'] != '':
            time = int(value[f'Wait{index}'])
            if time >= 7:
                carriages = ' sgl '
                if value[f'Carriages{index}'] == 'Double':
                    carriages = ' dbl '
                msg += value[f'Dest{index}'] + carriages + f'{time}    '
        return msg

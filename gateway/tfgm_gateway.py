import http.client

class TfgmGateway:

    def get_metrolinks(self):

        conn = http.client.HTTPConnection("api.tfgm.com")

        headers = {
            'Host': "api.tfgm.com",
            'Ocp-Apim-Subscription-Key': "b993ac5fb61041009c173ba92683dea8",
            'Cache-Control': "no-cache",
        }

        conn.request("GET", "odata/Metrolinks?$top=10&$filter=Line eq 'Bury' and StationLocation eq 'Prestwich' and AtcoCode eq '9400ZZMAPWC2'", headers=headers)

        res = conn.getresponse()
        data = res.read()

        print(data.decode("utf-8"))

        return data
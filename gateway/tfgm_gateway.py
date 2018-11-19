import http.client

class TfgmGateway:

    def get_metrolinks(self):
        conn = http.client.HTTPSConnection("api.tfgm.com")

        headers = {
            'host': "api.tfgm.com",
            'ocp-apim-subscription-key': "b993ac5fb61041009c173ba92683dea8",
            'cache-control': "no-cache",
            'postman-token': "75fae57a-bcbf-8e12-c06a-e7a3275fa67f"
        }

        conn.request("GET",
                     "/odata/Metrolinks?%24top=10&%24filter=Line%20eq%20'Bury'%20and%20StationLocation%20eq%20'Prestwich'%20and%20AtcoCode%20eq%20'9400ZZMAPWC2'",
                     headers=headers)

        res = conn.getresponse()
        data = res.read().decode("utf-8")

        print(data)
        return data

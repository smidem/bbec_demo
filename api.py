import config

action = 'AdHocQueryGetIDByName'
body = '''<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
               xmlns:xsd="http://www.w3.org/2001/XMLSchema"
               xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
              <soap:Body>
                <AdHocQueryGetIDByNameRequest xmlns="Blackbaud.AppFx.WebService.API.1">
                  <ClientAppInfo REDatabaseToUse="1234ABC" 
                                 ClientAppName="bbec_demo" 
                                 TimeOutSeconds="5"/>
                  <Name>Interaction Data List Query</Name>
                </AdHocQueryGetIDByNameRequest>
              </soap:Body>
            </soap:Envelope>'''


def set_head(endpoint):
    headers = config.headers.copy()
    headers.update({'SOAPAction': f'{config.base_endpoint}{endpoint}'})
    return headers


res = config.session.post(config.api, headers=set_head(action), data=body)
print(res)

# Machine to machine for microservice api

# request library to interact with the server/api
# json to make the resulting json into a redable format
import requests
import json

serverUrl='https://dwsfties-uat-api.epa.gov/api/auth/realms/sdwismod/protocol/openid-connect/token'

access_token = ''

# login credentials
credentials = {
    "grant_type":'password',
     # username and password will be provided to you
    "username": '<providedUsername>', 
    "password": '<providedPassword>'
}

# header
postHeaders = {
    "headers": "application/x-www-form-urlencoded"
}

# we send our login credentials to the server to get the access_token and other relevant information
serverResponse = requests.post(serverUrl, data=credentials, headers=postHeaders)

# process the response
if serverResponse.status_code != 200:
    print("Failed to get tokens:", serverResponse.status_code, serverResponse.text)
else:
    actualResponse = serverResponse.json()
    # print(actualResponse)
    access_token = actualResponse.get("access_token")
    refresh_token = actualResponse.get("refresh_token")
    token_type = actualResponse.get("token_type")
    expires_in = actualResponse.get("expires_in")
    # print("Access token: ", access_token)

# Now we have the access_token, we're ready to call the api
inventoryApi = "https://inventory.dwsfties-uat-api.epa.gov"

headerForApi = {
    "Authorization": f"Bearer {access_token}"
}

apiCall = requests.get(f"{inventoryApi}/inventory/water-system", headers=headerForApi)

if apiCall.status_code != 200:
    print("Api call failed with the token: ", apiCall.status_code, apiCall.text)
else:
    data = apiCall.json()
    print(json.dumps(data, indent=4))



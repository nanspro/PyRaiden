import json, requests
import os, pprint

API_ENDPOINT = 'http://localhost:5001/api/v1/'

# Querying Information About Your Raiden Node
url = API_ENDPOINT + 'address'
r = requests.get(url)
response = json.loads(r.text)
pprint.pprint(response)

# Querying channels and tokens

# # Get a list of all unsettled channels
# url = API_ENDPOINT + 'channels'
# r = requests.get(url)
# response = json.loads(r.text)
# pprint.pprint(response)

# # Get a list of all unsettled channels for the given token address.
# TOKEN_ADDR = '0x380EB4e2C14ee155DBb55Ee1670B3B2f5b34eC85'
# url = API_ENDPOINT + 'channels/' + TOKEN_ADDR
# r = requests.get(url)
# response = json.loads(r.text)
# pprint.pprint(response)

# # Query information about one of your channels
# PARTNER_ADDR = '0x61C808D82A3Ac53231750daDc13c777b59310bD9'
# url = API_ENDPOINT + 'channels/' + TOKEN_ADDR + '/' + PARTNER_ADDR
# r = requests.get(url)
# response = json.loads(r.text)
# pprint.pprint(response)

# # A list of addresses of all registered tokens.
# url = API_ENDPOINT + 'tokens'
# r = requests.get(url)
# response = json.loads(r.text)
# pprint.pprint(response)

# # Returns the address of the corresponding token network for the given token, if the token is registered.
# url = API_ENDPOINT + 'tokens/' + TOKEN_ADDR
# r = requests.get(url)
# response = json.loads(r.text)
# pprint.pprint(response)

# # Returns a list of all partners with whom you have non-settled channels for a certain token.
# url = API_ENDPOINT + 'tokens/' + TOKEN_ADDR + '/partners'
# r = requests.get(url)
# response = json.loads(r.text)
# pprint.pprint(response)

# # Returns a list of all transfers that have not been completed yet.
# url = API_ENDPOINT + 'pending_transfers'
# r = requests.get(url)
# response = json.loads(r.text)
# pprint.pprint(response)

# # Returns a list of all transfers for a token that have not been completed yet.
# url = API_ENDPOINT + 'pending_transfers/' + TOKEN_ADDR
# r = requests.get(url)
# response = json.loads(r.text)
# pprint.pprint(response)

# # Returns a list of all transfers for a token limited to a specific channel
# url = API_ENDPOINT + 'pending_transfers/' + TOKEN_ADDR + '/' + PARTNER_ADDR
# r = requests.get(url)
# response = json.loads(r.text)
# pprint.pprint(response)

# Registers a token. If a token is not registered yet
# url = API_ENDPOINT + 'tokens/' + '0x24c2242E3bC74C8b9B523aFd7080Eed951B72686'
# r = requests.put(url)
# response = json.loads(r.text)
# pprint.pprint(response)

TEST_TOKEN_ADDR = '0x24c2242E3bC74C8b9B523aFd7080Eed951B72686'

# Channel Management

# Opens (i. e. creates) a channel.
HEADER = { 'Content-Type': 'application/json', }
# url = API_ENDPOINT + 'channels'
# data = { 'partner_address': '0x102AE332d990c77B4803F6f1BFB2cD71E63C7dbb', \
#     'settle_timeout': 500, 'token_address': '0x380EB4e2C14ee155DBb55Ee1670B3B2f5b34eC85', \
#         'total_deposit': 3500000000000000000}
# r = requests.put(url, headers=HEADER, json=data)
# response = json.loads(r.text)
# pprint.pprint(response)

# This request is used to close a channel or to increase the deposit in it.
# url = API_ENDPOINT + 'channels/' + TEST_TOKEN_ADDR + '/0x4fc91De80f00A2d67139dF88458AF53F8d5910c2'
# data = { 'state': 'closed' }
# data2 = { 'total_deposit': 100 }
# r = requests.patch(url, headers=HEADER, json=data2)
# response = json.loads(r.text)
# pprint.pprint(response)

# r = requests.patch(url, headers=HEADER, json=data)
# response = json.loads(r.text)
# pprint.pprint(response)


# # Query details of all joined token networks.
# url = API_ENDPOINT + 'connections'
# r = requests.get(url)
# response = json.loads(r.text)
# pprint.pprint(response)

# Join a token network.
# url = API_ENDPOINT + 'connections/' + '0x380EB4e2C14ee155DBb55Ee1670B3B2f5b34eC85'
# data = { 'funds': '2000000000000000000' }
# r = requests.put(url, headers=HEADER, json=data)
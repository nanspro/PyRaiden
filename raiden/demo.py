from client import Client

TOKEN_ADDR = '0x380EB4e2C14ee155DBb55Ee1670B3B2f5b34eC85'
PARTNER_ADDR = '0x61C808D82A3Ac53231750daDc13c777b59310bD9'

client = Client('http://localhost:5001/', 'v1')

address = client.get_address()
tokenChannels = client.get_channels_for_token(TOKEN_ADDR)
tokenPartners = client.get_channels_for_token_with_partner(TOKEN_ADDR,
                                                           PARTNER_ADDR)
print(address)
print(tokenChannels)
print(tokenPartners)

''' Raiden Unit Tests '''
from client import Client

client = Client('http://localhost:5001/', 'v1')
TOKEN_ADDR = '0x380EB4e2C14ee155DBb55Ee1670B3B2f5b34eC85'
PARTNER_ADDR = '0x61C808D82A3Ac53231750daDc13c777b59310bD9'


def test_address():
    resp = client.get_address()
    address = resp['our_address']
    if address != '0x41a06892815a450c8bB7297C65290a0864871677':
        raise AssertionError()


if __name__ == "__main__":
    test_address()
    print("All tests passed")

from client import Client

client = Client('http://localhost:5001/', 'v1')

address = client.get_address()

# PyRaiden
A client library to interact with raiden network (an off-chain scaling solution using state channels) written in python.

## Prerequisites
You should have raiden running on a node with your ethereum address and you should've access to the rpc endpoint for the 
node.

``` python
# Create a raiden client like this
client = Client('http://localhost:5001/', 'v1')

# Get address
response = client.get_address()
your_address = response['our_address']

# Get channels for a particular registered token
tokenChannels = client.get_channels_for_token('0x380EB4e2C14ee155DBb55Ee1670B3B2f5b34eC85')
```

**Demo Usage**

``` python
cd raiden
# Get responses for all the methods possible
python3 demo.py
```

**Testing**
```python
cd raiden
python3 test.py
```

You can view `raiden/cleint.py` to see all different methods of class `Client` 


# PyRaiden
A client library to interact with raiden network (an off-chain scaling solution using state channels) written in python.

## Prerequisites
You should have raiden running on a node with your ethereum address and you should've access to the rpc endpoint for the 
node.

Create a raiden client like this
``` python
client = Client('http://localhost:5001/', 'v1')
your_ address = client.get_address()
```

**Demo Usage**

``` python
cd raiden
# Get responses for all the methods possible
python3 demo.py
```

You can view `raiden/cleint.py` to see different methods of class client 


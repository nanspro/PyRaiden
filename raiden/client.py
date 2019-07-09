import os, requests
import json

class Client:
    'Creates a client object who will interact with raiden'
    API_ENDPOINT = ''

    def __init__(self, url, version):
        self.url = url
        self.version = version
        Client.API_ENDPOINT = url + '/api/' + version
    
    def request(self, endpoint, method = 'get', header = None, data = None):
        if method == 'get':
            r = requests.get(endpoint)
        elif method == 'put':
            if header == None and data == None:
                r = requests.put(endpoint)
            else:
                r = requests.put(endpoint, headers=header, json=data)
        elif method == 'patch':
            r = requests.patch(endpoint, headers=header, json=data)
        elif method == 'post':
            r = requests.post(endpoint, headers=header, json=data)
        elif method == 'delete':
            r = requests.delete(endpoint, headers=header)
        response = json.loads(r.text)
        return response
    
    def get_address(self):
        endpoint = Client.API_ENDPOINT + '/address'
        return self.request(endpoint)
    
    def get_pending_transfers(self):
        endpoint = Client.API_ENDPOINT + '/pending_transfers'
        return self.request(endpoint)
    
    def get_pending_token_transfers(self, addr):
        endpoint = Client.API_ENDPOINT + '/pending_transfers/' + addr
        return self.request(endpoint)
    
    def get_pending_channel_transfers(self, tokenAddr, partnerAddr):
        endpoint = Client.API_ENDPOINT + '/pending_transfers/' + tokenAddr + '/' + partnerAddr
        return self.request(endpoint)
    
    def register_token(self, addr):
        endpoint = Client.API_ENDPOINT + '/tokens/' + addr
        return self.request('put', endpoint)

    def get_all_tokens(self):
        endpoint = Client.API_ENDPOINT + '/tokens/'
        return self.request(endpoint)

    def get_registered_tokenAddr(self, addr):
        endpoint = Client.API_ENDPOINT + '/tokens/' + addr
        return self.request(endpoint)
    
    def get_token_partners(self, addr):
        endpoint = Client.API_ENDPOINT + '/tokens/' + addr + '/partners'
        return self.request(endpoint)    
    
    def get_channels(self):
        endpoint = Client.API_ENDPOINT + '/channels'
        return self.request(endpoint)

    def get_channels_for_token(self, addr):
        endpoint = Client.API_ENDPOINT + '/channels/' + addr
        return self.request(endpoint)
    
    def get_channels_for_token_with_partner(self, tokenAddr, partnerAddr):
        endpoint = Client.API_ENDPOINT + '/channels/' + tokenAddr + '/' + partnerAddr
        return self.request(endpoint)
    
    def create_channel(self, header, data):
        endpoint = Client.API_ENDPOINT + '/channels'
        return self.request('put', endpoint, header, data)

    def close_channel(self, header, data, tokenAddr, partnerAddr):
        endpoint = Client.API_ENDPOINT + '/channels' + tokenAddr + '/' + partnerAddr
        return self.request('patch', endpoint, header, data)
    
    def increase_deposit(self, header, data, tokenAddr, partnerAddr):
        endpoint = Client.API_ENDPOINT + '/channels' + tokenAddr + '/' + partnerAddr
        return self.request('patch', endpoint, header, data)

    def get_networks(self):
        endpoint = Client.API_ENDPOINT + '/connections/'
        return self.request(endpoint)
    
    def join_network(self, addr, header, data):
        endpoint = Client.API_ENDPOINT + '/connections/' + addr
        return self.request('put', endpoint, header, data)

    def leave_network(self, addr, header):
        endpoint = Client.API_ENDPOINT + '/connections/' + addr
        return self.request('delete', endpoint, header)
    
    def pay(self, tokenAddr, targetAddr, header, data):
        endpoint = Client.API_ENDPOINT + '/payments' + tokenAddr + '/' + targetAddr
        return self.request('post', endpoint, header, data)
    
    def get_events(self, tokenAddr, targetAddr):
        endpoint = Client.API_ENDPOINT + '/payments' + tokenAddr + '/' + targetAddr
        return self.request(endpoint)
    
class Login:

    def __init__(self, pc):
        self.pc = pc
        self.auth_client

    def create_auth_client(self, key, b64secret, passphrase, product = None, url = None):

        if (product != None):
            # Set a default product
            auth_client = self.pc.AuthenticatedClient(key, b64secret, passphrase,
                                                   product_id=product)

        if (url != None):
            # Use the sandbox API (requires a different set of API access credentials)
            auth_client = self.pc.AuthenticatedClient(key, b64secret, passphrase,
                                                   api_url=url)
        else:
            auth_client = self.pc.AuthenticatedClient(key, b64secret, passphrase)

        return auth_client

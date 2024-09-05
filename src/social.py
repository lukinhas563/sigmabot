from atproto import Client, client_utils

class Social:
    def __init__(self, username: str, password: str):
        self.client = Client()
        self.profile = self.client.login(username, password)
        print('Welcome, ', self.profile.display_name)
    
    def post(self, text: str):
        message = client_utils.TextBuilder().text(text)
        post = self.client.send_post(message)
        self.client.like(post.uri, post.cid)
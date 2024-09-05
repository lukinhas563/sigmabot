from src.post import Post
from src.social import Social

class Builder:
    def __init__(self):
        self.post = None
        self.social = None
    
    def set_post(self, post: Post):
        self.post = post
        return self
    
    def set_social(self, social: Social):
        self.social = social
        return self
    
    def build(self):
        return Bot(self)

class Bot:
    def __init__(self, builder: Builder):
        self.post = builder.post
        self.social = builder.social
    
    def run(self):
        try:
            post = self.post.generate()
            self.social.post(post)
            print(post)
        except Exception as e:
            print(f"Erro ao postar: {e}")
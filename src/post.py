from markovify import Text

class Post:
    def __init__(self, model: Text):
        self.model = model

    def generate(self) -> str:
        sentence = None

        while sentence == None:
            sentence = self.model.make_sentence(tries=100)
            
        return sentence
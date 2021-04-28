
class Command:
    def __init__(self, user_input, response):
        self.user_input = user_input
        self.response = response
    def Procedure(self, inputString) -> str:
        if self.user_input in inputString:
            return self.response

all = [
    Command("joe mama", "good question"),
    Command("you suck", "no, please do not say that")
]
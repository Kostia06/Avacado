import argparse

class Arg:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description = "Your Project Manager")
        self.parser.add_argument("-a", "--api_key", type = str, help = "OpenAI API key.")
        self.parser.add_argument("-m",  "--message", type = str, help = "Message to send to the AI.")
        self.parser.add_argument('cd', nargs=argparse.REMAINDER, help='Change directory')
        self.args = vars(self.parser.parse_args())

    def get(self, key):
        return self.args.get(key, None)




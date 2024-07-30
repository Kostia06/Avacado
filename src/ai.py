from openai import OpenAI

class AI:
    def __init__(self, api_key):
        self.client = OpenAI(api_key = api_key)

    def create_prompt(self, text):
        chat_completion = self.client.chat.completions.create(
            messages = [
                {
                    "role": "system",
                    "content": text,
                }
            ],
            model = "gpt-3.5-turbo"
        )
        return chat_completion


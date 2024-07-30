from store import Store
from ai import AI
from arg import Arg

def main():
    store = Store()
    arg = Arg()

    api_key = arg.get("api_key")
    message = arg.get("message")

    if message and not api_key:
        print("Please provide a API key to use the AI. In this website, you can get a free API key: \"https://platform.openai.com/settings/profile?tab=api-keys\" ")
        return

    if api_key:
        store.set("api_key", api_key)
        ai = AI(store.get("api_key"))
        if message:
            print(ai.create_prompt(message).choices[0].message.content)


if __name__ == "__main__":
    main()

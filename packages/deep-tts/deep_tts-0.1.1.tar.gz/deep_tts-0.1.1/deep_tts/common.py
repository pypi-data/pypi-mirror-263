class DeepTTS:
    def __init__(self, token: str):
        self.token = token

    def generate(self, text: str):
        if self.token:
            return "Generated audio for: " + text


if __name__ == "__main__":
    tts = DeepTTS("this_is_a_token")
    print(tts.generate("Hello, world!"))

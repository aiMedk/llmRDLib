from ollama import Client

class OllamaChat:
    def __init__(self, host='http://0.0.0.0:8000'):
        """
        Intialiser Ollama client.

        """
        self.client = Client(host=host)

    def chat(self, model, content):
        """
        Le contenu du message.

        """
        messages = [{'role': 'user', 'content': content}]
        response = self.client.chat(model=model, messages=messages)
        return response

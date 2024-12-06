import argparse
from .llm_client import OllamaChat

def main():
    parser = argparse.ArgumentParser(description='coomuniquer avec Ollama chat via API.')
    parser.add_argument('-m', '--model', required=True, help='Le model à utiliser (ex., "llama3").')
    parser.add_argument('-c', '--content', required=True, help='Le contenu du message.')
    parser.add_argument('--host', default='http://0.0.0.0:8000', help='le host du serveur Ollama (default: http://0.0.0.0:8000).')

    args = parser.parse_args()

    ollama_client = OllamaChat(host=args.host)

    response = ollama_client.chat(model=args.model, content=args.content)

    print(response)
t
if __name__ == '__main__':
    main()

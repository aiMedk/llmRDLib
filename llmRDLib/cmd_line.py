import argparse
from .llm_client import OllamaChat

def main():
    parser = argparse.ArgumentParser(description='coomuniquer avec Ollama chat via API.')
    parser.add_argument('-m', '--model', required=True, help='Le model à utiliser (ex., "llama3").')
    parser.add_argument('-c', '--content', required=True, help='Le contenu du message.')
    parser.add_argument('--host', default='http://0.0.0.0:8000', help='le host du serveur Ollama (default: http://0.0.0.0:8000).')
    parser.add_argument('--res', type=str, help='Parametre optionnel pour afficher le score d\'une comparaison.')



    args = parser.parse_args()

    ollama_client = OllamaChat(host=args.host)

    response = ollama_client.chat(model=args.model, content=args.content)
    if args.res:
        score = ollama_client.Cmp(desired_output=args.res, generated_output= response['message']['content'])
        print(f"Score: {round(score*100)}%")
    else:
        print(response['message']['content'])

if __name__ == '__main__':
    main()

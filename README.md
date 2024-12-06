# llmRDLib

`llmRDLib` est une bibliothèque Python qui permet d’interagir avec l’API Ollama Chat. Elle facilite l’envoi de messages à un modèle spécifique et la réception des réponses.

---

## Fonctionnalités

- **Client Simple** : Interagissez facilement avec l’API Ollama Chat.
- **Interface en Ligne de Commande (CLI)** : Utilisez la bibliothèque via la ligne de commande avec des paramètres pour le modèle et le contenu.

---

Utilisation
En tant que bibliothèque

Voici un exemple d'utilisation dans un script Python :
```python
from llmRDLib import OllamaChat

client = OllamaChat(host="http://0.0.0.0:8000")
response = client.chat(model="llama3", content="Bonjour, comment ça va ?")
print(response)
```
En ligne de commande

Exécutez directement depuis le terminal :
```bash
llmRDLib -m llama3 -c "Bonjour, le monde !"
```
Explications des paramètres :

    -m ou --model : Spécifiez le modèle à utiliser (exemple : "llama3").
    -c ou --content : Le contenu du message à envoyer.
    --host : (Optionnel) L'URL du serveur Ollama (par défaut : http://0.0.0.0:8000).

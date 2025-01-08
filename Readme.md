# llmRDLib

`llmRDLib` est une bibliothèque Python qui permet d’interagir avec l’API Ollama Chat. Elle facilite l’envoi de messages à un modèle spécifique et la réception des réponses.

---

## Fonctionnalités

- **Client Simple** : Interagissez facilement avec l’API Ollama Chat.
- **Interface en Ligne de Commande (CLI)** : Utilisez la bibliothèque via la ligne de commande avec des paramètres pour le modèle et le contenu.

---


## 1. Pré-requis

Assurez-vous d'avoir les éléments suivants installés sur votre machine :
- **Python** : Version 3.7 ou supérieure.
- **Git** : Un outil de contrôle de version.

---


## 2. Création d'un environnement virtuel

Pour éviter les conflits avec les dépendances globales de Python, il est recommandé d'utiliser un environnement virtuel.

1. Créez un environnement virtuel :
   ```bash
   python3 -m venv venv
   #Activez l'environnement virtuel :
   #Sur Linux/macOS :
   source venv/bin/activate

   #Sur Windows :
   venv\Scripts\activate

## 3. Cloner le dépôt GitHub

Clonez le dépôt llmRDLib et naviguez dans son répertoire :
```bash
git clone https://github.com/aiMedk/llmRDLib.git
cd llmRDLib
```

## 4. Installation de la bibliothèque

Installez la bibliothèque et ses dépendances à l'aide de pip :
```bash
pip install .
#Vérifiez si la commande est disponible :
llmRDLib --help
```

## 5. Utilisation de la bibliothèque
En ligne de commande

Vous pouvez envoyer un message à un modèle spécifique directement depuis le terminal :
```bash
llmRDLib -m llama3 -c "Bonjour, comment ça va ?"
```

En tant que bibliothèque Python

Utilisez la bibliothèque dans un script Python :
```python
from llmRDLib import OllamaChat

client = OllamaChat(host="http://0.0.0.0:8000")
response = client.chat(model="llama3", content="Bonjour, le monde !")
print(response)
```
from ollama import Client
from rouge_score import rouge_scorer
from sentence_transformers import SentenceTransformer, util

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
    def Cmp(self, desired_output, generated_output):
        
        scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
        scores = scorer.score(desired_output, generated_output)

        # Cosine Similarity
        model = SentenceTransformer('all-MiniLM-L6-v2') 
        embeddings1 = model.encode(desired_output, convert_to_tensor=True)
        embeddings2 = model.encode(generated_output, convert_to_tensor=True)
        cosine_score = util.pytorch_cos_sim(embeddings1, embeddings2).item()
        # print(f"Cosine Similarity: {cosine_score}")
        w_rouge_l = 0.15
        w_cosine = 0.85

        return (w_rouge_l * scores["rougeL"].fmeasure) + (w_cosine * cosine_score)


    
    

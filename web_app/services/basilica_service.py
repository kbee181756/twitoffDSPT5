# web_app/services/basilica_service.py
# web_app/services/basilica_service.py 

import os 
import basilica



from dotenv import  load_dotenv

load_dotenv()  # parse the .evv file for the environment variable

BASILICA_API_KEY = os.getenv("BASILICA_API_KEY")

connection = basilica.Connection('b4e679b7-5d94-d89e-70a2-3332c31a6b7a')
print(type(connection))


if __name__ == '__main__':
    
    print(type(connection)) #> <basilica.Connection object at 0x102081b10>
    sentences = ["Hello world!", "How are you?"]
    embeddings = connection.embed_sentences(sentences)
    print(list(embeddings)) # [[0.8556405305862427, ...], ...]
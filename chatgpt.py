from openai import OpenAI
from openai import APIError
from bs4 import BeautifulSoup
import requests as re

api_Key = ""

class Chatbot:

    def __init__(self, api_key: str) -> None:
        self.name = 'summary bot'
        self.client = OpenAI(api_key=api_key)
    
    def generate_text(self, msg: str, role:str="user") -> str:
        try:
            completion = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": role, "content": "Give me a summary for the article"},
                    {"role": role, "content": msg}
                ]
            )
            return completion.choices[0].message['content']
        except APIError as e:
            print(f"Message:{e.message}")
                
    def generate_content(self, url: str) -> str:
        response = re.get(url)
        content = response.content
        soup = BeautifulSoup(content,"html.parser")
        paragraphs = soup.find_all('p')
        text = ' '.join([para.get_text() for para in paragraphs])
        return text

'''''
if __name__ == "__main__":
    html = 'https://doi.org/10.1007/s00264-018-4116-3'
    chat = Chatbot(api_Key)
    role = "user"
    text = chat.generate_content(html)
    print(chat.generate_text("how are you"))

'''
    
    








                              

    
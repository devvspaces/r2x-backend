import json
import re

from models.generative import GenerativeModel
from models.mindsdb import GptModel

class TextGenerator:
    def __init__(self, model: GenerativeModel):
        self.__model = model
    
    def generate(self, input: str, **kwargs) -> str:
        return self.__model.prompt(input, **kwargs)
    
    def generate_with_format(self, input: str, format: str, **kwargs):
        question = f'{input} in this {format}'
        answer = self.generate(question, **kwargs)
        return self.extract_json(answer)
    
    def extract_json(self, text: str) -> dict:
        json_data = re.search(r'\[.*\]', text, re.DOTALL)
        if json_data:
            json_data = json_data.group()
        else:
            raise Exception('No JSON data found in the text.')
        return json.loads(json_data)


generator = TextGenerator(GptModel())

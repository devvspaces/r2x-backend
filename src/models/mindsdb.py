

from models.generative import GenerativeModel
from utils.base.mindsdb import connect_server


class GptModel(GenerativeModel):
    """
    GPT model proxy using MindsDB.
    """

    project_name = 'mindsdb'
    model_name = 'openai'

    def __init__(self):
        self.__connection = connect_server()

    def __make_query(self, input: str) -> str:
        return f"""
        SELECT question, answer
        FROM {self.project_name}.{self.model_name}
        WHERE question = '{input}'
        """

    def prompt(self, input, **kwargs) -> str:
        project = self.__connection.get_project(self.project_name)
        df = project.query(self.__make_query(input)).fetch()
        return df['answer'][0]

    def prompt_with_context(self, input, context: str, **kwargs) -> str:
        return self.__model(input, context=context, **kwargs)

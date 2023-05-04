import openai, datetime
from src.config import BaseConfig
openai.api_key = BaseConfig.API_KEY


class ChatGPT(object):
    def __init__(self):
        self.completion = openai.Completion
        self.counter = 0

    def get_result(self, question: str):
        try:
            questions = [
                f"Make short question: {question}",
                f"What a keywords of this question: {question} Write only keywords with separator ','",
                question,
                f"Make 3 alternatives of this question: {question} Write only alternatives with separator ','",
                f"Make a description of this question: {question}"
            ]
            lst = []
            self.counter = self.counter + 1
            for q in questions:
                lst.append(self.completion.create(
                    engine="text-davinci-002",
                    prompt=q,
                    max_tokens=1024,
                    n=1,
                    stop=None,
                    temperature=0.5
                    ).choices[0].text
                )

            return {
                "Question_ID": self.counter,
                "Question_short": lst[0].strip(),
                "Question_original": question,
                "Keywords": lst[1].strip().split(", "),
                "Answer_plain_text": lst[2],
                "Answer_original": lst[2].strip(),
                "Question_original_alternatives": lst[3].strip().split("\n"),
                "Question_short_alternatives": lst[3].strip().split("\n"),
                "Notes": lst[4].strip(),
                "Source_type": "SP_FAQ",
                "date": f"{datetime.datetime.now().year}-{datetime.datetime.now().month}-{datetime.datetime.now().day}"
            }
        except:
            return {
                "Answer_original": "Error"
            }

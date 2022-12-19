import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from conversation_qa.utils import generate_answer, get_answer_prompt, clean_answer

_device = "cuda" if torch.cuda.is_available() else "cpu"


class QA:
    def __init__(self, model_name: str):
        self._model = GPT2LMHeadModel.from_pretrained(model_name)
        self._model.to(_device)
        if torch.cuda.is_available():
            self._model.half()

        self._tokenizer = GPT2Tokenizer.from_pretrained(model_name)

    def get_answer(self, text: str, dialogue: str, query: str) -> str:
        prompt = get_answer_prompt(text, query, dialogue)
        answer = generate_answer(self._model, self._tokenizer, prompt)
        return clean_answer(answer, text)


class Dialogue:
    def __init__(self):
        self._dialogue_pairs = []

    def add_dialogue_pair(self, query: str, answer: str) -> "Dialogue":
        self._dialogue_pairs.append((query, answer))
        return self

    def get_text(self) -> str:
        text = ""
        for query, answer in self._dialogue_pairs:
            text += f"Q: {query}\n"
            text += f"A: {answer}\n"

        return text

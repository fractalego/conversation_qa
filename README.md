# Conversational QA
This framework is trained on the [CoQA dataset](https://stanfordnlp.github.io/coqa/).


# Install
pip install conversation_qa


# Example 
```python

from conversation_qa import QA, Dialogue

qa = QA("fractalego/conversation-qa")

dialogue = Dialogue()
dialogue.add_dialogue_pair("Where was the cat?", "The fence.")

text = "A white cat is on the fence."
query = "What color is it?"
expected = "white"
qa.get_answer(text, dialogue.get_text(), query)
```

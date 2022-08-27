# Conversational QA
This framework is trained on the [CoQA dataset](https://stanfordnlp.github.io/coqa/).


# Install
pip install conversation-qa


# Example 
```python

from conversation_qa import QA, Dialogue

qa = QA("fractalego/conversation-qa")

dialogue = Dialogue()
dialogue.add_dialogue_pair("Where was the cat?", "The fence.")

text = "A white cat is on the fence."
query = "What color is it?"
qa.get_answer(text, dialogue.get_text(), query)
```

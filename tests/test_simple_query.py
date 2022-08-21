import unittest

from conversation_qa import QA, Dialogue


class TestQuery(unittest.TestCase):
    def test_simple_query(self):
        qa = QA("fractalego/conversation-qa")
        dialogue = Dialogue()
        dialogue.add_dialogue_pair("Where was the cat?", "The fence.")
        text = "A white cat is on the fence."
        query = "What color is it?"
        expected = "white"
        prediction = qa.get_answer(text, dialogue.get_text(), query)
        self.assertTrue(prediction.lower(), expected)

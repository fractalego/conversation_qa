import unittest

from conversation_qa import QA, Dialogue


class TestQuery(unittest.TestCase):
    def test__simple_query(self):
        qa = QA("fractalego/conversation-qa")
        dialogue = Dialogue()
        dialogue.add_dialogue_pair("Where was the cat?", "The fence.")
        text = "A white cat is on the fence."
        query = "What color is it?"
        expected = "white"
        prediction = qa.get_answer(text, dialogue.get_text(), query)
        self.assertTrue(prediction.lower(), expected)

    def test__empty_text(self):
        qa = QA("fractalego/conversation-qa")
        dialogue = Dialogue()
        text = "."
        query = "What color is it?"
        expected = "unknown"
        prediction = qa.get_answer(text, dialogue.get_text(), query)
        self.assertTrue(prediction.lower(), expected)
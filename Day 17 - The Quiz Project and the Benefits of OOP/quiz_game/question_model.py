class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text.replace("&quot;", '"')
        self.answer = q_answer

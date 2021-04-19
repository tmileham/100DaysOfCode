PROJECT_PATH = "C:/Users/Tom/Desktop/Python/100 Days of Code/Day 24 - Files, Directories and Paths/"
NAME_PATH = "{0}Input/Names/invited_names.txt".format(PROJECT_PATH)
LETTER_TEMPLATE_PATH = "{0}Input/Letters/starting_letter.txt".format(PROJECT_PATH)
LETTER_OUTPUT_PATH = "{0}Output/ReadyToSend/".format(PROJECT_PATH)
PLACEHOLDER = "[name]"


class LetterHandler:
    def __init__(self):
        self.recipients = []
        self.load_names()

    def load_names(self):
        with open(NAME_PATH, mode="r") as f:
            self.recipients = f.readlines()

    def load_letter(self):
        with open(LETTER_TEMPLATE_PATH, mode="r") as f:
            self.content = f.read()

    def write_letter(self, recipient):
        self.load_letter()
        PLACEHOLDER = "[name]"
        self.content = self.content.replace(PLACEHOLDER, recipient)
        print(self.content)

        with open(
            "{0}letter_for_{1}.txt".format(LETTER_OUTPUT_PATH, recipient), mode="w"
        ) as f:
            f.write(self.content)

    def mail_merge(self):
        for r in self.recipients:
            self.write_letter(r.strip("\n"))

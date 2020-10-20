

class Question:
    def __init__(self, question, a1, a2, a3, a4, a5, answer):
        self.__question = question
        self.__a1 = a1
        self.__a2 = a2
        self.__a3 = a3
        self.__a4 = a4
        self.__a5 = a5
        self.__answer = answer

    def set_question(self, question):
        self.__question = question

    def set_a1(self, a1):
        self.__a1 = a1

    def set_a2(self, a2):
        self.__a2 = a2

    def set_a3(self, a3):
        self.__a3 = a3

    def set_a4(self, a4):
        self.__a4 = a4

    def set_a5(self, a5):
        self.__a5 = a5

    def set_answer(self, answer):
        self.__answer = answer

    def get_question(self):
        return self.__question

    def get_a1(self):
        return self.__a1

    def get_a2(self):
        return self.__a2

    def get_a3(self):
        return self.__a3

    def get_a4(self):
        return self.__a4

    def get_a5(self):
        return self.__a5

    def get_answer(self):
        return self.__answer


def main():
    q1 = question.Question("What was the first planet that the covenant invaded?", "A. Harvest", "B. Earth",
                           "C. Reach", "D. Onyx")
    q2 = question.Question("What year did the Human-Covenant war start?", "A. 2020", "B. 2457", "C. 2525", "D. 2552")
    q3 = question.Question("What was the way the Covenant destroyed human worlds?", "A. Infection", "B. Glassing",
                           "C. Overwhelming Forces", "D. Both B and C")
    q4 = question.Question("What was the name of the Spartan that saved humanity?", "A. Kat-B320", "B. Lucy-B901",
                           "C. John-117", "D. Jorge-052")
    q5 = question.Question("What event was the beginning of the end for the Covenant empire?", "A. The Great Break",
                           "B. The Great Schism", "C. The Grunt Rebellion", "D. The Great Journey")

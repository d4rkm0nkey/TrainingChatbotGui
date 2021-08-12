
class AnswerTypes():
    NONE = "none"
    ANSWER = "answer"
    QUESTION_TOPIC = "qtopic"
    NEW_TOPIC = "ntopic"

    @staticmethod
    def getTypes():
        types = []
        for type in dir(AnswerTypes):
            if not type.startswith("_"):
                t = AnswerTypes.__dict__[type]
                if isinstance(t, str):
                    types.append(t)
        return types

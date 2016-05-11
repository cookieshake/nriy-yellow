from twkorean import TwitterKoreanProcessor


class Ongari:
    def __init__(self):
        self.tkp = TwitterKoreanProcessor()

    def tokenize(self, text):
        tokens = self.tkp.tokenize(text)

        rtText = ""

        for tk in tokens:
            if tk[1] != "Space": rtText += tk[0] + " : " + tk[1] + "\n"

        return rtText


if __name__ == '__main__':
    o = Ongari()
    print(o.tokenize("집에 가고 싶닼ㅋㅋㅋ"))

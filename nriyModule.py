import random
import jpype

from ongari import Ongari


class NriyModule:
    userDic = {}

    def makeTextMessage(self, text):
        rp = {
            "message": {
                "text": text
            }
        }
        return rp

    def handle(self, rq):
        jpype.attachThreadToJVM()
        o = Ongari()

        m_user_key = rq["user_key"]
        m_type = rq["type"]
        m_content = rq["content"]

        if m_user_key not in self.userDic:
            self.userDic[m_user_key] = {"status": "normal"}

        if m_type == "text" and m_content.split()[0] == "--선택":
            response = self.select(m_content)

        else:
            response = o.tokenize(m_content)

        return self.makeTextMessage(response)


    def select(self, text):
        args = text.split("\n")[1:]
        if len(args) == 0:
            rptext = "선택할걸 입력해줘여"
        else:
            pick = random.choice(args)
            rptext = pick + " --> 이게 좋을듯 ㅇㅇ"

        return rptext

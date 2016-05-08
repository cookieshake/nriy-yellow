import json

import nriyModule
from flask import Flask, request

app = Flask(__name__)
nm = nriyModule.NriyModule()

@app.route('/', methods=['POST','GET'])
def index():
    return "NRIY-YELLOW"

@app.route('/keyboard', methods=['POST','GET'])
def keyboard():
    response = {
        "type": "text"
    }

    return json.dumps(response)


@app.route('/message', methods=['POST','GET'])
def message():
    """
    Request 예제
    ----------------------------------------------------------------------------
    {
      "user_key": "encryptedUserKey",
      "type": "text",
      "content": "차량번호등록"
    }
    ----------------------------------------------------------------------------
    {
      "user_key": "encryptedUserKey",
      "type": "photo",
      "content": "http://photo_url/number.jpg"
    }
    ============================================================================
    Response 예제
    {
        "message":{
            "text" : "귀하의 차량이 성공적으로 등록되었습니다. 축하합니다!"
        }
    }
    ----------------------------------------------------------------------------
    {
      "message": {
        "text": "귀하의 차량이 성공적으로 등록되었습니다. 축하합니다!",
        "photo": {
          "url": "https://photo.src",
          "width": 640,
          "height": 480
        },
        "message_button": {
          "label": "주유 쿠폰받기",
          "url": "https://coupon/url"
        }
      },
      "keyboard": {
        "type": "buttons",
        "buttons": [
          "처음으로",
          "다시 등록하기",
          "취소하기"
        ]
      }
    }
    ----------------------------------------------------------------------------
    """
    try:
        rq = request.get_json()
        rp = nm.handle(rq)
        return json.dumps(rp)

    except Exception as e:
        response = {
            "message": {
                "text": "에러가 발생하였습니다: \n" + str(e)
            }
        }

        return json.dumps(response)

app.run(host = "0.0.0.0", debug = True)




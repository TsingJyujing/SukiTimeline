"""
利用微信上传图片，但是还不能编辑图片
"""
import json
import itchat
import requests
from itchat.content import *
import traceback

# post_url = "http://127.0.0.1:8000/image/upload/"
post_url = "http://127.0.0.1:8086/image/upload/"


@itchat.msg_register([PICTURE])
def download_files(msg):
    try:
        if msg["User"]["NickName"] in {"袁逸凡", "张蓓"}:
            msg.download(msg.fileName)
            with open(msg.fileName, "rb") as fp:
                resp = requests.post(post_url, files={'file': fp}).content
                result = json.loads(
                    resp.decode()
                )
                if result["status"] == "success":
                    return "上传成功，图片ID：%s" % result["image_id"]
                else:
                    raise Exception("上传失败！返回信息：" + json.dumps(result, indent=2))
    except Exception as ex:
        print(traceback.format_exc())
        return str(ex)
    return None


def main():
    itchat.auto_login(True)
    itchat.run(True)


if __name__ == '__main__':
    main()

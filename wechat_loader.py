"""
利用微信上传图片，但是还不能编辑图片
"""
import os
import time
import json
import itchat
import requests
from itchat.content import *
import traceback

post_url = "http://127.0.0.1:8086/image/upload/unsafe"

# 只允许昵称在SET内的用户上传照片
allowed_nickname = {"袁逸凡", "张蓓"}


@itchat.msg_register([PICTURE])
def download_files(msg):
    try:
        if msg["User"]["NickName"] in allowed_nickname:
            filename = os.path.join("wechat_files", msg.fileName)
            msg.download(filename)
            with open(filename, "rb") as fp:
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
    print("Starting to do authentication.")
    itchat.auto_login(True, enableCmdQR=2)
    print("Authorized.")
    itchat.run(True)


if __name__ == '__main__':
    while True:
        try:
            main()
        except:
            print("Error while running WechatAutoReply.")
            print(traceback.format_exc())
        finally:
            time.sleep(2)

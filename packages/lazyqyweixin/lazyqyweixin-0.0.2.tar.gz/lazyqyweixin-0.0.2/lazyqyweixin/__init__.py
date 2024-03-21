from lazysdk import lazyrequests
from Crypto.Cipher import AES
import xml.dom.minidom
import showlog
import chardet
import hashlib
import base64
import socket
import struct
from . import internal_app


def get_sha1(token, timestamp, nonce, encrypt):
    """用SHA1算法生成安全签名
    @param token:  票据
    @param timestamp: 时间戳
    @param encrypt: 密文
    @param nonce: 随机字符串
    @return: 安全签名
    """
    sort_list = [token, timestamp, nonce, encrypt]
    sort_list.sort()
    sha = hashlib.sha1()
    sha.update("".join(sort_list).encode("utf-8"))
    return sha.hexdigest()


# 消息体签名校验
def check_signature(
        token: str,
        timestamp: str,
        nonce: str,
        echo_str: str,
        msg_signature: str
):
    """
    验证前面传来的签名
    :param token:
    :param timestamp:
    :param nonce:
    :param echo_str:
    :param msg_signature:
    :return:
    """
    signature = get_sha1(
        token=token,
        timestamp=timestamp,
        nonce=nonce,
        encrypt=echo_str
    )  # 计算签名以比对传过来的签名
    if msg_signature == signature:
        return True
    else:
        return False


def decrypt_msg(
        encoding_aes_key,
        encrypt
):
    """

    加解密库里，ReceiveId 在各个场景的含义不同：

    企业应用的回调，表示corpid
    第三方事件的回调，表示suiteid
    个人主体的第三方应用的回调，ReceiveId是一个空字符串
    :return:
    """
    res = dict()
    key = base64.b64decode(encoding_aes_key + "=")
    cryptor = AES.new(
        key=key,
        mode=AES.MODE_CBC,
        iv=key[:16])
    # 使用BASE64对密文进行解码，然后AES-CBC解密

    plain_text = cryptor.decrypt(base64.b64decode(encrypt))
    encoding = chardet.detect(plain_text).get("encoding")
    showlog.info(f'猜测编码：{encoding}')
    plain_text = plain_text.decode(encoding)
    res["decode_content"] = plain_text
    # print("plain_text",plain_text)

    pad = ord(plain_text[-1])
    # print("pad", pad)

    # 去除16位随机字符串
    content = plain_text[16:-pad]
    # print('content', content)
    try:
        msg_len = socket.ntohl(struct.unpack("I", content[: 4].encode('utf-8'))[0])
        msg = content[4: msg_len + 4]
        receive_id = content[msg_len + 4:]
        res["msg_len"] = msg_len
        res["msg"] = msg
        res["receive_id"] = receive_id
    except:
        pass
    return res


def make_response_str(
        msg_signature,
        timestamp,
        nonce,
        echo_str,
        token,
        encoding_aes_key
):
    """
    对接收到的消息进行校验，校验通过则解密，不通过则返回空
    :param msg_signature:
    :param timestamp:
    :param nonce:
    :param echo_str:
    :param token:
    :param encoding_aes_key:
    :return:
    """
    check_signature_res = check_signature(
        msg_signature=msg_signature,
        timestamp=timestamp,
        nonce=nonce,
        echo_str=echo_str,
        token=token
    )
    if check_signature_res:
        decrypt_msg_res = decrypt_msg(
            encoding_aes_key=encoding_aes_key,
            encrypt=echo_str
        )
        msg = decrypt_msg_res['msg']
        return msg
    else:
        return ''


def xml_to_dict(xml_string: str):
    """
    解析xml为dict
    :param xml_string:
    :return:
    """
    res = dict()
    # 加载XML文档
    dom = xml.dom.minidom.parseString(xml_string)
    root = dom.documentElement
    for each in root.childNodes:
        # print(each)
        # # 获取节点名
        # print(each.nodeName)
        # # 获取节点值
        # print(each.firstChild)
        if each.firstChild:
            res[each.nodeName] = each.firstChild.data
    return res


def get_permanent_code(
        suite_access_token: str,
        auth_code_value: str
):
    """
    获取永久授权码
    :return:
    """
    url = f"https://qyapi.weixin.qq.com/cgi-bin/service/get_permanent_code?suite_access_token={suite_access_token}"
    # params = {
    #     "suite_access_token": suite_access_token
    # }
    data = {
        "auth_code": auth_code_value
    }
    return lazyrequests.lazy_requests(
        method="POST",
        url=url,
        # params=params,
        json=data,
        return_json=True
    )


class WorkWeixin:
    def __init__(
            self,
            suite_id: str,
            suite_secret: str,
            token: str,
            encoding_aes_key: str
    ):
        self.suite_id = suite_id
        self.suite_secret = suite_secret
        self.token = token
        self.encoding_aes_key = encoding_aes_key

    def get_suite_access_token(self, suite_ticket: str):
        """
        获取suite_access_token
        :return:
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/service/get_suite_token"
        data = {
            "suite_id": self.suite_id,
            "suite_secret": self.suite_secret,
            "suite_ticket": suite_ticket
        }
        return lazyrequests.lazy_requests(
            method="POST",
            url=url,
            json=data,
            return_json=True
        )

    @staticmethod
    def external_contact_group_chat(
            access_token: str,
            cursor: str = None,
            limit: int = 10
    ):
        """
        获取客户群列表
        https://developer.work.weixin.qq.com/document/path/93414

        常见错误：
        701008：user list or group creater no license
        该userid没有激活互通账号，请激活后重试

        :return:
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/list"
        params = {"access_token": access_token}
        data = {
            "status_filter": 0,
            "owner_filter": {
                # "userid_list": ["abel"]
            },
            "cursor": cursor,
            "limit": limit
        }
        return lazyrequests.lazy_requests(
            method="POST",
            url=url,
            params=params,
            json=data,
            return_json=True
        )

    @staticmethod
    def service_get_corp_token(
            suite_access_token: str,
            auth_corp_id: str,
            permanent_code: str
    ):
        """
        获取企业凭证access_token
        https://developer.work.weixin.qq.com/document/path/90605
        :return:
        """
        url = "https://qyapi.weixin.qq.com/cgi-bin/service/get_corp_token"
        params = {"suite_access_token": suite_access_token}
        data = {
            "auth_corpid": auth_corp_id,  # 授权方corpid
            "permanent_code": permanent_code  # 永久授权码，通过get_permanent_code获取
        }
        return lazyrequests.lazy_requests(
            method="POST",
            url=url,
            params=params,
            json=data,
            return_json=True
        )


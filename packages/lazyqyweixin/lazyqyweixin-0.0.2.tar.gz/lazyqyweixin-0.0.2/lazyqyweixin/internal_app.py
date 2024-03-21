from lazysdk import lazyfile
from lazysdk import lazypath
import requests
import showlog
import json
import time
import os


class WorkWeixin:
    """
    企业微信应用
    """
    def __init__(
            self,
            corp_id: str,
            agent_id: int,
            secret: str
    ):
        """
        初始化
        :param corp_id: 企业id
        :param secret: 应用秘钥
        :param agent_id: 企业应用的id，整型。企业内部开发，可在应用的设置页面查看；第三方服务商，可通过接口 获取企业授权信息 获取该参数值
        """
        self.corp_id = corp_id
        self.secret = secret
        self.agent_id = agent_id
        self.cache_path = "cache_data"
        lazypath.make_path(self.cache_path)
        self.access_token = self.get_token()

    def get_token(
            self
    ):
        """
        获取access_token
        文档：https://developer.work.weixin.qq.com/document/path/91039

        access_token的有效期通过返回的expires_in来传达，正常情况下为7200秒（2小时），有效期内重复获取返回相同结果，过期后获取会返回新的access_token。
        由于企业微信每个应用的access_token是彼此独立的，所以进行缓存时需要区分应用来进行存储。
        access_token至少保留512字节的存储空间。
        企业微信可能会出于运营需要，提前使access_token失效，开发者应实现access_token失效时重新获取的逻辑。

        :return:
            {
                'errcode': 0,
                'errmsg': 'ok',
                'access_token': 'token内容',
                'expires_in': 7200
            }
            参数	说明
            errcode	出错返回码，为0表示成功，非0表示调用失败
            errmsg	返回码提示语
            access_token	获取到的凭证，最长为512字节
            expires_in	凭证的有效时间（秒）
        """
        method = 'GET'
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        params = {
            "corpid": self.corp_id,
            "corpsecret": self.secret
        }
        # 尝试使用本地缓存
        token_file = os.path.join(self.cache_path, f'token_{self.secret}.json')
        try:
            local_file = lazyfile.read(file=token_file, json_auto=True)
            if local_file:
                expires_ts = local_file.get('expires_ts')
                if expires_ts > time.time():
                    return local_file.get('access_token')
                else:
                    pass
            else:
                pass
        except FileNotFoundError:
            pass
        # 尝试使用本地缓存
        showlog.info('未获取到本地缓存，将获取最新token...')
        response = requests.request(
            method=method,
            url=url,
            params=params
        )
        response_json = response.json()
        errcode = response_json.get('errcode')
        if errcode != 0:
            showlog.warning(response_json)
            return
        else:
            access_token = response_json.get('access_token')

            if access_token:
                expires_in = response_json.get('expires_in')
                expires_ts = time.time() + expires_in - 100
                response_json['expires_ts'] = expires_ts
                lazyfile.save(
                    file=token_file,
                    content=json.dumps(response_json)
                )
                return access_token
            else:
                return

    def refresh_token(self):
        """
        刷新access_token
        :return:
        """
        self.access_token = self.get_token()

    def get_user_id_list(
            self,
            cursor: str = None,
            limit: int = 10000
    ):
        """

        :param cursor:
        :param limit:
        :return:
        """
        method = "POST"
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/list_id?access_token={self.access_token}'
        post_json = {
            "limit": limit
        }
        if cursor:
            post_json['cursor'] = cursor
        response = requests.request(
            method=method,
            url=url,
            json=post_json

        )
        return response.json()

    def get_user_info(
            self,
            user_id: str = None
    ):
        """

        :param user_id:
        :return:
        """
        file = os.path.join(self.cache_path, f'user_info_{user_id}.json')
        if os.path.exists(file):
            showlog.info('已有本地缓存')
            response_json = lazyfile.read(file=file, json_auto=True)
        else:
            showlog.info('无缓存，将获取')
            method = "GET"
            url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.access_token}&userid={user_id}'
            response = requests.request(
                method=method,
                url=url
            )
            response_json = response.json()
            lazyfile.save(
                file=file,
                content=json.dumps(response_json, ensure_ascii=False)
            )
        return response_json

    def chat_group_create(
            self,
            name,
            owner,
            user_list,
            chat_id=None
    ):
        """
        创建群聊会话
        https://developer.work.weixin.qq.com/document/path/90245
        :param name:
        :param owner: 指定群主的id。如果不指定，系统会随机从userlist中选一人作为群主
        :param user_list:
        :param chat_id: 群聊的唯一标志，不能与已有的群重复；字符串类型，最长32个字符。只允许字符0-9及字母a-zA-Z。如果不填，系统会随机生成群id
        :return:
        """
        method = 'POST'
        url = f'https://qyapi.weixin.qq.com/cgi-bin/appchat/create?access_token={self.access_token}'
        request_json = {
            "name": name,  # 群聊名，最多50个utf8字符，超过将截断
            "userlist": user_list,  # 群成员id列表。至少2人，至多2000人
        }
        if owner:
            request_json['owner'] = owner
        if chat_id:
            request_json['chatid'] = chat_id
        response = requests.request(
            method=method,
            url=url,
            json=request_json
        )
        return response.json()

    def chat_group_send(
            self,
            chat_id,
            msg_type: str = 'text',
            content: str = '[烟花]'
    ):
        """
        应用推送消息
        https://developer.work.weixin.qq.com/document/path/90248
        :param name:
        :param owner: 指定群主的id。如果不指定，系统会随机从userlist中选一人作为群主
        :param user_list:
        :param chat_id: 群聊的唯一标志，不能与已有的群重复；字符串类型，最长32个字符。只允许字符0-9及字母a-zA-Z。如果不填，系统会随机生成群id
        :return:
        """
        method = 'POST'
        url = f'https://qyapi.weixin.qq.com/cgi-bin/appchat/send?access_token={self.access_token}'
        request_json = {
            "chatid": chat_id,
            "msgtype": msg_type,
            "text": {
                "content": content
            },
            "safe": 0
        }  # 文本消息
        response = requests.request(
            method=method,
            url=url,
            json=request_json
        )
        return response.json()

    def send_message(
            self,
            to_user: list = None,
            to_party: list = None,
            to_tag: list = None,
            msg_type: str = 'text',
            content: str = '[烟花] this is a test message:)',
            safe: int = 0,
            enable_id_trans: int = 0,
            enable_duplicate_check: int = 0,
            duplicate_check_interval: int = 1800
    ):
        """
        发送消息
        文档：https://developer.work.weixin.qq.com/document/path/90236

        :param to_user: 指定接收消息的成员，成员ID列表（多个接收者用‘|’分隔，最多支持1000个）。特殊情况：指定为"@all"，则向该企业应用的全部成员发送
        :param to_party: 指定接收消息的部门，部门ID列表，多个接收者用‘|’分隔，最多支持100个。当touser为"@all"时忽略本参数
        :param to_tag: 指定接收消息的标签，标签ID列表，多个接收者用‘|’分隔，最多支持100个。当touser为"@all"时忽略本参数
        :param msg_type: 消息类型，此时固定为：text
        :param content: 消息内容，最长不超过2048个字节，超过将截断（支持id转译）
        :param safe: 表示是否是保密消息，0表示可对外分享，1表示不能分享且内容显示水印，默认为0
        :param enable_id_trans: 表示是否开启id转译，0表示否，1表示是，默认0。仅第三方应用需要用到，企业自建应用可以忽略。
        :param enable_duplicate_check: 表示是否开启重复消息检查，0表示否，1表示是，默认0
        :param duplicate_check_interval: 表示是否重复消息检查的时间间隔，默认1800s，最大不超过4小时

        :return:
        """
        method = 'POST'
        url = f'https://qyapi.weixin.qq.com/cgi-bin/message/send'
        request_json = {
           "msgtype": msg_type,
           "agentid": self.agent_id,
           "text": {
               "content": content
           }
        }  # 文本消息
        if to_user:
            request_json["touser"] = "|".join(to_user)
        if to_party:
            request_json["toparty"] = "|".join(to_party)
        if to_tag:
            request_json["totag"] = "|".join(to_tag)
        if safe:
            request_json["safe"] = safe
        if enable_id_trans:
            request_json["enable_id_trans"] = enable_id_trans
        if enable_duplicate_check:
            request_json["enable_duplicate_check"] = enable_duplicate_check
        if duplicate_check_interval:
            request_json["duplicate_check_interval"] = duplicate_check_interval

        params = {"access_token": self.access_token}  # token参数
        response = requests.request(
            method=method,
            url=url,
            json=request_json,
            params=params
        )
        return response.json()

    def department(
            self,
            user_id=None,
            access_token=None
    ):
        """
        获取部门列表
        文档：https://developer.work.weixin.qq.com/document/path/90208

        :return:
        """
        method = 'GET'
        url = f'https://qyapi.weixin.qq.com/cgi-bin/department/list'
        print(self.access_token)
        if not access_token:
            params = {"access_token": self.access_token}
        else:
            params = {"access_token": access_token}
        if user_id:
            params["id"] = user_id
        response = requests.request(
            method=method,
            url=url,
            params=params
        )
        return response.json()

    def department_users(
            self,
            department_id
    ):
        """
        获取部门成员
        文档：https://developer.work.weixin.qq.com/document/path/90200

        :return:
        """
        method = 'GET'
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/simplelist'
        params = {"access_token": self.access_token}
        if department_id:
            params["department_id"] = department_id
        response = requests.request(
            method=method,
            url=url,
            params=params
        )
        return response.json()

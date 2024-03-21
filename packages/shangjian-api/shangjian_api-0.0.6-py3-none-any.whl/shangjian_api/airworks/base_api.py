# coding:utf8
import json
import time
import requests
from json import JSONDecodeError
from urllib import parse
from . import settings
import urllib3
from urllib3.util.ssl_ import create_urllib3_context
from requests.adapters import HTTPAdapter
TOP_PACKAGE = settings.TOP_PACKAGE

class CustomSslContextHttpAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        ctx = create_urllib3_context()
        ctx.load_default_certs()
        ctx.options |= 0x4  # ssl.OP_LEGACY_SERVER_CONNECT
        self.poolmanager = urllib3.PoolManager(ssl_context=ctx)

class ApiError(Exception):
    def __init__(self, error_code, error_msg):
        self.error_code = error_code
        self.error_msg = error_msg

    def __str__(self):
        return f"ErrorCode: {self.error_code}, ErrorMsg: {self.error_msg}"


class ApiResponse:
    def __init__(self, api: "BaseApi"):
        self.api = api


class BaseApi:
    def __init__(
        self,
        base_url="",
        access_key="",
        access_secret="",
        app_url="",
        app_method="get",
        token_api="api_gateway/auth/get_token",
        **kwargs,
    ):
        self.base_url = base_url
        self.access_key = access_key
        self.access_secret = access_secret
        #
        self._check_local_config()
        #
        self.app_method = app_method
        self.app_url = app_url
        self.token_api = token_api
        #
        self.token_str = ""
        self.token_expired_time = 0

        self.session = requests.Session()
        self.session.mount("https://rds.csc.com.cn", CustomSslContextHttpAdapter())

    def close(self):
        self.session.close()
        return

    def _check_local_config(self):
        self.base_url = self.base_url or settings.BASE_URL
        self.access_key = self.access_key or settings.ACCESS_KEY
        self.access_secret = self.access_secret or settings.ACCESS_SECRET

        if not all([self.base_url, self.access_key, self.access_secret]):
            raise TOP_PACKAGE.exceptions.NoConfigError
        return

    @staticmethod
    def to_response(response):
        try:
            json_response = json.loads(response)
        except JSONDecodeError:
            raise ApiError(error_code=30000, error_msg="json解析错误")
        if json_response.get("error_code") != 0:
            raise ApiError(
                error_code=json_response["error_code"],
                error_msg=json_response.get("error_message"),
            )
        return json_response

    def request(self, method, app_url, **kwargs):
        # 兼容不加schema的情况 以及用户可指定为https等
        url = f"{self.base_url}/{app_url}"
        if not url.startswith("http"):
            url = f"http://{url}"
        #
        r = self.session.request(method, url, **kwargs)
        r.close()
        return self.to_response(r.text)

    def get(self, url, params):
        query_string = parse.urlencode(params)
        return self.request("GET", f"{url}?{query_string}")

    def post(self, url, data):
        return self.request("POST", url, data=data)

    def refresh_token(self):
        token_response = self.post(
            self.token_api,
            {
                "access_key": self.access_key,
                "access_secret": self.access_secret,
            },
        ).get("data")
        self.token_str = token_response.get("token")
        self.token_expired_time = token_response.get("expire_time")

    def _api_response(self, token_update=True, **kwargs):
        #
        app_url = kwargs.get("app_url", self.app_url)
        app_method = kwargs.get("api_method", self.app_method)
        if not self.token_str or time.time() > self.token_expired_time:
            self.refresh_token()
        try:
            kwargs["token"] = self.token_str
            if app_method.lower() == "get":
                json_response = self.get(app_url, kwargs)
            elif app_method.lower() == "post":
                json_response = self.post(app_url, kwargs)
            else:
                raise ApiError(error_code=30001, error_msg="目前仅支持post和get的接口")
        except ApiError as e:
            if token_update and e.error_code == 40002:
                return self._api_response(token_update=False, **kwargs)
            else:
                raise e
        return json_response

    def api_response(self, **kwargs):
        return self._api_response(**kwargs)

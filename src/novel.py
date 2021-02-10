from typing import List

import requests
from bs4 import BeautifulSoup
import copy

from src.user import SelfUser
from src.utils import fastRegex
from tenacity import retry, stop_after_attempt, retry_if_exception_type
from urllib3.exceptions import ConnectionError, ProtocolError
from requests.exceptions import ConnectionError as CE


class Novel:
    id: int
    title: str
    author: str
    library: str
    status: str
    totalWords: int
    briefIntroduction: str
    copyright: bool
    volumeList: List[dict]

    @classmethod
    @retry(stop=stop_after_attempt(3), retry=retry_if_exception_type(ConnectionError))
    @retry(stop=stop_after_attempt(3), retry=retry_if_exception_type(ProtocolError))
    @retry(stop=stop_after_attempt(3), retry=retry_if_exception_type(CE))
    @retry(stop=stop_after_attempt(3), retry=retry_if_exception_type(TimeoutError))
    def __init__(cls, articleid: int):
        main_page = BeautifulSoup(
            requests.get(f"http://www.wenku8.net/wap/article/articleinfo.php?id={articleid}").text,
            features="html.parser")
        main_web_content = main_page.text
        cls.id = articleid
        cls.title = fastRegex(r"新书\n(.*)", main_web_content)
        cls.author = fastRegex(r"作者:(\w*)", main_web_content)
        cls.library = fastRegex(r"类别:(\w*)", main_web_content)
        cls.status = fastRegex(r"状态:(\w*)", main_web_content)
        cls.copyright = True if main_web_content.find("版权问题") == -1 else False
        if cls.copyright:
            cls.totalWords = int(fastRegex(r"字数:(\d*)", main_web_content))
        cls.briefIntroduction = fastRegex(r"\[作品简介\]([\s\S]*)联系管理员", main_web_content)
        cls.cover = main_page.find("img")["src"]
        read_page_request = requests.get(
            f"https://www.wenku8.net/novel/{2 if cls.status == '连载中' else 0}/{articleid}/index.htm",
            cookies=SelfUser.cookies)
        read_page_request.encoding = "gbk"
        read_page = BeautifulSoup(read_page_request.text,
                                  features="html.parser")
        tags = read_page.find_all("td")
        volumeList = []
        for i in tags:
            if i["class"][0] == "vcss":
                volumeList.append({"name": str(i.string), "chapters": []})
            elif i["class"][0] == "ccss" and i.string != "\xa0":
                volumeList[len(volumeList) - 1]["chapters"].append({"name": str(i.string), "cid": int(i.a["href"].replace(".htm", ""))})
        cls.volumeList = volumeList


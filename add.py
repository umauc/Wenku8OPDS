import json
from multiprocessing.dummy import freeze_support

from local_settings import WENKU8_PASSWD, WENKU8_USERNAME
from src.novel import Novel
from src.user import SelfUser


print("Adding Wenku8's Novels into data.json")
print("It may take a long time...")

novel_list = []
novel_dict_list = []

self_user = SelfUser(WENKU8_USERNAME, WENKU8_PASSWD)


def add(i):
    if __name__ == '__main__':
        try:
            if i != 0:
                novel = Novel(i)
                novel_list.append(novel)
                novel_dict = {"book_path": f"https://wenku8.herokuapp.com/get/{novel.id}", "cover_path": novel.cover,
                              "a_title": novel.title, "a_author": novel.author, "a_status": novel.status,
                              "a_summary": novel.briefIntroduction, "tags": ""}
                novel_dict_list.append(novel_dict)
                return f"Added {novel.title}[{novel.id}]"
        except ValueError:
            pass


if __name__ == '__main__':
    freeze_support()
    for i in range(3500):
        add(i)
    json.dump(novel_dict_list, open("data.json", "w+"))

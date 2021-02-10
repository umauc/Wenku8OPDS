import json

from local_settings import WENKU8_PASSWD, WENKU8_USERNAME

from src.novel import Novel
from src.user import SelfUser

print("Adding Wenku8's Novels into data.json")
print("It may take a long time...")

self_user = SelfUser(WENKU8_USERNAME, WENKU8_PASSWD)


def get_novel(number):
    novel = Novel(number)
    print(f"Added {novel.title}[{novel.id}]")
    novel_dict = {"book_path": f"https://wenku8.herokuapp.com/get/{novel.id}", "cover_path": novel.cover,
                  "a_title": novel.title, "a_author": novel.author, "a_status": novel.status,
                  "a_summary": novel.briefIntroduction, "tags": ""}
    return novel_dict


if __name__ == '__main__':
    novel_list = []
    for i in range(1, 3000):
        try:
            novel_list.append(get_novel(i))
        except AssertionError:
            pass
    json.dump(novel_list, open("data.json", "w+"))

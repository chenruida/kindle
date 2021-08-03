from ClippingsParser import main
import requests

TOKEN = 'secret_GbMfRy93ceKE02ZMlKkVeIfefiSlJDaP1pGq8Ie3Wgt'


def up_databases(title, author, page, text):
    body = {
        "parent": {
            "type": "database_id",
            "database_id": "681a5248-72c2-45b4-9ff6-332c7dda4f4c"
        },
        "title": [
            {
                "type": "text",
                "text": {
                    "content": "书摘",
                }
            }
        ],
        "properties": {
            "标题": {"title": [{"type": "text", "text": {"content": title}}]},
            "页码": {"rich_text": [{"type": "text", "text": {"content": page}}]},
            "作者": {"rich_text": [{"type": "text", "text": {"content": author}}]},
            "内容": {"rich_text": [{"type": "text", "text": {"content": text}}]},
        }
    }
    r = requests.request(
        "POST",
        "https://api.notion.com/v1/pages",  # 字符串为页面id
        json=body,
        headers={"Authorization": "Bearer " + TOKEN,
                 "Notion-Version": "2021-05-13",
                 "Content-Type": "application/json"}
    )
    return r


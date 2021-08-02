from ClippingsParser import main
import requests

TOKEN = 'secret_GbMfRy93ceKE02ZMlKkVeIfefiSlJDaP1pGq8Ie3Wgt'


def create_database(databaseName):
    body = {
        "parent": {
            "type": "page_id",
            "page_id": "024521c1-5030-4a91-ab71-1de6d5cbf20a"
        },
        "title": [
            {
                "type": "text",
                "text": {
                    "content": databaseName,
                }
            }
        ],
        "properties": {
            "Page": {
                "title": [{"type": "text", "text": {"content": "滴滴快车"}}]
            },
            "Content": {
                "rich_text": {[{"text": {"content": "支付宝"}}]}
            }
        }
    }
    r = requests.request(
        "POST",
        "https://api.notion.com/v1/databases",  # 字符串为页面id
        json=body,
        headers={"Authorization": "Bearer " + TOKEN,
                 "Notion-Version": "2021-05-13",
                 "Content-Type": "application/json"}
    )
    return r


if __name__ == "__main__":
    r = upload()
    print(r.text)

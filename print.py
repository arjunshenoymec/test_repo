import json


RAW_JSON = '{"userId": 2, "id": 20, "title": "doloribus ad provident suscipit at", "body": "qui consequuntur ducimus possimus quisquam amet similique\\nsuscipit porro ipsam amet\\neos veritatis officiis exercitationem vel fugit aut necessitatibus totam\\nomnis rerum consequatur expedita quidem cumque explicabo"}'

data = json.loads(RAW_JSON)

print(f'id: {data["id"]}, title: {data["title"]}')
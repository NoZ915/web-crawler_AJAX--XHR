import json
import urllib.request as req

# 抓取Dcard哈利波特魔法覺醒看板的資料
url = "https://www.dcard.tw/service/api/v2/forums/harrypottermagicawakened/posts"

request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")  # 根據觀察，取得的資料為JSON格式

# 解析 JSON 格式的資料
data = json.loads(data)
i = 0
for key in data:
    cleanData = data[i]
    i += 1
    print(cleanData["title"])

#coding: utf-8
import json

json_str = """
{
    "id" : 90,
    "name" : "python",
    "url" : "http://www.v2ex.com/go/python",
    "title" : "Python",
    "title_alternative" : "Python",
    "topics" : 7646,
    "stars" : 4862,

        "header" : "这里讨论各种 Python 语言编程话题，也包括 Django，Tornado 等框架的讨论。这里是一个能够帮助你解决实际问题的地方。",


        "footer" : null,

    "created" : 1278683336,
    "avatar_mini" : "//v2ex.assets.uxengine.net/navatar/8613/985e/90_mini.png?m=1504080972",
    "avatar_normal" : "//v2ex.assets.uxengine.net/navatar/8613/985e/90_normal.png?m=1504080972",
    "avatar_large" : "//v2ex.assets.uxengine.net/navatar/8613/985e/90_large.png?m=1504080972"
}
"""
res = json.loads(json_str)

print(res['id']) # 90
print(res['name']) # python
print(res['url']) # http://www.v2ex.com/go/python
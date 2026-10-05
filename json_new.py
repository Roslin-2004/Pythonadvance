# import json
#
# f=open("sample3.json","r")
# content=json.load(f)
# print(content)
import json
data=[{"name":"arum","age":20},{"name":"ajun","age":23}]
f=open("data.json","w")
json.dump(data,f)
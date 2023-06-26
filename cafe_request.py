



import requests
from datetime import datetime
session = requests.Session()


login_url = "https://nid.naver.com/nidlogin.login?url=http://section.cafe.naver.com"
login_data = {
    "id": "아이디",
    "pw": "비밀번호"
}
session.post(login_url, data=login_data)


cafe_url = "네이버카페주소"


response = session.get(cafe_url)
write_url = response.url + "/write"
response = session.get(write_url)
subject = u"제목"
content = u"내용"

data = {
    "subject": subject,
    "content": content,
    "clubid": "카페ID",
    "menuid": "메뉴ID",
    "boardtype": "글타입",
    "articleid": "글ID",
    "user_nick": "",
    "miming": "",
    "miming_opt": "",
    "isCommit": "true",
    "cafe_url": cafe_url,
    "cafe_hodu": "HIT",
    "clubcharset": "utf-8",
    "user_id": "아이디",
    "source": "",
    "callback": "",
    "extension": "jpg",
    "uploadFile": "",
    "event":"",
    "cafe_image": ""
}
response = session.post(write_url, data=data)
if response.status_code == 200:
    print("pass")
else:
    print("error")
response = session.get(response.url)
print(response.content)




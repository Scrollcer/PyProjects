import requests
from bs4 import BeautifulSoup

#Парсинг данных с сайта Skillbox.ru

skillbox = requests.get("https://live.skillbox.ru")
print(skillbox.status_code)
skillsoup = BeautifulSoup(skillbox.content)
webinars = skillsoup.findAll(class_ = "webinar-card__title")
[webinar.string.strip() for webinar in webinars]
webinar_full = skillsoup.findAll(class_ = "webinars__item")
for webinar in webinar_full:
    name = webinar.find(class_ = "webinar-card__title").string.strip()
    date = webinar.find(class_ = "webinar-card__date").string.strip()
    print(f'Вебинар "{name}" прошел {date} числа')
print()
#Парсинг данных с сайта Auto.ru

def fetch(url, params):
    headers = params["headers"]
    body = params["body"]
    method = params["method"]

    if method == "POST":
        return requests.post(url, headers = headers, data = body)
    if method == "GET":
        return requests.get(url, headers = headers)

car = fetch("https://auto.ru/-/ajax/desktop/listing/", {
  "headers": {
    "accept": "*/*",
    "accept-language": "en,ru;q=0.9,en-GB;q=0.8,en-US;q=0.7",
    "content-type": "application/json",
    "sec-ch-ua": "\" Not;A Brand\";v=\"99\", \"Microsoft Edge\";v=\"103\", \"Chromium\";v=\"103\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "same-origin",
    "sec-fetch-site": "same-origin",
    "x-client-app-version": "87.0.9727341",
    "x-client-date": "1658056767357",
    "x-csrf-token": "6dbdd4b09429dc668b64e0baa08dbff9de5a5cbebcd69c06",
    "x-page-request-id": "3c1d2d57f942d97dcba8ec4146e30c78",
    "x-requested-with": "XMLHttpRequest",
    "x-retpath-y": "https://auto.ru/chelyabinsk/cars/bmw/all/do-500000/",
    "x-yafp": "{\"a1\":\"BWTAeg==;0\",\"a2\":\"z7yj+GuiWLgPU451MVVY1a60HdNsQA==;1\",\"a3\":\"kgtBhouNTvIJ+ryjlnxYSw==;2\",\"a4\":\"ggEQMrqrplyyIIL4RYG+sWuVoN6nEfTqhOX8j6GiBGmI8w==;3\",\"a5\":\"gUaYVrG+LXwA6A==;4\",\"a6\":\"HMI=;5\",\"a7\":\"/NJtCtXB9kcXyg==;6\",\"a8\":\"GLwrF06i+98=;7\",\"a9\":\"VrI9cpuj39oJCg==;8\",\"b1\":\"gs870S3ivaA=;9\",\"b2\":\"8NPEjuDkV5N1Lw==;10\",\"b3\":\"YykhNhKbyOpCGg==;11\",\"b4\":\"XnlcHVbMTQ8=;12\",\"b5\":\"0Hmw+HEQ7ZCaAg==;13\",\"b6\":\"cbHpWSBFNgX5Ug==;14\",\"b7\":\"bsg68KCr+XLtrA==;15\",\"b8\":\"9JNX5ZC2KGs7MA==;16\",\"b9\":\"uCOFIzdezoHhjw==;17\",\"c1\":\"Q6QFTQ==;18\",\"c2\":\"K8F1fDnURndnk3tzEJjLfg==;19\",\"c3\":\"99zBfh8gXRyySRAZ8oqXfQ==;20\",\"c4\":\"v39RYnBHJOs=;21\",\"c5\":\"aG1dAg+EJww=;22\",\"c6\":\"41QZqA==;23\",\"c7\":\"4smjSu0AlgU=;24\",\"c8\":\"kIQ=;25\",\"c9\":\"BICXooyDljg=;26\",\"d1\":\"KFi6n51Pqzg=;27\",\"d2\":\"zP5D+g==;28\",\"d3\":\"S9Bjpc/iWJ4TUQ==;29\",\"d4\":\"jUKQkDiyeGs=;30\",\"d5\":\"gX3kHdVUyJc=;31\",\"d7\":\"TiHIceEoEZg=;32\",\"d8\":\"p4KeXJ9X1jgy3eLxra0md/KbzVYPEqiCkTU=;33\",\"d9\":\"lmIz4Ypq7Pk=;34\",\"e1\":\"R7IN9KgyVYKFXw==;35\",\"e2\":\"FUAhTqf4jq4=;36\",\"e3\":\"w3ifOql6vrs=;37\",\"e4\":\"umzODUs/Y5c=;38\",\"e5\":\"i/NmzL9vS8NdBg==;39\",\"e6\":\"rByl9hS+kP0=;40\",\"e7\":\"XO5wKWhGRwvaeA==;41\",\"e8\":\"fpkDQaFPeWU=;42\",\"e9\":\"j45DJyslbvo=;43\",\"f1\":\"pawG+i2f2JVmzg==;44\",\"f2\":\"4RY/HGzUkqI=;45\",\"f3\":\"IbhTrTWnSiliGg==;46\",\"f4\":\"xY1U0V7EYjI=;47\",\"f5\":\"dEW/Vooer9CRdg==;48\",\"f6\":\"BIacpe0WeF/SUw==;49\",\"f7\":\"l3zb2u2hIbL+SQ==;50\",\"f8\":\"J9OhFFqYltZ6sQ==;51\",\"f9\":\"O1w0VyrOz8E=;52\",\"g1\":\"Ta11NwHFePzp/A==;53\",\"g2\":\"XnIO2mhbfBUZFw==;54\",\"g3\":\"pVSjfnF64e0=;55\",\"g4\":\"RcGrMapUye43vQ==;56\",\"g5\":\"yO9SWmYu0q0=;57\",\"g6\":\"OpsM/kXrhlb+Jw==;58\",\"g7\":\"ndCz94Cp1z8=;59\",\"g8\":\"ms/xWEwn8CM=;60\",\"g9\":\"Se7jhWp9Ygo=;61\",\"h1\":\"k0pC0D1TENtfkA==;62\",\"h2\":\"dv2y3PgnENaRag==;63\",\"h3\":\"ZQlxs5lA3UHyGw==;64\",\"h4\":\"fFtwqlMxJGAe6w==;65\",\"h5\":\"gUoifbzPV88=;66\",\"h6\":\"2isolFJW0bA13w==;67\",\"h7\":\"4RB3ZXPZgiDWO7PkeBr122aXeKowLarN57isLU+AZ9zkX+pQ;68\",\"h8\":\"lnZGmsN4Xj1N9w==;69\",\"h9\":\"eznnGNUuhT60bw==;70\",\"i1\":\"v5zihEkb5fc=;71\",\"i2\":\"RXVRbDMvMyLtHA==;72\",\"i3\":\"6xqXbxWdoCb+TQ==;73\",\"i4\":\"LiaosEuFWi98PQ==;74\",\"i5\":\"ClG54HlfK7muVw==;75\",\"z1\":\"OLFSx8A9dsNVzb3Yy395KzbTNJt2uOWPi/LFe8xdTNb9bErveGZ4DhjSerjhiHiCL8WN2w0OaKg7ZV9NYobwkg==;76\",\"z2\":\"3lEw8WoRJoF4OuV5QLNGCKxSKSmawBbqE7DMHe5gastzb/0Glo2euVcNdRuN8n3I0eg5Ky/PGNHTaZvnZ29JKg==;77\",\"y2\":\"AZfc5WpijPk6fg==;78\",\"y3\":\"Ih1NPq+OJh3qBA==;79\",\"y6\":\"1t97VPlrQnyyNQ==;80\",\"y8\":\"xGS66293FyCsrQ==;81\",\"x4\":\"dAKVGttZbG6Qog==;82\",\"z4\":\"guyhhPXrYuS4cA==;83\",\"z6\":\"GEjVC95OgThz5OJC;84\",\"z7\":\"QoAYc7tZ0YtNZcbC;85\",\"z8\":\"98A+6uxTvlGiJ/rHkFg=;86\",\"z9\":\"fhQQxZu5X/jgm8d3;87\",\"y1\":\"CIqMqtquEU0p5276;88\",\"y4\":\"eU9qrx4HSNCoJtW/;89\",\"y5\":\"iXYpgpk1V/r9M/cvKhc=;90\",\"y7\":\"3DQeYnep7jj96y6V;91\",\"y9\":\"iiui6NRZ9vGUD3EtbZY=;92\",\"y10\":\"kYez6uZhM98vO2zPX68=;93\",\"x1\":\"YvxV7L60gST1P9AR;94\",\"x2\":\"Sbx41m33sRzMIGCpul0=;95\",\"x3\":\"/xTHPHD+UeKwFl+k;96\",\"x5\":\"6nmVVNqwgQANPudw;97\",\"z3\":\"B7aTnUN9gI1lx+nNlZBZEe+FEeu3DBlh+tpjTPSDLmE=;98\",\"z5\":\"1TAGuMX2UV8=;99\",\"v\":\"6.3.1\",\"pgrdt\":\"gJBqcXB6fDpbLWOT/cJxRbKSfKQ=;100\",\"pgrd\":\"uZOXsy4pL/KFNQK8c0ESreU1eZPbDVHOJOWaOIZofh4jDxXF4wSYWjOuWbZ0jjLK5P/luC9QzgrvNrvQVvf76b5BApJDXKMivpmfxBehY5cglVsRk8KVcMIATEc6YM9QQvuu4Gi0VDnhr9/IMf5wDyMzdywCKu3h4xAEqbpL+tn0+EGqEVtpwK4hDoz0EPqDaOXbZtfpXW9aOqTGn2HUrTbz/FY=\"}",
    "cookie": "_csrf_token=6dbdd4b09429dc668b64e0baa08dbff9de5a5cbebcd69c06; autoru_sid=a%3Ag62d3eed72v8qgnlg7tha3300gapbqac.a5f41b96e347d6efe90023ca31482e63%7C1658056407752.604800.ZPwF6zsVnxKoIDvGbBTfrw.pr2bu05eosUp-txEvZBF4xKIV1-dD58k3sjCbjAbzCY; autoruuid=g62d3eed72v8qgnlg7tha3300gapbqac.a5f41b96e347d6efe90023ca31482e63; suid=6745708372eee8e6e7e49cda03abdf2e.a56f2bd003c380a5b2a083d2a703edb0; from=morda; yuidlt=1; my=YwA%3D; _yasc=8Hp1ITc9WyUU9pv1sOykS3Xn5WSzCgb4bVylbMq5N1hVYN5i; sso_status=sso.passport.yandex.ru:synchronized_no_beacon; los=1; ys=wprid.1658056701749203-9579868280330453554-sas2-2338-sas-l7-balancer-8080-BAL-3428; from_lifetime=1658056764105; yandexuid=3392515611658056764; spravka=dD0xNjI2NTIwNzY0O2k9MTc2LjIyNi4xNjkuMjIzO0Q9NUEwNkRDOTdEODYyQzZCNDg0NUNFNEQ1M0I2RDIxRjJEMzRERjdBOTlDNTc4QkYyRTkzMDIyNkU4NjYxRDMxNDkxODJFNDVFO3U9MTYyNjUyMDc2NDczNDg0ODYyMjtoPTE1ZmRjYmQwMjljYTM1MWY2NDhmNTUwNTJkZTQ0NDc0",
    "Referer": "https://auto.ru/chelyabinsk/cars/bmw/all/do-500000/",
    "Referrer-Policy": "no-referrer-when-downgrade"
  },
  "body": "{\"price_to\":500000,\"catalog_filter\":[{\"mark\":\"BMW\"}],\"section\":\"all\",\"category\":\"cars\",\"output_type\":\"list\",\"geo_radius\":200,\"geo_id\":[56]}",
  "method": "POST"
});
car_data = car.json()
for offer in car_data["offers"]:
    print(f'{offer["vehicle_info"]["tech_param"]["human_name"]} Mileage: {offer["state"]["mileage"]}, Price: {offer["price_info"]["EUR"]}')

#Работа с selenium
import webbrowser
import time
from selenium import webdriver
edge_path="C:\Users\user\Downloads\edgedriver_win64\msedgedriver.exe"
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

webbrowser.get('edge').open("https://hh.ru/")
time.sleep(5)

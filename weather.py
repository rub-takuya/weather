import requests

city_name = input("都市名を入れてください:")
app_id = " "
#&units=metricで摂氏温度を求める
URL = "https://api.openweathermap.org/data/2.5/weather?q={0},jp&units=metric&lang=ja&appid={1}".format(city_name, app_id)

response = requests.get(URL)
data =  response.json()

#天気情報
weather = data["weather"][0]["description"]
#最高気温
temp_max = data["main"]["temp_max"]
#最低気温
temp_min = data["main"]["temp_min"]
#寒暖差
#小数点以下の指定の桁数で丸める round関数
diff_temp = round(temp_max - temp_min,2)
#湿度
humidity = data["main"]["humidity"]

context = {"天気": weather, "最高気温":str(temp_max) + "度", "最低気温": str(temp_min) + "度", "寒暖差": str(diff_temp) + "度", "湿度": str(humidity) + "%"}
print("--{0}'s Weather--".format(city_name))
for k, v in context.items():
    print("{0}:{1}".format(k, v))

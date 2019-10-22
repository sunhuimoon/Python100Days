import requests
import json


def main():
    #  这个例子使用了天行数据提供的国内新闻数据接口，其中的APIKey需要自己到该网站申请。
    resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
    data_model = json.loads(resp.text)
    for news in data_model['newslist']:
        print(news['title'])


if __name__ == '__main__':
    main()
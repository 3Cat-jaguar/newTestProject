from django.shortcuts import render
#from .models import post_table
from openapi.models import api_table
import requests


def parsing(request):
    date = str('2021-10-01')
    category = str(100)
    requesturl = "https://www.kamis.or.kr/service/price/xml.do?action=dailyPriceByCategoryList"
    requesturl += "&p_product_cls_code=01"
    requesturl += "&p_regday=" + date
    requesturl += "&p_convert_kg_yn=N"
    requesturl += "&p_item_category_code=" + category
    requesturl += "&p_cert_key=111"
    requesturl += "&p_cert_id=222"
    requesturl += "&p_returntype=json"
    print('request url : ' + str(requesturl))

    apidata = requests.get(requesturl)
    jsondata = apidata.json()
    for item in jsondata['data']['item']:
        item_name = item['item_name']
        #print(item_name + item['unit'])
        api_table.objects.create(category = category, item_name = item_name,
                                 kind_name = item['kind_name'], rank = item['rank'],
                                 unit = item['unit'], date = item['day1'],
                                 today_price = item['dpr1'], average_price = item['dpr7'])
    context = {
        'apidata':api_table.objects.all()
    }

    return render(request, 'index.html', context)


# def mainpage(request):
#     #posts = post_table.objects.all()
#     context = {
#         'apidata':api_table.objects.all()
#     }
#     #return render(request, 'index.html', {'posts':posts}})
#     return render(request, 'index.html', context)

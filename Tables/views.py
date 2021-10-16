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
        print(item_name + item['unit'])
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

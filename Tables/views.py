from django.shortcuts import render
#from .models import post_table
from openapi.models import api_table
import requests
import datetime
from datetime import datetime, date
from django.db.models import Q


def request_openapi_data(urldate, category):
    requesturl = "https://www.kamis.or.kr/service/price/xml.do?action=dailyPriceByCategoryList"
    requesturl += "&p_product_cls_code=01"
    requesturl += "&p_regday=" + urldate
    requesturl += "&p_convert_kg_yn=N"
    requesturl += "&p_item_category_code=" + category
    requesturl += "&p_cert_key=111"
    requesturl += "&p_cert_id=222"
    requesturl += "&p_returntype=json"
    print('request url : ' + str(requesturl))

    apidata = requests.get(requesturl)
    # request 실패시 처리를 어떻게 할지?
    jsondata = apidata.json()
    return jsondata


def create_db(urldate, i):
    category = str(i * 100)
    jsondata = request_openapi_data(urldate, category)
    for item in jsondata['data']['item']:
        # print(item_name + item['unit'])
        api_table.objects.create(category=category, item_name=item['item_name'],
                                 kind_name=item['kind_name'], rank=item['rank'],
                                 unit=item['unit'], date=urldate,
                                 today_price=item['dpr1'], average_price=item['dpr7'])
    return


# def update_db(urldate, i, index):
#     category = str(i * 100)
#     jsondata = request_openapi_data(urldate, category)
#     print(index)
#     for item in jsondata['data']['item']:
#         print(index)
#         objectslist = api_table.objects.filter(id=index)
#         if objectslist:
#             print('데이터를 수정합니다')
#             objects = objectslist.first()
#             objects.category = category
#             objects.item_name = item['item_name']
#             objects.kind_name = item['kind_name']
#             objects.rank = item['rank']
#             objects.unit = item['unit']
#             objects.date = item['day1']
#             if (item['dpr1'] != '-'):
#                 objects.today_price = item['dpr1']
#             elif (item['dpr2'] != '-'):
#                 objects.today_price = item['dpr2']
#             elif (item['dpr3'] != '-'):
#                 objects.today_price = item['dpr3']
#             elif (item['dpr4'] != '-'):
#                 objects.today_price = item['dpr4']
#             elif (item['dpr5'] != '-'):
#                 objects.today_price = item['dpr5']
#             else:
#                 objects.today_price = '-'
#             objects.average_price = item['dpr7']
#             objects.save()
#         else:
#             print('데이터를 추가합니다')
#             api_table.objects.create(category=category, item_name=item['item_name'],
#                                      kind_name=item['kind_name'], rank=item['rank'],
#                                      unit=item['unit'], date=item['day1'],
#                                      today_price=item['dpr1'], average_price=item['dpr7'])
#         index += 1
#     return index


def update_db(urldate, i):
    category = str(i * 100)
    jsondata = request_openapi_data(urldate, category)
    for item in jsondata['data']['item']:
        objectslist = api_table.objects.filter(item_name=item['item_name'], kind_name=item['kind_name'], rank=item['rank'])
        if objectslist:
            print('데이터를 수정합니다')
            objects = objectslist.first()
            if (item['dpr1'] != '-'):
                objects.today_price = item['dpr1']
                objects.date = urldate
            objects.average_price = item['dpr7']
            objects.save()
        elif item['dpr1'] != '-':
            print('데이터를 추가합니다')
            api_table.objects.create(category=category, item_name=item['item_name'],
                                     kind_name=item['kind_name'], rank=item['rank'],
                                     unit=item['unit'], date=urldate,
                                     today_price=item['dpr1'], average_price=item['dpr7'])
    return


def parsing(request):
    todayyear = datetime.now().year
    todaymonth = datetime.now().month
    todaydate = datetime.now().day
    todayweekday = str(date(todayyear, todaymonth, todaydate).strftime('%A'))
    print('today weekday : ' + todayweekday)
    urldate = str(todayyear) + '-' + str(todaymonth) + '-' + str(todaydate)
    print(urldate)
    if not api_table.objects.all().exists():
        i = 1
        while i < 5:
            create_db(urldate, i)
            i += 1
    elif (api_table.objects.filter(date=urldate).first() is None) and (todayweekday != 'Sunday'):
        # 일요일 외 nodata 가 나오는 다른 케이스도 찾아야함
        # index = api_table.objects.all().first().id
        i = 1
        while i < 5:
            # index = update_db(urldate, i, index)
            # update_db(urldate, i)
            create_db(urldate, i)
            i += 1
        # objectslist = api_table.objects.filter(id=index)
        # while objectslist:
        #     print('데이터 초기화')
        #     objects = objectslist.first()
        #     objects.category = 0
        #     objects.item_name = ''
        #     objects.kind_name = ''
        #     objects.rank = ''
        #     objects.unit = ''
        #     objects.date = ''
        #     objects.today_price = ''
        #     objects.average_price = ''
        #     objects.save()
        #     index += 1
        #     objectslist = api_table.objects.filter(id=index)
    context = {
        'apidata':api_table.objects.filter(Q(item_name__contains='캠벨') | Q(kind_name__contains='캠벨')).exclude(today_price='-').order_by('-date')
    }
    return render(request, 'index.html', context)


# def mainpage(request):
#     #posts = post_table.objects.all()
#     context = {
#         'apidata':api_table.objects.all()
#     }
#     #return render(request, 'index.html', {'posts':posts}})
#     return render(request, 'index.html', context)

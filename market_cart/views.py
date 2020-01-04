from typing import List

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json
import base64
from django.core.files.base import ContentFile

from watson_developer_cloud import VisualRecognitionV3
from io import BytesIO
import re

# Create your views here.

visual_recognition = VisualRecognitionV3(
    '2019-12-29',
    iam_apikey='of5nQEB24TQsRqgOE2Ms6eFDWxPHBfMim6CLc1LQj5lt')


def process_img(request):
    data = request.POST['image_data']
    _format, imgstr = data.split(';base64,')
    ext = _format.split('/')[-1]
    data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)  # You can save this as file instance.
    return data


def clear_(x):
    x.clear()




pro_dict = {"crunchy": 5.0, "indomie": 3.5, "bakerolls": 7.0, "m3mol": 4.5, "oreo": 2.0,
            "redbull": 25.0, "schwepps": 10.0, "tiger": 3.0, "wafer": 2.5, "fanta":5.5}

items = []
quantity = []
prices = []
total=0

@csrf_exempt
def cart(request):

    if request.method == 'POST' and 'image_data' in request.POST:
        img = process_img(request)
        classes = visual_recognition.classify(img, threshold='0.8',
                                              classifier_ids='Prod-Class_1015062714').get_result()
        res = classes['images'][0]["classifiers"][0]["classes"]
        if res:
            res=res[0]['class']
            if res in items:
                ind=items.index(res)
                quantity[ind] +=1
                prices[ind] = pro_dict[res] * quantity[ind]
            else:
                items.append(res)
                quantity.append(1)
                prices.append(pro_dict[res])
    elif request.method == 'POST' and 'reset' in request.POST:
        items.clear()
        quantity.clear()
        prices.clear()
        total=0

    _all = zip(items,quantity, prices)
    total = sum(prices)

    context_vars = {'all': _all, "total": total}

    return render(request, 'cart.html', context_vars)

from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from utils.pagination import Pagination
from datetime import datetime
from app01.helper import uid2pori

def check(request):
    pori = uid2pori(request.unicom_userid)

    count = models.Order.objects.filter(status=1,level=pori-1).count()
    queryset = models.Order.objects.filter( status=1,level= pori-1 ).order_by('status','-id')

    paper = Pagination(request, queryset.count())
    queryset = queryset[paper.start:paper.end]
    context = {
        "queryset": queryset,
        "paper_string": paper.html(),
        'count': count
    }

    return render(request, 'check.html', context)


def check_action(request, action, oid):
    if not action in [1, 2]:
        return HttpResponse("请求错误")
    pori = uid2pori(request.unicom_userid)
    print(oid)
    print(action)
    print(pori)


    ctime = datetime.now()
    if action != 1:
        models.Order.objects.filter(id=oid, status=1).update(status=3,update_datetime=ctime)
    else:
        row = models.Order.objects.filter(id=oid, status=1)
        print(row[0])
        if pori == 3:
            models.Order.objects.filter(id=oid, status=1).update(status=2,update_datetime=ctime)
        else:
            models.Order.objects.filter(id=oid, status=1).update(level = pori,update_datetime=ctime)


    return redirect('/check/')
import copy

from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from utils.pagination import Pagination
from datetime import datetime
from app01.helper import uid2pori,uid2depart
import pytz
utc=pytz.UTC

# count = models.Order.objects.filter(status=2).count()
# queryset = models.Order.objects.filter(status=2).order_by('status', '-id')


def deal(request):
    pori = uid2pori(request.unicom_userid)
    d_id = uid2depart(request.unicom_userid)

    count = models.Order.objects.filter(status=2).count()
    queryset = models.Order.objects.filter( status=2).order_by('-id')

    query_list = list(queryset.values())
    ctime = datetime.now()


    for i in range(0,count):
        beg_time=query_list[i]['update_datetime']
        ctime = ctime.replace(tzinfo=utc)
        beg_time = beg_time.replace(tzinfo=utc)
        if query_list[i]['rest_time']==0:
            continue

        diff = ctime - beg_time
        restime = 7-diff.days
        if restime<=0:
            restime=0

        if restime==0:
            models.Order.objects.filter(id=query_list[i]['id']).update(alarm =2,rest_time=0)
            delay = models.depart_kpi.objects.filter(dpart=d_id).values()
        elif restime<=2:
            models.Order.objects.filter(id=query_list[i]['id']).update(alarm =1,rest_time=restime)
        else:
            models.Order.objects.filter(id=query_list[i]['id']).update(rest_time=restime, alarm=0)
        print(diff.days)



    paper = Pagination(request, queryset.count())
    queryset = queryset[paper.start:paper.end]

    count1 = models.Helporder.objects.filter(status=1,support=d_id).count()
    queryset1 = models.Helporder.objects.filter(status=1,support=d_id).order_by('-id')

    paper1 = Pagination(request, queryset1.count())
    queryset1 = queryset1[paper1.start:paper1.end]





    context = {
        "queryset": queryset,
        "queryset1":queryset1,
        "paper_string": paper.html(),
        'count': count,
        'd_id':d_id
    }

    return render(request, 'deal.html', context)


def deal_action(request, action, oid):

    if not action in [1,2]:
        return HttpResponse("请求错误")
    ctime = datetime.now()
    if action == 1:
        pori = uid2pori(request.unicom_userid)


        models.Order.objects.filter(id=oid, status=2).update(status=4, update_datetime=ctime)
    elif action ==2:
        models.Helporder.objects.filter(id=oid, status=1).update(status=2, update_datetime=ctime)

    return redirect('/deal/')
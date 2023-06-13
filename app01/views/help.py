import copy

from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from utils.pagination import Pagination
from datetime import datetime
from app01.helper import uid2pori,uid2depart
from utils.bootstrapmodelform import BootStrapModelForm


# count = models.Order.objects.filter(status=2).count()
# queryset = models.Order.objects.filter(status=2).order_by('status', '-id')

class MyModalForm(BootStrapModelForm):
    class Meta:
        model = models.Helporder
        fields = [ 'submit','support','ord_id','mark']

def help(request):
    if request.method == "GET":
        form = MyModalForm()
    else:
        form = MyModalForm(data=request.POST)
        if form.is_valid():
            form.instance.create_datetime = datetime.now()
            form.save()
            form = MyModalForm()

    pori = uid2pori(request.unicom_userid)
    d_id = uid2depart(request.unicom_userid)


    count = models.Helporder.objects.filter(status=1,submit=d_id).count()
    queryset = models.Helporder.objects.filter(submit= d_id).order_by('-id')
    form = MyModalForm()


    paper = Pagination(request, queryset.count())
    queryset = queryset[paper.start:paper.end]
    context = {
        "queryset": queryset,
        "paper_string": paper.html(),
        'count': count,
        'd_id':d_id,
        'form':form
    }

    return render(request, 'help.html', context)




def help_action(request, action, oid):

    print(1111111111)
    if not action in [1]:
        return HttpResponse("请求错误")
    pori = uid2pori(request.unicom_userid)


    ctime = datetime.now()

    print(2111111111)
    models.Order.objects.filter(id=oid, status=2).update(status=4, update_datetime=ctime)



    return redirect('/help/')
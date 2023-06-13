from django.shortcuts import render, redirect
from app01 import models
from utils.pagination import Pagination
from utils.bootstrapmodelform import BootStrapModelForm
from datetime import datetime
from ..helper import uid2pori


def my(request):

    pori = uid2pori(request.unicom_userid)
    queryset = models.Order.objects.filter(user_id=request.unicom_userid).order_by('-id')

    paper = Pagination(request, queryset.count())
    queryset = queryset[paper.start:paper.end]
    context = {
        "queryset": queryset,
        "paper_string": paper.html(),
    }
    return render(request, 'my.html', context)


class MyModalForm(BootStrapModelForm):
    class Meta:
        model = models.Order
        fields = ['tpl', 'info']


def my_add(request):
    if request.method == "GET":
        form = MyModalForm()
        return render(request, 'my_add.html', {'form': form})

    form = MyModalForm(data=request.POST)
    if not form.is_valid():
        return render(request, "my_add.html", {'form': form})

    tpl_object = form.cleaned_data['tpl']
    form.instance.user_id = request.unicom_userid
    form.instance.leader_id = tpl_object.leader_id
    form.instance.create_datetime = datetime.now()
    form.save()
    return redirect('/my/')

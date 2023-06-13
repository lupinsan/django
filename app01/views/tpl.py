from django.shortcuts import render, redirect, HttpResponse
from app01 import models
from utils.pagination import Pagination
from utils.bootstrapmodelform import BootStrapModelForm
from django.http import JsonResponse


class TplModelForm(BootStrapModelForm):
    class Meta:
        model = models.Template
        fields = ["title", "leader", "dpart"]


def tpl(request):
    if request.method == "GET":
        form = TplModelForm()
    else:
        form = TplModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            form = TplModelForm()


    queryset = models.Template.objects.all().order_by('-id')

    paper = Pagination(request, queryset.count())
    queryset = queryset[paper.start:paper.end]
    context = {
        "queryset": queryset,
        "paper_string": paper.html(),
        "form": form
    }
    return render(request, 'tpl.html', context)


def tpl_edit(request, pk):
    tpl_object = models.Template.objects.filter(id=pk).first()
    if request.method == "GET":
        form = TplModelForm(instance=tpl_object)
    else:
        form = TplModelForm(instance=tpl_object, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/tpl/')

    queryset = models.Template.objects.all().order_by('-id')
    paper = Pagination(request, queryset.count())
    queryset = queryset[paper.start:paper.end]
    context = {
        "queryset": queryset,
        "paper_string": paper.html(),
        "form": form
    }
    return render(request, 'tpl.html', context)


def tpl_delete(request, pk):
    try:
        models.Template.objects.filter(id=pk).delete()
        return JsonResponse({"status": True})
    except Exception as e:
        return JsonResponse({"status": False})

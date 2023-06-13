from django.shortcuts import render, redirect
from app01 import models
from utils.pagination import Pagination
from utils.bootstrapmodelform import BootStrapModelForm
from datetime import datetime


def uid2pori(uid):

    row = models.UserInfo.objects.filter(id=uid).order_by('-id')
    d_id = row[0].dpart_id
    row1 = models.department.objects.filter(id=d_id).order_by('-id')
    return row1[0].d_pori

def uid2depart(uid):
    row = models.UserInfo.objects.filter(id=uid).order_by('-id')
    d_id = row[0].dpart_id
    return d_id
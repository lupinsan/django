from django.db import models


# Create your models here.

# 用户表
#need to----------------------------------------------修改用户

class UserInfo(models.Model):
    role_choices = (("user", "员工"), ("leader", "领导"),("operator","操作员"))

    role = models.CharField(verbose_name="角色", choices=role_choices, max_length=12)
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)
    dpart = models.ForeignKey(verbose_name='单位', to='department', on_delete=models.CASCADE, related_name='dparts', default=1)

    def __str__(self):
        return self.username



class department(models.Model):
    d_name = models.CharField(verbose_name='单位名称', max_length=32)
    d_pori = models.SmallIntegerField(verbose_name='级别', choices=((0,"操作单位"),(1, "提交单位"), (2, "权限单位1"), (3, "权限单位2")), default=1)

    def __str__(self):
        return self.d_name


# 模板表
class Template(models.Model):
    title = models.CharField(verbose_name='类别', max_length=32)
    mark = models.CharField(verbose_name='说明', max_length=32, default="")
    leader = models.ForeignKey(verbose_name='需要的审批者', to='UserInfo', on_delete=models.CASCADE)
    dpart = models.ForeignKey(verbose_name='处理部门', to='department', on_delete=models.CASCADE , default=1)

    def __str__(self):
        return self.title






class Order(models.Model):
    user = models.ForeignKey(verbose_name='发起者', to='UserInfo', on_delete=models.CASCADE, related_name='users')
    tpl = models.ForeignKey(verbose_name='模板', to='Template', on_delete=models.CASCADE, related_name='dpartments')
    leader = models.ForeignKey(verbose_name='审批者', to='UserInfo', on_delete=models.CASCADE, related_name='leaders')

    info = models.CharField(verbose_name='工单内容', max_length=128)

    status = models.SmallIntegerField(verbose_name='状态', choices=((1, "待审批"), (2, "通过未处理"), (3, "不通过"),(4,"处理完成")), default=1)
    level = models.SmallIntegerField(verbose_name='层级', choices=((0,"操作"),(1, "创建"), (2, "通过权限1"), (3, "通过权限2")), default=1)

    create_datetime = models.DateTimeField(verbose_name='创建时间')
    update_datetime = models.DateTimeField(verbose_name='审批时间', null=True, blank=True)
    rest_time = models.SmallIntegerField(verbose_name='剩余天数',default = 7)
    alarm = models.SmallIntegerField(verbose_name='预警状态',choices=((0,"无预警"),(1, "预警！"),(2,"超时！")),default = 0)


class Helporder(models.Model):
    ord_id= models.SmallIntegerField(verbose_name='工单号',default=1)
    mark = models.CharField(verbose_name='说明', max_length=32, default="")
    submit = models.ForeignKey(verbose_name='请求协作部门', to='department', on_delete=models.CASCADE, related_name='submit')
    support = models.ForeignKey(verbose_name='希望协作部门', to='department', on_delete=models.CASCADE, related_name='support')
    status = models.SmallIntegerField(verbose_name='状态',choices=((1, "待协作"),(2,"以完成协作")),default=1)
    create_datetime = models.DateTimeField(verbose_name='创建时间',null=True)
    update_datetime = models.DateTimeField(verbose_name='完成时间', null=True, blank=True)


class kpi(models.Model):
    operator = models.ForeignKey(verbose_name='操作员', to='UserInfo', on_delete=models.CASCADE, related_name='ops')
    workdeal = models.SmallIntegerField(verbose_name='完成工单数',default=0)
    helpdeal = models.SmallIntegerField(verbose_name='完成协助数',default=0)


class depart_kpi(models.Model):
    dpart = models.ForeignKey(verbose_name='处理部门', to='department', on_delete=models.CASCADE )
    workdeal = models.SmallIntegerField(verbose_name='部门完成工单数',default=0)
    delaydeal = models.SmallIntegerField(verbose_name='部门超时工单数',default=0)
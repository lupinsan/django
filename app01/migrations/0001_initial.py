# Generated by Django 4.2.2 on 2023-06-13 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="department",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("d_name", models.CharField(max_length=32, verbose_name="单位名称")),
                (
                    "d_pori",
                    models.SmallIntegerField(
                        choices=[(0, "操作单位"), (1, "提交单位"), (2, "权限单位1"), (3, "权限单位2")],
                        default=1,
                        verbose_name="级别",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[("user", "员工"), ("leader", "领导"), ("operator", "操作员")],
                        max_length=12,
                        verbose_name="角色",
                    ),
                ),
                ("username", models.CharField(max_length=32, verbose_name="用户名")),
                ("password", models.CharField(max_length=64, verbose_name="密码")),
                (
                    "dpart",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="dparts",
                        to="app01.department",
                        verbose_name="单位",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Template",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=32, verbose_name="类别")),
                (
                    "mark",
                    models.CharField(default="", max_length=32, verbose_name="说明"),
                ),
                (
                    "dpart",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app01.department",
                        verbose_name="处理部门",
                    ),
                ),
                (
                    "leader",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app01.userinfo",
                        verbose_name="需要的审批者",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("info", models.CharField(max_length=128, verbose_name="工单内容")),
                (
                    "status",
                    models.SmallIntegerField(
                        choices=[(1, "待审批"), (2, "通过未处理"), (3, "不通过"), (4, "处理完成")],
                        default=1,
                        verbose_name="状态",
                    ),
                ),
                (
                    "level",
                    models.SmallIntegerField(
                        choices=[(0, "操作"), (1, "创建"), (2, "通过权限1"), (3, "通过权限2")],
                        default=1,
                        verbose_name="层级",
                    ),
                ),
                ("create_datetime", models.DateTimeField(verbose_name="创建时间")),
                (
                    "update_datetime",
                    models.DateTimeField(blank=True, null=True, verbose_name="审批时间"),
                ),
                (
                    "leader",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="leaders",
                        to="app01.userinfo",
                        verbose_name="审批者",
                    ),
                ),
                (
                    "tpl",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="dpartments",
                        to="app01.template",
                        verbose_name="模板",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="users",
                        to="app01.userinfo",
                        verbose_name="发起者",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Helporder",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ord_id", models.SmallIntegerField(default=1, verbose_name="工单号")),
                (
                    "mark",
                    models.CharField(default="", max_length=32, verbose_name="说明"),
                ),
                (
                    "status",
                    models.SmallIntegerField(
                        choices=[(1, "待协作"), (2, "以完成协作")], default=1, verbose_name="状态"
                    ),
                ),
                (
                    "submit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="submit",
                        to="app01.department",
                        verbose_name="请求协作部门",
                    ),
                ),
                (
                    "support",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="support",
                        to="app01.department",
                        verbose_name="希望协作部门",
                    ),
                ),
            ],
        ),
    ]

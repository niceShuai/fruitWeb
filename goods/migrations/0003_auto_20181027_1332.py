# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-27 05:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20181025_2144'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goodsinfo',
            options={'verbose_name': '商品详细信息'},
        ),
        migrations.AlterModelOptions(
            name='goodstype',
            options={'verbose_name': '商品分类'},
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='click',
            field=models.IntegerField(verbose_name='点击量'),
        ),
    ]
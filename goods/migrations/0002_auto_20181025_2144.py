# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-25 13:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goodsinfo',
            options={'verbose_name': '商品详细信息', 'verbose_name_plural': '商品详细信息'},
        ),
        migrations.AlterModelOptions(
            name='goodstype',
            options={'verbose_name': '商品分类', 'verbose_name_plural': '商品分类'},
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='click',
            field=models.IntegerField(default=0, verbose_name='点击量'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsType', verbose_name='所属类别'),
        ),
    ]

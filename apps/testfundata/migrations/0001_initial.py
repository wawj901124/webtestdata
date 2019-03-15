# Generated by Django 2.0.5 on 2019-01-22 17:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pageelement', '0009_remove_eletestdata_modulepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_cookie', models.BooleanField(default=True)),
                ('select_option_text', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='select_option_text')),
                ('select_input_text', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='select_input_text')),
                ('colnum', models.CharField(default='0', max_length=100, verbose_name='colnum')),
                ('check_text', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='check_text')),
                ('add_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='添加时间')),
                ('modulepage', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pageelement.ModulePage', verbose_name='模块页面')),
                ('search_button_xpath', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pageelement.PageEle', verbose_name='search_button_xpath')),
                ('select_input_xpath', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='six', to='pageelement.PageEle', verbose_name='select_input_xpath')),
                ('select_option_xpath', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sox', to='pageelement.PageEle', verbose_name='select_option_xpath')),
            ],
            options={
                'verbose_name': '搜索测试数据',
                'verbose_name_plural': '搜索测试数据',
            },
        ),
    ]

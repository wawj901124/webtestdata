# Generated by Django 2.0.5 on 2019-01-21 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pageelement', '0005_auto_20190121_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eletestdatatype',
            name='modulepage',
        ),
        migrations.RemoveField(
            model_name='eletestdatatype',
            name='pageele',
        ),
        migrations.RemoveField(
            model_name='eletestdatatype',
            name='projectmodule',
        ),
        migrations.RemoveField(
            model_name='eletestdatatype',
            name='testproject',
        ),
        migrations.AlterField(
            model_name='eletestdatatype',
            name='test_data_type',
            field=models.CharField(default='', max_length=100, unique=True, verbose_name='测试数据类型'),
        ),
    ]

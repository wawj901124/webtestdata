# Generated by Django 2.0.5 on 2019-06-19 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inputtip', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputtipdata',
            name='inputtext',
            field=models.CharField(blank=True, default='', max_length=1500, null=True, verbose_name='输入框的输入内容'),
        ),
    ]

# Generated by Django 2.0.5 on 2019-05-30 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addactivity', '0004_auto_20190510_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='addactivity',
            name='hdlx',
            field=models.CharField(blank=True, default='', help_text='1表示选择拉新类型，2表示选择促活方式，3表示选择留存类型，4表示选择转化方式类型，5表示选择投诉补偿类型', max_length=100, null=True, verbose_name='输入活动类型的选项的内容'),
        ),
    ]

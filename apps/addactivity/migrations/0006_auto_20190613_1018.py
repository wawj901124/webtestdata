# Generated by Django 2.0.5 on 2019-06-13 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addactivity', '0005_addactivity_hdlx'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addactivity',
            name='tjrwxz',
            field=models.CharField(blank=True, default='', help_text='3表示选择用户活动参与次数', max_length=100, null=True, verbose_name='输入点击添加任务弹窗中的选项的内容'),
        ),
    ]
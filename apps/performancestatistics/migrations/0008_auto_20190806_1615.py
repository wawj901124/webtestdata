# Generated by Django 2.0.5 on 2019-08-06 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('performancestatistics', '0007_auto_20190806_1611'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meminfotestresult',
            old_name='licknextpageheapalloc',
            new_name='clicknextpageheapalloc',
        ),
        migrations.RenameField(
            model_name='meminfotestresult',
            old_name='licknextpageheapfree',
            new_name='clicknextpageheapfree',
        ),
        migrations.RenameField(
            model_name='meminfotestresult',
            old_name='licknextpageheapsize',
            new_name='clicknextpageheapsize',
        ),
        migrations.RenameField(
            model_name='meminfotestresult',
            old_name='licknextpageobjectsactivities',
            new_name='clicknextpageobjectsactivities',
        ),
        migrations.RenameField(
            model_name='meminfotestresult',
            old_name='licknextpageobjectsviews',
            new_name='clicknextpageobjectsviews',
        ),
        migrations.RenameField(
            model_name='meminfotestresult',
            old_name='licknextpagepsstotal',
            new_name='clicknextpagepsstotal',
        ),
    ]
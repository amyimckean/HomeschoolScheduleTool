# Generated by Django 3.2.3 on 2021-06-15 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeschoolTool', '0003_auto_20210615_2333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='studentName',
            new_name='studentFirstName',
        ),
        migrations.AddField(
            model_name='student',
            name='studentLastName',
            field=models.CharField(default='', max_length=50),
        ),
    ]

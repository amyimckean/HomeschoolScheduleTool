# Generated by Django 3.2.3 on 2021-08-15 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HomeschoolTool', '0003_alter_scheduleditem_recurtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduleditem',
            name='recurType',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HomeschoolTool.recurrencetype'),
        ),
    ]
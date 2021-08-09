# Generated by Django 3.2.3 on 2021-08-07 06:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HomeschoolTool', '0007_delete_userextended'),
    ]

    operations = [
        migrations.CreateModel(
            name='teacherClass',
            fields=[
                ('classID', models.AutoField(default='', primary_key=True, serialize=False)),
                ('className', models.CharField(default='', max_length=50)),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='scheduleditem',
            name='classT',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HomeschoolTool.teacherclass'),
        ),
    ]
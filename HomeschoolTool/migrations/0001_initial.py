# Generated by Django 3.2.3 on 2021-08-14 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='recurrenceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recurrenceTypeName', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='scheduleItemType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ScheduleItemTypeName', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjectName', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='teacherClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('className', models.CharField(default='', max_length=50)),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(default='', max_length=50)),
                ('lastName', models.CharField(default='', max_length=50)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='scheduledItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='', max_length=50)),
                ('details', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
                ('allDay', models.BooleanField(default=True)),
                ('recurEnd', models.DateTimeField(blank=True, null=True)),
                ('classT', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HomeschoolTool.teacherclass')),
                ('recurType', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HomeschoolTool.recurrencetype')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomeschoolTool.student')),
                ('subject', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='HomeschoolTool.subject')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomeschoolTool.scheduleitemtype')),
            ],
        ),
        migrations.CreateModel(
            name='completedItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('completedDate', models.DateTimeField(blank=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomeschoolTool.scheduleditem')),
            ],
        ),
    ]

# Generated by Django 3.2.3 on 2021-07-04 06:13

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
                ('recurrenceTypeID', models.AutoField(default='', primary_key=True, serialize=False)),
                ('recurrenceType', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='scheduleItemType',
            fields=[
                ('scheduleItemTypeID', models.AutoField(default='', primary_key=True, serialize=False)),
                ('ScheduleItemTypeName', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('studentID', models.AutoField(default='', primary_key=True, serialize=False)),
                ('studentFirstName', models.CharField(default='', max_length=50)),
                ('studentLastName', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='subject',
            fields=[
                ('subjectID', models.AutoField(default='', primary_key=True, serialize=False)),
                ('subjectName', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='scheduledItem',
            fields=[
                ('scheduledItemID', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(default='', max_length=50)),
                ('details', models.CharField(default='', max_length=255, null=True)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
                ('reoccurEnd', models.DateTimeField(blank=True, null=True)),
                ('reoccurType', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HomeschoolTool.recurrencetype')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HomeschoolTool.student')),
                ('subject', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='HomeschoolTool.subject')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
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

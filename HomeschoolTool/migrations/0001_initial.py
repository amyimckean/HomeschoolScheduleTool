# Generated by Django 3.2.3 on 2021-06-06 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='subject',
            fields=[
                ('subjectID', models.AutoField(default='', primary_key=True, serialize=False)),
                ('subjectName', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='week',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Time', models.CharField(default='', max_length=50)),
                ('Friday', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Friday', to='HomeschoolTool.subject')),
                ('Monday', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Monday', to='HomeschoolTool.subject')),
                ('Saturday', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Saturday', to='HomeschoolTool.subject')),
                ('Sunday', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Sunday', to='HomeschoolTool.subject')),
                ('Thursday', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Thursday', to='HomeschoolTool.subject')),
                ('Tuesday', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Tuesday', to='HomeschoolTool.subject')),
                ('Wednesday', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Wednesday', to='HomeschoolTool.subject')),
            ],
        ),
    ]

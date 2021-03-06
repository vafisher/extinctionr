# Generated by Django 2.2 on 2019-06-03 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('circles', '0013_auto_20190516_2054'),
    ]

    operations = [
        migrations.CreateModel(
            name='CircleJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('job', models.TextField(default='')),
                ('circle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='circles.Circle')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contacts.Contact')),
                ('filled', models.ForeignKey(help_text='Who will fill this job?', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='my_job_set', to='contacts.Contact')),
            ],
        ),
    ]

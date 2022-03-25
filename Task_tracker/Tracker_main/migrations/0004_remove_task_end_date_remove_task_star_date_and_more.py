# Generated by Django 4.0 on 2022-03-24 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker_main', '0003_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='task',
            name='star_date',
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Assigned', 'Assigned'), ('In_progress', 'In progress'), ('under_review', 'under review'), ('done', 'done')], default='Assigned', max_length=30),
        ),
    ]

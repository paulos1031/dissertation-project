# Generated by Django 3.0.4 on 2020-04-14 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='breached_tickets',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='calls_answered',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='chats_taken',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='counter_queries_taken',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='rank_position',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='tickets_closed',
            field=models.IntegerField(),
        ),
    ]

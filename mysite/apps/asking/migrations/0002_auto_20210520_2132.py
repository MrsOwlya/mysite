# Generated by Django 2.2.12 on 2021-05-20 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answerer_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asking.users'),
        ),
        migrations.AlterField(
            model_name='ask',
            name='asker_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asking.users'),
        ),
    ]

# Generated by Django 3.0.8 on 2021-10-26 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navbar1', '0005_auto_20211026_0243'),
    ]

    operations = [
        migrations.AddField(
            model_name='submitted_detail',
            name='match_key_id',
            field=models.IntegerField(default=0),
        ),
    ]

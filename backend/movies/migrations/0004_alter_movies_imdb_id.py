# Generated by Django 4.2.4 on 2023-11-18 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_people_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='imdb_id',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]

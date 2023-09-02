# Generated by Django 4.0 on 2023-04-28 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Curriculum', '0002_curriculum_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='curriculum',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='curriculum',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]

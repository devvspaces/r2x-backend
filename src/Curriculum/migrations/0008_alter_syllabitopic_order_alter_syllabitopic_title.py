# Generated by Django 4.0 on 2023-04-29 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Curriculum', '0007_alter_syllabitopic_slug_alter_syllabitopic_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='syllabitopic',
            name='order',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='syllabitopic',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]

# Generated by Django 4.0 on 2023-04-29 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Curriculum', '0006_alter_curriculum_slug_alter_curriculumsyllabi_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='syllabitopic',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='syllabitopic',
            name='title',
            field=models.CharField(editable=False, max_length=255),
        ),
    ]
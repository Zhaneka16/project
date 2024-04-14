# Generated by Django 4.0 on 2024-03-28 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Проект', 'verbose_name_plural': 'Проекты'},
        ),
        migrations.AlterModelOptions(
            name='projectphoto',
            options={'verbose_name': 'Фотографии проекта', 'verbose_name_plural': 'Фотографии проектов'},
        ),
        migrations.AlterField(
            model_name='projectphoto',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='main.project'),
        ),
    ]

# Generated by Django 4.0 on 2024-04-10 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_department_employee'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'Сотрудник', 'verbose_name_plural': 'Сотрудники'},
        ),
        migrations.RenameField(
            model_name='design_object',
            old_name='design_object_name',
            new_name='name',
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-25 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kuliah', '0003_auto_20160825_0454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jadwalkuliah',
            name='semester',
            field=models.CharField(choices=[('semester_1', 'Semester 1'), ('semester_2', 'Semester 2'), ('semester_3', 'Semester 3'), ('semester_4', 'Semester 4'), ('semester_5', 'Semester 5'), ('semester_6', 'Semester 6'), ('semester_7', 'Semester 7'), ('semester_8', 'Semester 8'), ('semester_9', 'Semester 9'), ('semester_10', 'Semester 10'), ('semester_11', 'Semester 11'), ('semester_12', 'Semester 12'), ('semester_pendek', 'Semester Pendek')], default='semester_1', max_length=50),
        ),
    ]

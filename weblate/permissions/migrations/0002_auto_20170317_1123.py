# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 10:23
from __future__ import unicode_literals

from django.db import migrations


def copy_groupacl(apps, schema_editor):
    existing = apps.get_model('trans', 'GroupACL').objects.all()
    GroupACL = apps.get_model('permissions', 'GroupACL')

    for item in existing.iterator():
        created = GroupACL.objects.create(
            language=item.language,
            project=item.project,
            subproject=item.subproject,
        )
        created.groups.add(*item.groups.all())


class Migration(migrations.Migration):

    dependencies = [
        ('permissions', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(copy_groupacl),
    ]

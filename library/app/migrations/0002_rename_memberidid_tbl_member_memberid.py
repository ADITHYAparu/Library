# Generated by Django 4.0.5 on 2022-10-04 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_member',
            old_name='memberidid',
            new_name='memberid',
        ),
    ]
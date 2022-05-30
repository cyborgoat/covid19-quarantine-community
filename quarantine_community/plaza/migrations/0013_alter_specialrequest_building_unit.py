# Generated by Django 4.0 on 2022-05-30 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plaza', '0012_alter_specialrequest_building_subunit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialrequest',
            name='building_unit',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='bu_special', to='plaza.buildingunit'),
            preserve_default=False,
        ),
    ]

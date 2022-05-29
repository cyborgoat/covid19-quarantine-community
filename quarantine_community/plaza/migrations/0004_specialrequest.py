# Generated by Django 4.0 on 2022-05-29 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('overview', '0004_covidbasicinfo_name'),
        ('plaza', '0003_alter_officialnotification_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=32)),
                ('body', models.TextField()),
                ('responder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responder', to='overview.user')),
            ],
        ),
    ]
# Generated by Django 4.2.6 on 2023-12-07 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('title', models.CharField(max_length=64)),
                ('birthday', models.DateField()),
                ('banned', models.BooleanField()),
                ('level', models.IntegerField()),
                ('profession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_8.profession')),
                ('rase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_8.race')),
            ],
        ),
    ]

# Generated by Django 3.0.5 on 2020-06-03 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(default='', max_length=25, unique=True)),
                ('nom', models.CharField(default='', max_length=25, unique=True)),
                ('password', models.CharField(default='', max_length=32, unique=True)),
            ],
        ),
    ]
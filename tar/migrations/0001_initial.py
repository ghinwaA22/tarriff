# Generated by Django 4.1 on 2022-08-29 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code1', models.CharField(max_length=2)),
                ('code2', models.CharField(max_length=2)),
                ('code3', models.CharField(max_length=2)),
                ('code4', models.CharField(max_length=2)),
                ('dach', models.CharField(max_length=4)),
                ('desc', models.TextField(max_length=200, verbose_name='Description')),
                ('tax', models.CharField(max_length=3)),
                ('unit', models.CharField(choices=[('num', 'number'), ('m2', 'square_meter'), ('m3', 'cube_meter'), ('kg', 'kilo_gram')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=200, verbose_name='Title')),
                ('note1', models.TextField(max_length=200, verbose_name='Note')),
                ('note2', models.TextField(max_length=200, verbose_name='Extra Note')),
                ('note3', models.TextField(max_length=200, verbose_name='Extra')),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=200, verbose_name='Title')),
                ('note1', models.TextField(max_length=200, verbose_name='Note')),
                ('note2', models.TextField(max_length=200, verbose_name='Extra Note')),
                ('note3', models.TextField(max_length=200, verbose_name='Extra')),
                ('section_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapters', to='tar.section')),
            ],
        ),
    ]
# Generated by Django 5.0.6 on 2024-06-25 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(default='', max_length=100)),
                ('contactnumber', models.CharField(default='', max_length=15)),
                ('address', models.CharField(default='', max_length=100)),
                ('gender', models.CharField(default='', max_length=20)),
                ('dateofbirth', models.CharField(default='', max_length=20)),
                ('qualification', models.CharField(default='', max_length=10)),
                ('username', models.CharField(default='', max_length=10)),
                ('password', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='tolldetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tollnumber', models.CharField(default='', max_length=10)),
                ('startpoint', models.CharField(default='', max_length=10)),
                ('endpoint', models.CharField(default='', max_length=10)),
                ('tickettype', models.CharField(default='', max_length=10)),
                ('cost', models.CharField(default='', max_length=10)),
            ],
        ),
    ]

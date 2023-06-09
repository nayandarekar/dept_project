# Generated by Django 4.2.1 on 2023-05-07 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_repositor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter Author Name', max_length=255)),
                ('description', models.CharField(help_text='Enter Author Description', max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.CharField(help_text='Enter Book Description', max_length=255),
        ),
    ]

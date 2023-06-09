# Generated by Django 4.2.1 on 2023-05-08 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_repositor', '0002_author_alter_book_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra_sauce', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_repositor.author')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_repositor.book')),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='book',
            field=models.ManyToManyField(through='book_repositor.BookAuthor', to='book_repositor.book'),
        ),
    ]

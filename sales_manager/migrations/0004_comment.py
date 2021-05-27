# Generated by Django 3.2.3 on 2021-05-26 15:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sales_manager', '0003_alter_book_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='sales_manager.book')),
                ('like', models.ManyToManyField(related_name='liked_comments', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(default=3, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

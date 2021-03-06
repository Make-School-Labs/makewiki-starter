# Generated by Django 3.0.2 on 2020-05-12 21:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wiki', '0002_auto_20191105_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title of your article.', max_length=600, unique=True)),
                ('slug', models.CharField(blank=True, editable=False, help_text='Unique URL path to access this article. Generated by the system.', max_length=600)),
                ('content', models.TextField(help_text='Write the content of your particleage here.')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='The date and time this article was created. Automatically generated when the model saves.')),
                ('modified', models.DateTimeField(auto_now=True, help_text='The date and time this article was updated. Automatically generated when the model updates.')),
                ('author', models.ForeignKey(help_text='The user that posted this article.', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Page',
        ),
    ]

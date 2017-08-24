from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
      ('blog', '0002_post_category'),
    ]

    operations = [
        migrations.CreateModel(
        name='Category',
        fields=[
        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        ('name', models.CharField(max_length=225)),
        ('slug', models.SlugField(max_length=100)),
        ],
    ),

        migrations.RemoveField(
            model_name='post',
            name='Category',
        ),

        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.Category'),
        ),
        ]

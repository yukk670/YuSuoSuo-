# Generated by Django 2.2 on 2019-07-12 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(0, '天赋树反馈'), (1, '视屏反馈'), (2, '字幕反馈'), (3, '回答反馈')], default=0, verbose_name='收藏类型')),
                ('type_id', models.IntegerField(verbose_name='收藏的类型id')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(db_index=1, max_length=30, unique=1, verbose_name='用户名')),
                ('password', models.CharField(max_length=128, verbose_name='密码')),
                ('nickname', models.CharField(max_length=30, null=1, verbose_name='昵称')),
                ('smajor', models.IntegerField(choices=[(0, '计算机科学与技术')], default=0, verbose_name='专业')),
                ('coin', models.IntegerField(default=50, verbose_name='梭梭币')),
                ('exp', models.IntegerField(default=0, verbose_name='总经验值')),
                ('email', models.EmailField(blank=1, max_length=64, null=1, unique=1, verbose_name='邮箱地址')),
                ('image', models.ImageField(default='image/default.png', max_length=128, upload_to='image/%Y/%m')),
                ('is_active', models.BooleanField(default=False, verbose_name='是否激活')),
                ('is_ban', models.BooleanField(default=False, verbose_name='是否禁用')),
                ('attention_user', models.ManyToManyField(blank=1, related_name='attention', to='user.User')),
                ('fav_video', models.ManyToManyField(blank=1, to='base.Video', verbose_name='关注视频')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户表',
            },
        ),
    ]

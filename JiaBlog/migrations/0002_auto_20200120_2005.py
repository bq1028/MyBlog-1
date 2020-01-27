# Generated by Django 2.1.7 on 2020-01-20 20:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('JiaBlog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('area_id', models.CharField(max_length=10)),
                ('area_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleBodyPic',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('article_id', models.CharField(blank=True, max_length=20, null=True)),
                ('pic', models.ImageField(blank=True, null=True, upload_to='articlebodypics')),
            ],
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('body', mdeditor.fields.MDTextField()),
                ('timestamp', models.DateTimeField()),
                ('views', models.PositiveIntegerField(default=0)),
                ('greats', models.PositiveIntegerField(default=0)),
                ('comments', models.IntegerField(default=0)),
                ('status', models.CharField(default='DEL', max_length=20)),
                ('brief', models.CharField(blank=True, max_length=200, null=True)),
                ('pic', models.ImageField(upload_to='jiablogimages')),
                ('istop', models.CharField(blank=True, default='', max_length=5, null=True)),
                ('articlebodybrief', models.TextField(blank=True, null=True)),
                ('last_edit_timestamp', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
        migrations.CreateModel(
            name='BlogRole',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('status', models.IntegerField(default=0)),
            ],
            options={
                'permissions': (('add_user_per', '添加用户权限'), ('del_user_per', '删除用户权限'), ('change_user_per', '修改用户权限'), ('sel_user_per', '查询用户权限')),
            },
        ),
        migrations.CreateModel(
            name='BlogUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='男', max_length=32)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
                ('userpic', models.ImageField(blank=True, null=True, upload_to='userpic')),
                ('status', models.CharField(choices=[('active', '有效'), ('disabled', '无效')], default='有效', max_length=32)),
                ('brief', models.CharField(blank=True, max_length=1024, null=True)),
                ('role', models.ManyToManyField(blank=True, null=True, to='JiaBlog.BlogRole')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'ordering': ['c_time'],
            },
        ),
        migrations.CreateModel(
            name='BlogUserCollect',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('blogid', models.CharField(max_length=15)),
                ('userid', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CodeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255)),
                ('text', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('name', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='JiaBlog.BlogUser')),
                ('parentcomment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='JiaBlog.Comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JiaBlog.Articles')),
            ],
        ),
        migrations.CreateModel(
            name='DayNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(default=django.utils.timezone.now, verbose_name='日期')),
                ('count', models.IntegerField(default=0, verbose_name='网站访问次数')),
            ],
            options={
                'verbose_name': '网站日访问量统计',
                'verbose_name_plural': '网站日访问量统计',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Graduation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Hits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField(default=0)),
                ('blogid', models.IntegerField(default=0)),
                ('hitnum', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': '点击量',
                'verbose_name_plural': '点击量',
            },
        ),
        migrations.CreateModel(
            name='Honour',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Jia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('brief', models.CharField(max_length=100)),
                ('pic', models.ImageField(blank=True, null=True, upload_to='jia')),
            ],
        ),
        migrations.CreateModel(
            name='JiaFile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('file_name', models.CharField(max_length=500)),
                ('file_url', models.CharField(max_length=500)),
                ('file_status', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=256)),
                ('title', models.CharField(max_length=512)),
                ('content', models.TextField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('publish', models.DateTimeField(auto_now_add=True)),
                ('phone', models.CharField(blank=True, default='', max_length=11, null=True)),
                ('messpic', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.CharField(max_length=16, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=128)),
                ('year', models.IntegerField(null=True)),
                ('filmpic', models.ImageField(blank=True, null=True, upload_to='filmpics')),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='JiaBlog.Area')),
                ('genres', models.ManyToManyField(db_table='movie_genre', related_name='movies', to='JiaBlog.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1000)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('noteimage', models.ImageField(upload_to='noteimg')),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='params',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('param_value', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Recruinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=30)),
                ('job', models.CharField(max_length=50)),
                ('info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Recruitment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('industry_name', models.CharField(max_length=50)),
                ('is_form', models.CharField(choices=[('yes', '是'), ('no', '否')], max_length=10)),
                ('if_accept', models.CharField(max_length=50)),
                ('des', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sysrecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cpu', models.FloatField()),
                ('mem', models.FloatField()),
                ('disk_usage', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='男', max_length=32)),
                ('userpic', models.ImageField(blank=True, null=True, upload_to='userpic')),
                ('brief', models.CharField(max_length=100)),
                ('study_about', models.CharField(max_length=200)),
                ('personal_phone', models.CharField(max_length=15)),
                ('office_phone', models.CharField(max_length=15)),
                ('office_address', models.CharField(max_length=20)),
                ('info', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Userip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=30, verbose_name='IP地址')),
                ('count', models.IntegerField(default=0, verbose_name='访问次数')),
            ],
            options={
                'verbose_name': '访问用户信息',
                'verbose_name_plural': '访问用户信息',
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_time', models.DateField()),
                ('version_content', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='VisitNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0, verbose_name='网站访问总次数')),
            ],
            options={
                'verbose_name': '网站访问总次数',
                'verbose_name_plural': '网站访问总次数',
            },
        ),
        migrations.AddField(
            model_name='articles',
            name='authorname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JiaBlog.BlogUser'),
        ),
        migrations.AddField(
            model_name='articles',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JiaBlog.Category'),
        ),
        migrations.AddField(
            model_name='articles',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='JiaBlog.Tag'),
        ),
    ]

# Generated by Django 4.2 on 2023-05-02 13:27

import autoslug.fields
import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='blankpage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('meta_tags', models.CharField(blank=True, max_length=2000)),
                ('meta_desc', models.TextField(blank=True, max_length=2000)),
                ('slug', autoslug.fields.AutoSlugField(editable=True, populate_from='title', unique=True)),
                ('image', models.ImageField(upload_to='media/blog')),
                ('image_alt_name', models.CharField(blank=True, max_length=200)),
                ('desc', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('author', models.CharField(default='admin', max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('hit', models.PositiveIntegerField(default=0)),
                ('disc', models.BooleanField(default=False, verbose_name='Add In Disclaimer')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.CharField(blank=True, max_length=500)),
                ('purchase', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('certificate', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(editable=True, populate_from='title', unique=True)),
                ('logo', models.ImageField(blank=True, help_text='Optional', null=True, upload_to='media/catlogo')),
                ('logo1', models.ImageField(blank=True, help_text='Optional', null=True, upload_to='media/catlogo')),
                ('logo2', models.ImageField(blank=True, help_text='Optional', null=True, upload_to='media/catlogo')),
                ('top_three_cat', models.BooleanField(default=False)),
                ('more', models.BooleanField(blank=True, default=False, verbose_name='For Add In Right Menu')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('disc', models.BooleanField(default=False, verbose_name='Add In Disclaimer')),
                ('hit', models.PositiveIntegerField(default=0)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='app.category')),
            ],
            options={
                'verbose_name_plural': 'categories',
                'unique_together': {('slug', 'parent')},
            },
        ),
        migrations.CreateModel(
            name='clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/clients')),
            ],
        ),
        migrations.CreateModel(
            name='MainCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(editable=True, populate_from='title', unique=True)),
                ('disc', models.BooleanField(default=False, verbose_name='Add In Disclaimer')),
            ],
        ),
        migrations.CreateModel(
            name='offers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('off', models.CharField(max_length=100, verbose_name='Total Off')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('subtitle', models.CharField(max_length=100, verbose_name='Sub Title')),
                ('price', models.CharField(max_length=100, verbose_name='Price')),
                ('desc', models.CharField(max_length=100, verbose_name='Description')),
                ('button_text', models.CharField(max_length=100, verbose_name='Button Text')),
                ('button_url', models.URLField(default='', max_length=500, verbose_name='Button Link')),
                ('small_desc', models.CharField(max_length=100, verbose_name='Small Description')),
                ('active', models.BooleanField(default=False, verbose_name='Status')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('meta_tags', models.CharField(blank=True, max_length=2000)),
                ('meta_desc', models.TextField(blank=True, max_length=2000)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, max_length=500, populate_from='title', unique=True)),
                ('image', models.ImageField(upload_to='media/post')),
                ('image_alt_name', models.CharField(blank=True, max_length=200)),
                ('logo', models.ImageField(upload_to='media/post')),
                ('desc', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('badge', models.CharField(max_length=70)),
                ('youtube', models.URLField(default='', max_length=500)),
                ('author', models.CharField(default='admin', max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('hit', models.PositiveIntegerField(default=0)),
                ('button_text', models.CharField(default='Apply Now', max_length=20)),
                ('slider_post', models.BooleanField(blank=True, default=False)),
                ('price', models.IntegerField(default=0)),
                ('old_price', models.IntegerField(default=0)),
                ('discount', models.IntegerField()),
                ('emi_start_price', models.IntegerField()),
                ('why_title', models.CharField(blank=True, max_length=500)),
                ('why1', ckeditor.fields.RichTextField(blank=True)),
                ('why2', ckeditor.fields.RichTextField(blank=True)),
                ('why3', ckeditor.fields.RichTextField(blank=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='media/certificate')),
                ('disc', models.BooleanField(default=False, verbose_name='Add In Disclaimer')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='app.category')),
                ('maincourse', models.ManyToManyField(blank=True, related_name='posts', to='app.maincourse')),
            ],
        ),
        migrations.CreateModel(
            name='promocode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('valid_from', models.DateTimeField()),
                ('valid_to', models.DateTimeField()),
                ('amount', models.FloatField()),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('serial_number', models.IntegerField()),
                ('video_id', models.CharField(max_length=100)),
                ('is_preview', models.BooleanField(default=False)),
                ('desc', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='app.post')),
            ],
        ),
        migrations.CreateModel(
            name='timing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(blank=True, max_length=100, null=True)),
                ('day_duration', models.CharField(blank=True, max_length=100, null=True)),
                ('time_duration1', models.CharField(blank=True, max_length=100, null=True)),
                ('time_duration2', models.CharField(blank=True, max_length=100, null=True)),
                ('Post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time_posts', to='app.post')),
            ],
        ),
        migrations.CreateModel(
            name='tcforblog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('blank_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tc_blank_page', to='app.blankpage')),
            ],
        ),
        migrations.CreateModel(
            name='subcat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('disc', models.BooleanField(default=False, verbose_name='Add In Disclaimer')),
                ('parent', models.ForeignKey(blank=True, help_text='Select Only Sub Category', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcat', to='app.category')),
            ],
            options={
                'verbose_name_plural': 'Sub Categories',
                'unique_together': {('slug', 'parent')},
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
                ('stars', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='app.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='subcategory',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcat', to='app.subcat'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('phone', models.CharField(default='0', max_length=10)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='INR ORDER TOTAL')),
                ('emailAddress', models.EmailField(blank=True, max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('payment_id', models.CharField(max_length=100, null=True)),
                ('order_id', models.CharField(max_length=100, null=True)),
                ('coupon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.promocode')),
                ('orderitems', models.ManyToManyField(to='app.cart')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('Post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feature_posts', to='app.post')),
            ],
        ),
        migrations.CreateModel(
            name='faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('Post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faq_posts', to='app.post')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='media/profile_pic')),
                ('address', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=20)),
                ('Country', models.CharField(blank=True, max_length=20)),
                ('Company', models.CharField(blank=True, max_length=20)),
                ('City', models.CharField(blank=True, max_length=20)),
                ('State', models.CharField(blank=True, max_length=20)),
                ('Zip_Code', models.IntegerField(blank=True, default='1')),
                ('Telephone', models.IntegerField(blank=True, default='1')),
                ('Extension', models.CharField(blank=True, max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Curriculam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('Post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acc_posts', to='app.post')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='app.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='media/certificate')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('Post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cert_posts', to='app.post')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='app.post'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='boxes_three',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('slug', autoslug.fields.AutoSlugField(editable=True, populate_from='title', unique=True)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.category')),
            ],
        ),
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('meta_tags', models.CharField(blank=True, max_length=2000)),
                ('meta_desc', models.TextField(blank=True, max_length=2000)),
                ('slug', autoslug.fields.AutoSlugField(editable=True, populate_from='title', unique=True)),
                ('image', models.ImageField(upload_to='media/blog')),
                ('image_alt_name', models.CharField(blank=True, max_length=200)),
                ('desc', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('author', models.CharField(default='admin', max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('hit', models.PositiveIntegerField(default=0)),
                ('disc', models.BooleanField(default=False, verbose_name='Add In Disclaimer')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='blog', to='app.category')),
            ],
        ),
        migrations.AddField(
            model_name='blankpage',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='blank', to='app.category'),
        ),
    ]

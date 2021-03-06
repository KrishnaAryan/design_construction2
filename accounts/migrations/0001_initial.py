# Generated by Django 3.1.1 on 2021-12-10 12:29

import accounts.models
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.CharField(default=accounts.models.customer_generate_id, editable=False, max_length=10, primary_key=True, serialize=False)),
                ('mobile_no', models.CharField(max_length=13)),
                ('otp', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.CharField(default=accounts.models.department_generate_id, editable=False, max_length=10, primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Department',
            },
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.CharField(default=accounts.models.package_generate_id, editable=False, max_length=10, primary_key=True, serialize=False)),
                ('package_names', models.CharField(max_length=50)),
                ('package_detail', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Package',
            },
        ),
        migrations.CreateModel(
            name='ProjectDetails',
            fields=[
                ('id', models.CharField(default=accounts.models.projectDetails_generate_id, editable=False, max_length=10, primary_key=True, serialize=False)),
                ('booking_date', models.DateField()),
                ('total_value', models.FloatField()),
                ('booking_amount', models.FloatField()),
                ('project_description', models.TextField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department', to='accounts.department')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_details', to='accounts.package')),
                ('registration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_details', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'project Detail',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.CharField(default=accounts.models.team_generate_id, editable=False, max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('position', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=100, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team', to='accounts.projectdetails')),
                ('registration', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='register', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Team',
            },
        ),
        migrations.CreateModel(
            name='PersonalDetails',
            fields=[
                ('id', models.CharField(default=accounts.models.personal_generate_id, editable=False, max_length=10, primary_key=True, serialize=False)),
                ('full_name', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('dob', models.DateField()),
                ('profile_image', models.ImageField(upload_to='image/')),
                ('local_address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=25)),
                ('state', models.CharField(max_length=25)),
                ('zip_code', models.CharField(max_length=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('registrations', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personal_details', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'personal Detail',
            },
        ),
    ]

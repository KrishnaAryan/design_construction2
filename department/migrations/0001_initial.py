# Generated by Django 3.2.9 on 2021-11-23 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_auto_20211123_1335'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectCoordination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=25)),
                ('emp_id', models.CharField(max_length=8)),
                ('designation', models.CharField(max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_coordination', to='accounts.projectdetails')),
            ],
        ),
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=25)),
                ('emp_id', models.CharField(max_length=8)),
                ('designation', models.CharField(max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='finance', to='accounts.projectdetails')),
            ],
        ),
        migrations.CreateModel(
            name='ExecutionTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=25)),
                ('emp_id', models.CharField(max_length=8)),
                ('designation', models.CharField(max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='execution_team', to='accounts.projectdetails')),
            ],
        ),
        migrations.CreateModel(
            name='DesignTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=25)),
                ('emp_id', models.CharField(max_length=8)),
                ('designation', models.CharField(max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='design_team', to='accounts.projectdetails')),
            ],
        ),
    ]

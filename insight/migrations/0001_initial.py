# Generated by Django 3.1.1 on 2021-12-02 08:06

from django.db import migrations, models
import insight.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Insight',
            fields=[
                ('id', models.IntegerField(default=insight.models.insight_generate_id, editable=False, primary_key=True, serialize=False)),
                ('total_project', models.IntegerField()),
                ('total_project_value', models.FloatField()),
                ('total_project_amount_due', models.FloatField()),
                ('timeline', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

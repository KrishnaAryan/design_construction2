# Generated by Django 3.1.1 on 2021-12-10 12:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import payment_tracker.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentTracker',
            fields=[
                ('id', models.CharField(default=payment_tracker.models.payment_tracker_generate_id, editable=False, max_length=10, primary_key=True, serialize=False)),
                ('total_project_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_amount_due', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('payment_mode', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_tracker', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Payment Tracker',
            },
        ),
        migrations.CreateModel(
            name='PaymentInstallment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('installment', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.DateField()),
                ('payment_mode', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='accounts.projectdetails')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_installment', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Payment Installment',
            },
        ),
    ]

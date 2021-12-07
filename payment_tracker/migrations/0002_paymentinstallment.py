# Generated by Django 3.1.1 on 2021-12-07 12:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20211205_1248'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payment_tracker', '0001_initial'),
    ]

    operations = [
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
        ),
    ]
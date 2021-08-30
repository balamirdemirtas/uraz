# Generated by Django 3.0.5 on 2021-07-17 21:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='İsim:')),
                ('last_name', models.CharField(max_length=50, verbose_name='Soy İsim:')),
                ('email', models.EmailField(default='', max_length=254, verbose_name='Email Adresiniz:')),
                ('phone', models.CharField(max_length=11, verbose_name='Telefon :')),
                ('hotel', models.CharField(max_length=100, verbose_name='Hotel')),
                ('room', models.IntegerField()),
                ('city', models.CharField(max_length=100, verbose_name='İlçe :')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('paid', models.BooleanField(default=False)),
                ('day', models.DateField(null=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('created_date', models.DateTimeField(auto_now=True, verbose_name='Oluşturlma Tarihi')),
                ('author', models.ForeignKey(default='Alan', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='shop.Product')),
            ],
        ),
    ]
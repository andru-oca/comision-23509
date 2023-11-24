# Generated by Django 4.2.7 on 2023-11-24 20:43

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tienda",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(default="tienda x", max_length=100)),
                (
                    "ubicacion",
                    models.CharField(default="calle falsa 123", max_length=100),
                ),
                ("precio_tienda", models.FloatField(default=128000.0)),
                (
                    "contacto",
                    models.EmailField(default="tienda_x@mail.com", max_length=100),
                ),
                (
                    "rubro",
                    models.CharField(
                        choices=[
                            ("comida", "Gastronomia"),
                            ("industria", "Industria Textil"),
                            ("golosinas", "Chucherias"),
                        ],
                        max_length=10,
                    ),
                ),
                ("fecha_disponible", models.DateField(auto_now=True)),
            ],
            options={
                "db_table": "tiendas_cordoba_ventas",
            },
        ),
    ]

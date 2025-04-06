# Generated by Django 5.0.2 on 2025-04-05 17:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=100, unique=True)),
                ('mot_de_passe', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Moughataa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_fr', models.CharField(max_length=255)),
                ('nom_ar', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Wilaye',
            fields=[
                ('code_wilaye', models.IntegerField(primary_key=True, serialize=False)),
                ('nom_wilaye_Ar', models.CharField(blank=True, max_length=255, null=True)),
                ('nom_wilaye_fr', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_ar', models.CharField(max_length=100)),
                ('prenom_ar', models.CharField(max_length=100)),
                ('nom_fr', models.CharField(max_length=100)),
                ('prenom_fr', models.CharField(max_length=100)),
                ('numero_telephone', models.CharField(max_length=20)),
                ('photo_de_profile', models.ImageField(blank=True, null=True, upload_to='profils/')),
                ('moughataa', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='cars.moughataa')),
                ('wilaye', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.wilaye')),
            ],
        ),
        migrations.CreateModel(
            name='Sponsorise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('actif', models.BooleanField(default=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='VoitureLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marque', models.CharField(max_length=50)),
                ('modele', models.CharField(max_length=50)),
                ('annee', models.IntegerField()),
                ('prix_journalier', models.DecimalField(decimal_places=2, max_digits=10)),
                ('transmission', models.CharField(choices=[('Automatique', 'Automatique'), ('Manuelle', 'Manuelle')], max_length=20)),
                ('carburant', models.CharField(choices=[('Essence', 'Essence'), ('Gazoil', 'Gazoil')], max_length=20)),
                ('date_ajout', models.DateTimeField(auto_now_add=True)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('disponible', models.BooleanField(default=True)),
                ('duree_minimale', models.IntegerField(default=1)),
                ('description', models.TextField(blank=True, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='VoitureVendu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marque', models.CharField(max_length=50)),
                ('modele', models.CharField(max_length=50)),
                ('annee', models.IntegerField()),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('transmission', models.CharField(choices=[('Automatique', 'Automatique'), ('Manuelle', 'Manuelle')], max_length=20)),
                ('carburant', models.CharField(choices=[('Essence', 'Essence'), ('Gazoil', 'Gazoil')], max_length=20)),
                ('date_ajout', models.DateTimeField(auto_now_add=True)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='imagaes/')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='imagaes/')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('vendu', models.BooleanField(default=False)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.utilisateur')),
            ],
        ),
        migrations.AddField(
            model_name='moughataa',
            name='wilaye',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.wilaye'),
        ),
    ]

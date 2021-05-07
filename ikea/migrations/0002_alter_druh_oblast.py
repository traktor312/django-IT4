# Generated by Django 3.2 on 2021-05-07 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ikea', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='druh',
            name='oblast',
            field=models.CharField(blank=True, choices=[('postele', 'Postele'), ('pohovky', 'Pohovky'), ('knihovny a policové díly', 'Knihovny a policové díly'), ('stoly', 'Stoly'), ('skříňky a příborníky', 'Skříňky a příborníky'), ('TV stolky', 'TV stolky'), ('komody', 'Komody'), ('šatní skříně', 'Šatní skříně'), ('židle', 'Židle'), ('venkovní nábytek', 'Venkovní nábytek'), ('příborníky', 'Příborníky'), ('dětský nábytek', 'Dětský nábytek'), ('rozdělovače místností', 'Rozdělovače místností'), ('vozíky', 'Vozíky'), ('barový nábytek', 'Barový nábytek'), ('křesla a lenošky', 'Křesla a lenošky'), ('nábytek do kavárny', 'Nábytek do kavárny'), ('nábytek pro miminka', 'Nábytek pro miminka')], default='postele', help_text='Vyberte označení oblasti', max_length=50, verbose_name='Oblast'),
        ),
    ]

from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse


class Druh(models.Model):
    oznaceni_druhu = models.CharField(max_length=50, unique=True, verbose_name="Označení druhu nábytku",
                            help_text='Zadejte text o maximální délce 50 znaků; text musí být jedinečný')
    OBLAST = (
        ('postele', 'Postele'),
        ('pohovky', 'Pohovky'),
        ('knihovny a policové díly', 'Knihovny a policové díly'),
        ('stoly', 'Stoly'),
        ('skříňky a příborníky', 'Skříňky a příborníky'),
        ('TV stolky', 'TV stolky'),
        ('komody', 'Komody'),
        ('šatní skříně', 'Šatní skříně'),
        ('židle', 'Židle'),
        ('venkovní nábytek', 'Venkovní nábytek'),
        ('příborníky', 'Příborníky'),
        ('dětský nábytek', 'Dětský nábytek'),
        ('rozdělovače místností', 'Rozdělovače místností'),
        ('vozíky', 'Vozíky'),
        ('barový nábytek', 'Barový nábytek'),
        ('křesla a lenošky', 'Křesla a lenošky'),
        ('nábytek do kavárny', 'Nábytek do kavárny'),
        ('nábytek pro miminka', 'Nábytek pro miminka'),
    )
    oblast = models.CharField(max_length=50, choices=OBLAST, blank=True, default='postele', verbose_name="Oblast", help_text='Vyberte označení oblasti')

    class Meta:
        ordering = ["oznaceni_druhu"]
        verbose_name = 'Druh nábytku'
        verbose_name_plural = 'Druh nábytku'

    def __str__(self):
        return f"{self.oznaceni_druhu}, {self.oblast}"


class Nabytek(models.Model):
    nazev = models.CharField(max_length=100, verbose_name="Název nábytku", help_text='Zadejte text o maximální délce 100 znaků')
    popis = models.TextField(blank=True, null=True, verbose_name="Popis nábytku")
    cena = models.FloatField(validators=[MinValueValidator(0.0)], null=True, help_text="Zadejte nezáporné desetinné číslo", verbose_name="Cena")
    foto = models.ImageField(upload_to='nabytek/%Y/%m/%d/', blank=True, null=True, verbose_name="Fotka nábytku")
    druh = models.ForeignKey(Druh, on_delete=models.RESTRICT)

    class Meta:
        ordering = ["-cena", "nazev"]
        verbose_name = 'Nábytek'
        verbose_name_plural = 'Nábytek'

    def __str__(self):
        return f"{self.nazev}, {self.cena}"

    def get_absolute_url(self):
        """Metoda vrací URL stránky, na které se vypisují podrobné informace o nábytku"""
        return reverse('detail', args=[str(self.id)])

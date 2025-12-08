from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
numero_validator = RegexValidator(
    regex=r'^(\+226|\+225)?(0|5|6|7)\d{7}$',
    message="Le numéro est invalide, veuillez entrer un numéro valide"
)


class Inscription(models.Model):
    numero = models.CharField(
        verbose_name="Numero WhatsApp",
        max_length=14,
        validators=[numero_validator]
    )
    tiktok_username = models.CharField(
        verbose_name="Compte tiktok",
        max_length=60,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.tiktok_username
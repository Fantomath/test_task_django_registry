from django.db import models


class RegistryRecord(models.Model):
    full_name = models.CharField("ФИО", max_length=255)
    birth_date = models.DateField("Дата рождения")
    credit_amount = models.FloatField("Сумма кредита")
    term_months = models.PositiveIntegerField("Срок в месяцах")

    class Meta:
        verbose_name = "Запись реестра"
        verbose_name_plural = "Реестр"
        ordering = ["-id"]

    def __str__(self) -> str:
        return f"{self.full_name} ({self.birth_date})"

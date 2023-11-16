from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=20,
        verbose_name = "Введите названия сайта"
    )
    logo = models.ImageField(
        upload_to="image_user/",
        verbose_name="Загрузите логотип"
    )
    description = models.TextField(
        verbose_name="Введите описание сайта"
    )
    phone = models.CharField(
        max_length=15,
        verbose_name="Телефонный номер"
    )
    email = models.EmailField(
        verbose_name="Введите свою почту"
    )

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Настройки'

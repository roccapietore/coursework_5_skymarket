from django.conf import settings
from django.db import models
from users.models import User


class Ad(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название товара")
    price = models.IntegerField(verbose_name="Стоимость товара")
    description = models.TextField(max_length=1000, null=True, blank=True, verbose_name="Описание объявления")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор объявления")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время и дата создания объявления")
    image = models.ImageField(upload_to="ads_image/", null=True, blank=True, verbose_name="Изображение")

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(max_length=200, verbose_name="Текст отзыва")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор отзыва")
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name="Объявление с отзывом")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время и дата создания отзыва")

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return self.text


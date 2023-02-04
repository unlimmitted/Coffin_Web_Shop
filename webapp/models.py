from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField


class CoffinList(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название гроба")
    content = models.TextField(blank=True, verbose_name="Описание")
    content_details = models.TextField(blank=True, verbose_name="Подробное описание")
    slug = AutoSlugField(populate_from='title')
    photo = models.ImageField(upload_to="images/%Y/%m/%d", verbose_name="Фото")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('coffin', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Гробы'
        verbose_name_plural = 'Гробы'


class ReviewList(models.Model):
    username = models.CharField(max_length=35, verbose_name='Пользователь')
    title = models.CharField(max_length=255, verbose_name='Краткая оценка')
    content = models.TextField(blank=True, verbose_name='Отзыв')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'

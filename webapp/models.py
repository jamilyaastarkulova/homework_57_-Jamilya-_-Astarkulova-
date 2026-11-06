from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')

    def __str__(self):
        return self.name


class Todo(models.Model):
    summary = models.CharField(max_length=200, verbose_name='Краткое описание')
    description = models.TextField(null=True, blank=True, verbose_name='Полное описание')
    status = models.ForeignKey(
        'webapp.Status',
        on_delete=models.PROTECT,
        related_name='todos',
        verbose_name='Статус'
    )
    type = models.ForeignKey(
        'webapp.Type',
        on_delete=models.PROTECT,
        related_name='todos',
        verbose_name='Тип'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время обновления')

    def __str__(self):
        return f"{self.id}. {self.summary}"
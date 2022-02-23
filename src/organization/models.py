import uuid
from datetime import datetime, timedelta
from django.db import models
from django.urls import reverse


class Organization(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='Название организации')

    class Meta:
        verbose_name_plural = 'organizations'
        ordering = ['name']

    def __str__(self):
        return {self.name}

    def get_absolute_url(self):
        return reverse('organization', kwargs={'org_id': self.id})


class Key(models.Model):
    id = models.BigAutoField(primary_key=True)
    key = models.UUIDField(default=uuid.uuid4, editable=True, verbose_name='Ключ')
    start_date = models.DateField(auto_now_add=True, verbose_name='Начало действия')
    stop_date = models.DateField(default=datetime.now()+timedelta(days=30), verbose_name='Окончание действия')
    org_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    is_blocked = models.BooleanField(default=False, verbose_name='Блокировка')

    def __str__(self):
        return f'Key #{self.key} is related to Organization #{self.org_id}'

    def get_absolute_url(self):
        return reverse('key', kwargs={'key_id': self.id})

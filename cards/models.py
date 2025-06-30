from django.db import models
import uuid
from accounts.models import Account

class Card(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'ACTIVE', 'Активна'
        BLOCKED = 'BLOCKED', 'Заблокирована'
        EXPIRED = 'EXPIRED', 'Истек срок'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='cards')
    masked_number = models.CharField(max_length=19)
    expires_at = models.DateField()
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.ACTIVE)

    def __str__(self):
        return f'Card {self.masked_number}' 

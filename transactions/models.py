from django.db import models
import uuid
from accounts.models import Account


class Transaction(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Ожидается'
        SUCCESS = 'SUCCESS', 'Успешно'
        FAILED = 'FAILED', 'Неудачно'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='outgoing_transactions')
    receiver = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='incoming_transactions')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(choices=Status.choices, default=Status.PENDING, max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender} -> {self.receiver} | {self.amount}'


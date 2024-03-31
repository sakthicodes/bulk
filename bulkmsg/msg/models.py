# bulk_sender/models.py
from django.db import models

class Message(models.Model):
    phone_number = models.CharField(max_length=20)
    message_text = models.TextField()

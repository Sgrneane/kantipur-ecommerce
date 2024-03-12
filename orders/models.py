from django.db import models
import uuid
from account.models import CustomUser


# Create your models here.
class Cart(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField()
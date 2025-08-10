from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    image = models.CharField(max_length=256, blank=True)

    def __str__(self) -> str:
        name = self.user.first_name +' ' + self.user.last_name
        if name == ' ':
            return self.user.__str__()
        return name


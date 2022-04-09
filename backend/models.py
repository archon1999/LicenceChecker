from django.db import models


class ValidAccount(models.Model):
    accounts = models.Manager()
    mac_address = models.CharField(max_length=255)
    host_name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.host_name

from django.db import models

# Create your models here.
class Contacts(models.Model):
    contact_name = models.CharField(max_length=100, null=False, blank=False)
    contact_email = models.EmailField(null=False, blank=False)
    contact_subject = models.CharField(max_length=100, null=False, blank=False)
    contact_message = models.TextField(max_length=100,)

    def __str__(self):
        return str(self.contact_name)
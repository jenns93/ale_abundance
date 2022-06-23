from django.db import models

ISSUE_TYPE = ((0, "Product"), (1, "Review"), (2, "Order"), (3, "Profile"), (4, "Other"))

class Contact(models.Model):
    name = models.CharField(max_length=200, unique=True)
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=254, null=True, blank=False)
    issue_type = models.IntegerField(choices=ISSUE_TYPE, default=0)
    issue_details = models.TextField()
# Create your models here.

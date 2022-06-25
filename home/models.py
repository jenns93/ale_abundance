from django.db import models
from django.contrib.auth.models import User

ISSUE_TYPE = ((0, "Product"), (1, "Review"), (2, "Order"), (3, "Profile"), (4, "Other"))


class Contact(models.Model):
    full_name = models.CharField(max_length=50, null=True, blank=False)
    email = models.EmailField(max_length=254, null=True, blank=False)
    issue_type = models.IntegerField(choices=ISSUE_TYPE, default=0)
    issue_details = models.TextField()
    def __str__(self):
        return str(self.full_name)
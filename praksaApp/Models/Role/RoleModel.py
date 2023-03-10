from django.db import models

class Role(models.Model):
    roleId = models.IntegerField(primary_key=True)
    roleName = models.CharField(max_length=100)
    roleDescription = models.TextField()
    
    class Meta:
        db_table = "Role"
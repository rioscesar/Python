from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=255)
    # this should create different directories for users
    resume = models.FileField(upload_to='resume/')

    def __str__(self):
        return self.user_name

class Tag(models.Model):
    user = models.ForeignKey(User)
    tag = models.CharField(max_length=255)

    def __str__(self):
        return self.tag
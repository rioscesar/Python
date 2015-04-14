from django.db import models

class Users(models.Model):
    user_name = models.CharField(max_length=255)
    # this should create different directories for users
    resume = models.FileField(upload_to='resume/user_name/')

    def __str__(self):
        return self.user_name

class Tags(models.Model):
    user = models.ForeignKey(Users)
    tag = models.CharField(max_length=255)

    def __str__(self):
        return self.tag
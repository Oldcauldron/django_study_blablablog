from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Hashtag(models.Model):
    tag = models.CharField(max_length=60)
    owner_tag = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.tag


class Blogpost(models.Model):
    tag = models.ForeignKey(Hashtag, on_delete=models.CASCADE)
    owner_post = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    razdel = '=' * 20

    # def __str__(self):
    #     self.ret = f'''{self.title} \n {self.text}'''
    #     return self.ret
    def __str__(self):
        return self.title










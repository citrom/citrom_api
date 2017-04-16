from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class User(models.Model):
    name = models.CharField(max_length=30)
    lvl = models.PositiveSmallIntegerField()
    avatar = models.CharField(max_length=300)

class Post(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=3000)
    preview = models.CharField(max_length=300)
    category  = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    shedule = models.DateTimeField(auto_now_add=True, blank=True)
    allwoed =  models.BooleanField()
    likes = models.IntegerField()


class Comment(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id =models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    allowed = models.BooleanField()
    reported  = models.BooleanField()
    likes = models.IntegerField()

class User_meta(models.Model):
    udi = models.ForeignKey(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=300)
    value = models.CharField(max_length=300)

class Comment_meta(models.Model):
    udi = models.ForeignKey(Comment, on_delete=models.CASCADE)
    key = models.CharField(max_length=300)
    value = models.CharField(max_length=300)

class Post_meta(models.Model):
    udi = models.ForeignKey(Post, on_delete=models.CASCADE)
    key = models.CharField(max_length=300)
    value = models.CharField(max_length=300)
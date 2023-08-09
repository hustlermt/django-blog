from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Post(models.Model):
    # GENDER = (
    #     ('','Choose gender'),
    #     ('male','Male'),
    #     ('female','Female'),
    #     ('diversity','Diversity')
    #     )
  
    # user = models.CharField(max_length=255,null=True,blank=True)
    # gender = models.CharField(max_length=30,choices=GENDER)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' '+ str(self.timestamp)
    
    class Meta:
        ordering = ["-timestamp", ]

class Comment(models.Model):
    # user = models.CharField(max_length=255,null=True,blank=True)
    post = models.ForeignKey(Post,on_delete=CASCADE,related_name='post_comment')
    comment =models.TextField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.title
    
    class Meta:
        ordering = ["-timestamp", ]





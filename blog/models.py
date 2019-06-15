from django.db import models
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    #STATUS = (('draft', 'DRAFT'), ('published', 'Published'))
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    #slug = models.SlugField(max_length=200, unique_for_date='publish')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    #status = models.CharField(max_length=20, choices=STATUS, default='draft')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
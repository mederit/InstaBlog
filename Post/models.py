from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    body = models.TextField(db_index=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    slug = models.SlugField(max_length=15, unique=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-date_pub',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})
    

    def __str__(self):
        return f"{self.title} by {self.author}"


from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    body = models.TextField(db_index=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    slug = models.SlugField(max_length=15, unique=True)
    #photo = models.ImageField(upload_to='images')
    date_pub = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering = ('-date_pub',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f"{self.title} by {self.author}"

    def absolute_absolute_url(self):
        return reverse('post')


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, 
                                    related_name="comments_posts",
                                    verbose_name='пост',
                                    blank=True, null=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, 
                                        related_name='users_comments',
                                        verbose_name='автор коментария',
                                    blank=True, null=True)

    text = models.TextField(verbose_name='текст комментраия')
    created_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(verbose_name='статус', default=False)


    class Meta:
        ordering = ('created_date',)
        verbose_name = ' Коментарий'
        verbose_name_plural = 'Коментарии'

    def __str__(self):  
        return f"Comment by {self.author} on {self.post}"
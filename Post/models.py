from django.db import models

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, 
                                    related_name="comments")

    author = models.ForeignKey(User, on_delete=models.CASCADE, 
                                        related_name='users_comments')
    
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('created_at',)
        verbose_name = ' Коментарий'
        verbose_name_plural = 'Коментарии'

    def __str__(self):  
        return f"Comment by {self.author} on {self.post}"

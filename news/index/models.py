from django.db import models

# Create your models here.
class NewsCategory(models.Model):
    class Meta:
        verbose_name_plural = 'Категории'

    category_name = models.CharField(max_length=128)
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.category_name)

class News(models.Model):
    class Meta:
        verbose_name_plural = 'Новости'

    news_title = models.CharField(max_length=128)
    text = models.TextField()
    news_photo = models.ImageField(upload_to='media/', blank=True, null=True)
    news_category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.news_title)
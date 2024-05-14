from django.db import models
from django.urls import reverse

class Heh(models.Model):
    title = models.CharField('Название', max_length=80)
    content = models.TextField(blank=True, null=True, verbose_name="Текст статьи")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True, verbose_name="Фото")
    data = models.DateField('Дата публикации')
    cat_id = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name="Категории")
  
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})
    
 
    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты блюд от шеф-поваро'
        ordering = ['id']

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})
    
    class Meta:
        ordering = ['id']
 
  
 
 
    
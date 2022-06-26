from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from PIL import Image
from django.db.models.signals import pre_save, post_save
import random



class App(models.Model):
    app_name = models.CharField(max_length=100)
    app_image = models.ImageField(default='default.jpg', upload_to = 'app_images')
    date_published= models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, null=True, unique=True, editable=False)

    def __str__(self):
        return str(self.app_name)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.app_name)
        
        
    #     super().save(*args, **kwargs)
        
        
    #     img = Image.open(self.app_image.path)
    #     if img.height > 300 or img.width > 300 :
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.app_image.path)


    def get_absolute_url(self):
        return reverse('apps')


def slugify_instance_name(instance, save=False, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else :
        slug = slugify(instance.app_name)
    qs = App.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        rand_int = random.randint(100_000, 500_000)
        slug = f"{slug}-{rand_int}"
        return slugify_instance_name(instance, save=save, new_slug=slug)
    instance.slug = slug
    if save:
        instance.save()

def app_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        slugify_instance_name(instance, save=False)
        
    

pre_save.connect(app_pre_save, sender=App)


def app_post_save(sender, instance, created, *args, **kwargs):
    if created:
        slugify_instance_name(instance, save=True)
        

post_save.connect(app_pre_save, sender=App)
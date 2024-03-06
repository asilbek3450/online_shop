from django.db import models
from django.utils.text import slugify

from users.models import User


# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField()
    information = models.TextField()
    stock = models.PositiveIntegerField()  # Quantity in stock

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product_images")

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name_plural = "Product Images"
        ordering = ["-id"]

    def get_image_url(self):
        return self.image.url


class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s review for {self.product.name}"

    class Meta:
        verbose_name_plural = "Product Reviews"
        ordering = ["-id"]

    def get_rating(self):
        return self.rating

    def get_review(self):
        return self.review



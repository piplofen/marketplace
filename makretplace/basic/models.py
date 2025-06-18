from django.db import models
from django.urls import reverse

class Item(models.Model):
    name = models.CharField(max_length=120)
    article = models.CharField(max_length=20)
    manufacture = models.ForeignKey("Manufacture", on_delete=models.PROTECT, null=True)
    description = models.TextField(default="Описание товара")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey("Category", on_delete=models.PROTECT, null=True)
    photo = models.ImageField(upload_to="images", blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("item", kwargs={"item_id": self.pk})

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

class Manufacture(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=20)
    address = models.TextField(default="Юридический адрес")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("manufacture", kwargs={"manufacture_id": self.pk})

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"

class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category", kwargs={"category_id": self.pk})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

from django.db import models
from users.models import CustomUser
                                                                                #
# Create your models here.
class Category(models.Model):                       
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)            # Mahsulot muallifi bilan bog'lanish. on_delete=models.CASCADE - agar muallif o'chirilsa unga tegishli mahsulotlar ham o'chiriladi.
    category = models.ForeignKey(Category, on_delete=models.CASCADE)            # Mahsulot kategoriyasi bilan bog'lanish.
    title = models.CharField(max_length=150)                                    # Mahsulot sarlavhasi maydoni
    description = models.TextField()                                            # Qo'shimcha malumotlar uchun matn maydoni
    price = models.DecimalField(max_digits=10, decimal_places=2)                # Mahsulot narxi maydoni. max_digits=10 - maksimal raqamlar soni, decimal_places=2 - onlikdan keyingi raqamlar soni
    adress = models.CharField(max_length=150)                                   # Mahsulot manzili maydoni
    phone_number = models.CharField(max_length=17)                              # Mahsulot muallifining telefon raqami maydoni
    tg_username = models.CharField(max_length=50)                               # Mahsulot muallifining telegram foydalanuvchi nomi maydoni
    date_created = models.DateTimeField(auto_now_add=True)                      # Mahsulot yaratish sanasi maydoni. auto_now_add=True - faqat bir marta yaratilganda avtomatik ravishda hozirgi vaqtni saqlaydi
  
    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['-id']


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)              # Mahsulot bilan bog'lanish. on_delete=models.CASCADE - agar mahsulot o'chirilsa unga tegishli rasm ham o'chiriladi.
    image = models.ImageField(upload_to='product_images/')                      # Mahsulot rasmi maydoni. upload_to='product_images/' - rasmni saqlash papkasi

    def __str__(self):
        return str(self.product.title)


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)              # Izoh qilingan mahsulot bilan bog'lanish
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)            # Izoh muallifi bilan bog'lanish
    body = models.TextField()                                                   # Izoh matni maydoni
    # text = models.TextField()                                                   # Izoh matni maydoni
    date_created = models.DateTimeField(auto_now_add=True)                      # Izoh yaratish sanasi maydoni. auto_now_add=True - faqat bir marta yaratilganda avtomatik ravishda hozirgi vaqtni saqlaydi

    def __str__(self):
        return "Coment of " + str(self.author.username)


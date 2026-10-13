from django.db import models
from django.contrib.auth.models import AbstractUser
                                                                                #
# Create your models here.
class CustomUser(AbstractUser):                                                 # Foydalanuvchilar modelini yaratish uchun AbstractUser dan meros olish
    phone_number = models.CharField(max_length=15,)                             # Telefon raqami maydoni
    tg_username = models.CharField(max_length=50,)                              # Telegram foydalanuvchi nomi maydoni
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')  # Foydalanuvchi avatari maydoni. pipenv install Pillow deb o'rnatish kerak. upload_to='avatars/' - rasmni saqlash papkasi, default='avatars/default.jpg' - agar foydalanuvchi avatarini o'rnatmasa default rasmni saqlaydi
    
    def __str__(self):                                                          # Foydalanuvchi obyektini o'zini chaqirganda matn ko'rinishida username ni qaytaradi
        return str(self.username)                                               # 


class Saved(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    body = models.CharField(max_length=150)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):                                                          
        return "Saved of " + str(self.author.username)

    class Meta:
        db_table = 'products_saved'



"""
# Faqat tushuntirish uchun: AbstractUser bu maydonlarni allaqachon beradi.
# Amaldagi CustomUser ichida ularni qayta yozish shart emas.
from django.utils import timezone           

class MisolUser(AbstractUser):
    # id maydonini Django avtomatik yaratadi (AutoField yoki BigAutoField).
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='user_set',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='user_set',
        related_query_name='user',
    )
"""
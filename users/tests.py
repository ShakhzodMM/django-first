from django.test import TestCase
from products.models import Category, Product
from .models import CustomUser, Saved


class SavedModelTests(TestCase):
    def test_saved_product_is_linked_to_user_and_product(self):
        author = CustomUser.objects.create_user(
            username='saved-user',
            password='test-password',
            phone_number='',
            tg_username='',
        )
        category = Category.objects.create(name='Saved category')
        product = Product.objects.create(
            author=author,
            category=category,
            title='Saved product',
            description='Product description',
            price='10.00',
            adress='Tashkent',
            phone_number='',
            tg_username='',
        )

        saved = Saved.objects.create(author=author, product=product, body='')

        self.assertEqual(saved.author, author)
        self.assertEqual(saved.product, product)
        self.assertEqual(str(saved), 'Saved of saved-user')
        self.assertEqual(Saved._meta.db_table, 'products_saved')

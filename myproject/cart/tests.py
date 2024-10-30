# cart/tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Product, Cart, CartItem
from .forms import AddToCartForm

class CartTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.product = Product.objects.create(name='Test Product', price=10.00)

    def test_add_to_cart_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(f'/cart/add/{self.product.id}/', {'quantity': 2})
        self.assertRedirects(response, '/cart/detail/')
        
        cart = Cart.objects.get(user=self.user)
        self.assertEqual(cart.items.count(), 1)
        cart_item = cart.items.first()
        self.assertEqual(cart_item.product, self.product)
        self.assertEqual(cart_item.quantity, 2)

    def test_cart_detail_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get('/cart/detail/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Product')
        self.assertContains(response, 'Quantity: 1')
        self.assertContains(response, 'Total: $10.00')

from django.db import models

# Create your models here.

class login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

class category(models.Model):
    category_name = models.CharField(max_length=100)

class product(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    product_date = models.CharField(max_length=100)
    CATEGORY = models.ForeignKey(category,on_delete=models.CASCADE,default=1)

class user(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(login,on_delete=models.CASCADE,default=1)

class requests(models.Model):
    date = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=100)
    payment_date = models.CharField(max_length=100)
    USER = models.ForeignKey(user,on_delete=models.CASCADE,default=1)

class request_sub(models.Model):
    request_date = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    REQUESTS = models.ForeignKey(requests,on_delete=models.CASCADE,default=1)

class complaint(models.Model):
    complaints = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    reply = models.CharField(max_length=100)
    reply_date = models.CharField(max_length=100)
    USER = models.ForeignKey(user, on_delete=models.CASCADE, default=1)

class feedback(models.Model):
    feedbacks = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    USER = models.ForeignKey(user, on_delete=models.CASCADE, default=1)

class cart(models.Model):
    quantity = models.CharField(max_length=100)
    USER = models.ForeignKey(user, on_delete=models.CASCADE, default=1)
    PRODUCT = models.ForeignKey(product, on_delete=models.CASCADE, default=1)

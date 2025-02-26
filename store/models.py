from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="제품명")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="가격")
    stock = models.IntegerField(verbose_name="재고")
    description = models.TextField(verbose_name="설명", max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성 날짜")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정 날짜")

    def __str__(self):
        return self.name

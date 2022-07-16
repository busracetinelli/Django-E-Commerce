from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.models import Group
from djangoecommerce_app.models import User, City, CompanyAddress, CompanyFeature, Company, ProductCategory,  Product, ProductImage, ProductBrand, ProductStar, Coupon, Card, Order, OrderProductStatus, OrderProductComment,Contact

admin.site.site_header = 'Django Ecommerce Admin Panel'

admin.site.register(City)
admin.site.register(CompanyAddress)
admin.site.register(CompanyFeature)
admin.site.register(ProductCategory)
admin.site.register(ProductImage)
admin.site.register(ProductBrand)
admin.site.register(ProductStar)
admin.site.register(Coupon)
admin.site.register(OrderProductStatus)
admin.site.register(OrderProductComment)
admin.site.register(Contact)

@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = ["id", "username","first_name","last_name","email"]
    list_display_links = ["id", "username",]

    class Meta:
        model = User


@admin.register(Company)
class UserAdmin(ModelAdmin):
    list_display = ["id", "username","first_name","last_name","email"]
    list_display_links = ["id", "username",]

    class Meta:
        model = User


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ["id", "name","owner","brand","price"]
    list_display_links = ["id","name"]
    list_editable = ["owner","brand","price"]

    class Meta:
        model = Product


@admin.register(Order)
class ProductAdmin(ModelAdmin):
    list_display = ["id", "buyer","owner","status", "coupon", "transaction_id", "transaction_time", "transaction_total_amount"]
    list_display_links = ["id"]
    list_editable = ["buyer","owner","status"]

    class Meta:
        model = Order


@admin.register(Card)
class CardAdmin(ModelAdmin):
    list_display = ["id", "owner","product","status","transaction_total_amount"]
    list_display_links = ["id"]
    list_editable = ["owner","product","status","transaction_total_amount"]

    class Meta:
        model = Card


admin.site.unregister(Group)

from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Model,ForeignKey,CharField,DateTimeField,FloatField,EmailField,ImageField,DateField,TextField, BooleanField,IntegerField,DecimalField,ManyToManyField

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDERS = (
        ('Erkek', 'Erkek'),
        ('Kadın', 'Kadın'),
        ('Belirtilmemiş', 'Belirtilmemiş'),
    )
    profile_photo = ImageField(verbose_name='Profil Fotoğrafı', upload_to='images/user/profile/', blank=True, null=True)
    gender = CharField(max_length=100, null=True, blank=True, verbose_name='Cinsiyet', choices=GENDERS)
    birthday = DateField(null=True, blank=True, verbose_name='Doğum Tarihi')
    bio = TextField(blank=True, null=True, verbose_name='Biyografi')
    phone = CharField(max_length=100, null=True, blank=True, verbose_name='Telefon No')
    link_facebook = CharField(max_length=250, null=True, blank=True, default='#', verbose_name='Facebook Linki')
    link_instagram = CharField(max_length=250, null=True, blank=True, default='#', verbose_name='Instagram Linki')
    link_twitter = CharField(max_length=250, null=True, blank=True, default='#', verbose_name='Twitter Linki')
    link_web = CharField(max_length=250, null=True, blank=True, default='#', verbose_name='Website Linki')

    class Meta:
        verbose_name = 'Kullanıcı'
        verbose_name_plural = 'Tüm Kullanıcılar'


class City(Model):
    name = CharField(max_length=255, verbose_name='İsim')
    number = IntegerField(verbose_name='İl Kodu', unique=True)

    class Meta:
        ordering = ('-number',)
        verbose_name = 'Şehir'
        verbose_name_plural = 'Şehirler'

    def __str__(self):
        return self.name


class CompanyAddress(Model):
    name = CharField(max_length=255, verbose_name='İsim', default='Adres', blank=True)
    open_address = TextField(max_length=100, verbose_name='Açık Adres')
    short_address = TextField(max_length=70, verbose_name='Kısa Adres')
    postal_code = CharField(max_length=10, null=True, blank=True, verbose_name='Posta Kodu')
    lat = DecimalField(max_digits=9, decimal_places=6, null=True, blank=True, verbose_name='X Koordinatı')
    long = DecimalField(max_digits=9, decimal_places=6, null=True, blank=True, verbose_name='Y Koordinatı')

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Adres'
        verbose_name_plural = 'Adresler'

    def __str__(self):
        return self.name



class CompanyFeature(Model):
    name = CharField(max_length=255, verbose_name='İsim')
    description = TextField(max_length=1000, verbose_name='Açıklama', blank=True, null=True)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Şirket Özelliği'
        verbose_name_plural = 'Şirket Özellikleri'

    def __str__(self):
        return self.name



class Company(User):
    city = ForeignKey('djangoecommerce_app.City', blank=True, null=True, verbose_name='Şehir', on_delete=models.CASCADE)
    address = ForeignKey('djangoecommerce_app.CompanyAddress', blank=True, null=True, verbose_name='Adres', on_delete=models.CASCADE)
    identity_number = CharField(max_length=11, null=True, blank=True, verbose_name='TC No')
    executive_namesurname = CharField(max_length=250, null=True, blank=True, verbose_name='Yetkili Adı Soyadı')
    executive_identity_number = CharField(max_length=250, null=True, blank=True, verbose_name='Yetkili TC No')
    executive_email = CharField(max_length=250, null=True, blank=True, verbose_name='Yetkili Email')
    executive_phone = CharField(max_length=250, null=True, blank=True, verbose_name='Yetkili Telefon Numarası')
    mersis_no = CharField(max_length=250, null=True, blank=True, verbose_name='Mersis Numarası')
    kep_address = CharField(max_length=250, null=True, blank=True, verbose_name='Kep Adresi')
    tax_office = CharField(max_length=250, null=True, blank=True, verbose_name='Vergi Dairesi')
    tax_number = CharField(max_length=250, null=True, blank=True, verbose_name='Vergi No')
    legal_company_title = CharField(max_length=250, null=True, blank=True, verbose_name='Yasal Şirket Ünvanı')
    iban = CharField(max_length=250, null=True, blank=True, verbose_name='IBAN')
    features = ManyToManyField('djangoecommerce_app.CompanyFeature', verbose_name='Reklamveren Şirket Özellikleri', blank=True)

    class Meta:
        verbose_name = 'Şirket'
        verbose_name_plural = 'Şirketler'


class ProductCategory(Model):
    category = CharField(max_length=255, verbose_name='Ürün Kategorisi')

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Ürün Kategorisi'
        verbose_name_plural = 'Ürün Kategorileri'

    def __str__(self):
        return self.category


class ProductSubCategory(Model):
    owner = ForeignKey('djangoecommerce_app.ProductCategory', related_name='maincategory',blank=False, null=False, verbose_name='Ana Kategori', on_delete=models.CASCADE)
    sub_category = CharField(max_length=255, verbose_name='Ürün Kategorisi')

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Ürün Alt Kategorisi'
        verbose_name_plural = 'Ürün Alt Kategorileri'

    def __str__(self):
        return self.category


class ProductBrand(Model):
    name = CharField(max_length=255, verbose_name='Ürün Markası')

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Ürün Markası'
        verbose_name_plural = 'Ürün Markaları'

    def __str__(self):
        return self.name


class Product(Model):
    name = CharField(max_length=255, verbose_name='Ürün Adı')
    description = TextField(max_length=1000, blank=True, null=True, verbose_name='Açıklama')
    created_at = DateTimeField(auto_now_add=True, editable=False, verbose_name='Oluşturma Tarihi')
    category = ForeignKey('djangoecommerce_app.ProductCategory', blank=True, null=True, verbose_name='Ürün Kategorisi', on_delete=models.CASCADE)
    owner = ForeignKey('djangoecommerce_app.Company', related_name='owner',blank=False, null=False, verbose_name='Ürün Sahibi', on_delete=models.CASCADE)
    brand = ForeignKey('djangoecommerce_app.ProductBrand', related_name='brand',blank=True, null=True, verbose_name='Ürün Markası', on_delete=models.CASCADE)
    price = FloatField(validators=[MinValueValidator(1)],verbose_name='Ürün Fiyatı')
    thumbnail = ImageField(verbose_name='Resimi', upload_to='images/product/', blank=True, null=True)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Ürün'
        verbose_name_plural = 'Ürünler'

    def __str__(self):
        return self.name


class ProductImage(Model):
    image = ImageField(verbose_name='Resim', upload_to='images/product/')
    product = ForeignKey('djangoecommerce_app.Product', verbose_name='Ürün', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Ürün Resmi'
        verbose_name_plural = 'Ürün Resimleri'

    def __str__(self):
        return self.image.name


class ProductStar(Model):
    product = ForeignKey('djangoecommerce_app.Product', verbose_name='Ürün', null=True, blank=True, on_delete=models.CASCADE)
    owner = ForeignKey('djangoecommerce_app.User', verbose_name='Yıldız Veren Kişi', null=True, blank=True, on_delete=models.CASCADE)
    star = FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)],verbose_name='Yıldız')

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Ürün Yıldızı'
        verbose_name_plural = 'Ürün Yıldızları'

    def __str__(self):
        return self.image.name
        verbose_name = 'Reklamveren'
        verbose_name_plural = 'Reklamverenler'


class Coupon(Model):
    code = CharField(max_length=24, verbose_name='Kupon Kodu')
    discount_rate = FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)],verbose_name='İndirim Oranı (Yüzde)')
    guests = ManyToManyField('djangoecommerce_app.User', blank=True, verbose_name='Kullananlar', related_name='guests')
    companies = ManyToManyField('djangoecommerce_app.Company', blank=True, verbose_name='Kullanılabilir Restoranlar',related_name='companies')
    is_active = BooleanField(default=False, verbose_name='Aktif')
    created = DateTimeField(auto_now_add=True, editable=False, verbose_name='Yaratılma Tarihi')
    limit = IntegerField(default=0, verbose_name='Kullanım Adedi')

    def __str__(self):
        return self.code

    def is_exceed(self):
        if self.guests.count() < self.limit:
            return False
        return True

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Kupon'
        verbose_name_plural = 'Kuponlar'



class Card(Model):
    CARD_STATUS = (
        ('DISAPPROVED', 'Onaylanmadı'),
        ('APPROVED', 'Onaylandı'),
        ('REFUNDED', 'Iade Edildi'),
    )
    owner = ForeignKey('djangoecommerce_app.User', verbose_name='Satın Alan Kişi', null=True, blank=True, on_delete=models.CASCADE)
    product = ForeignKey('djangoecommerce_app.Product', verbose_name='Ürün', null=True, blank=True, on_delete=models.CASCADE)
    status = CharField(max_length=128, choices=CARD_STATUS, default='DISAPPROVED', blank=False, verbose_name='Durum')
    transaction_time = DateTimeField(auto_now_add=True, verbose_name='Ödeme Tarihi')
    transaction_total_amount = FloatField(verbose_name='Toplam Ödeme')

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Sepet'
        verbose_name_plural = 'Sepetler'



class Order(Model):
    STATUS_TYPES = (
        ('DISAPPROVED', 'Onaylanmadı'),
        ('APPROVED', 'Onaylandı'),
        ('REFUNDED', 'Iade Edildi'),
    )
    buyer = ForeignKey('djangoecommerce_app.User', verbose_name='Satın Alan', related_name='buyer', on_delete=models.CASCADE)
    card = ManyToManyField('djangoecommerce_app.Card', verbose_name='Sepetteki Ürünler', related_name='card')
    owner = ForeignKey('djangoecommerce_app.Company', verbose_name='Ürün Sahip Firma', related_name='order_owner', on_delete=models.CASCADE)
    coupon = ForeignKey('djangoecommerce_app.Coupon', null=True, blank=True, verbose_name='Kupon', on_delete=models.CASCADE)
    transaction_id = CharField(max_length=128, verbose_name='Ödeme Numarası')
    transaction_time = DateTimeField(auto_now_add=True, verbose_name='Ödeme Tarihi')
    transaction_total_amount = FloatField(verbose_name='Toplam Ödeme')
    status = CharField(max_length=128, choices=STATUS_TYPES, default='DISAPPROVED', blank=False, verbose_name='Durum')


    class Meta:
        ordering = ('-transaction_time',)
        verbose_name = 'Satın Alım'
        verbose_name_plural = 'Satın Alımlar'

    def __str__(self):
        return self.transaction_id


class OrderProductStatus(Model):
    ORDER_STATUS_TYPES = (
        ('EXPECTEDSHIPPED', 'Kargoya verilmesi bekleniyor.'),
        ('INCARGO', 'Ürününüz kargoda.'),
        ('DONE', 'Teslim edildi.'),
    )
    product = ForeignKey('djangoecommerce_app.Card', verbose_name='Ürün', blank=True, on_delete=models.CASCADE)
    status = CharField(max_length=15, choices=ORDER_STATUS_TYPES, default='EXPECTEDSHIPPED', blank=False, verbose_name='Durum')

    class Meta:
        verbose_name = 'Kargo Durumu'
        verbose_name_plural = 'Kargo Durumları'

    def __str__(self):
        return self.id


class OrderProductComment(Model):
    owner = ForeignKey('djangoecommerce_app.User', verbose_name='Yorum Yapan Kişi', related_name='comment_owner', on_delete=models.CASCADE)
    product = ForeignKey('djangoecommerce_app.Card', verbose_name='Ürün', blank=True, on_delete=models.CASCADE)
    comment = TextField(blank=False, null=False, verbose_name='Ürün Yorumu')

    class Meta:
        verbose_name = 'Ürün Yorumu'
        verbose_name_plural = 'Ürün Yorumları'

    def __str__(self):
        return self.id


class Contact(Model):
    name = CharField(max_length=50, verbose_name="Ad Soyad")
    email = EmailField(max_length=50, verbose_name="Mail")
    subject = CharField(max_length=200, verbose_name="Başlık")
    message = TextField(blank=True, null=True, verbose_name='Mesaj')
    created_date = DateTimeField(auto_now=True, verbose_name="Oluşum Tarihi")

    class Meta:
        verbose_name = 'İletişim'
        verbose_name_plural = 'İletişimler'

    def __str__(self):
        return self.subject

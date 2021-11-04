# from django.db import models
# from django.utils.text import slugify
#
# from django.db import models
# from django.utils.text import slugify
#
# class Artikel(models.Model):
#     judul_post = models.CharField(max_length=200, unique=True)
#     body_post = models.TextField()
#     penulis = models.CharField(max_length=100)
#     tanggal_post = models.DateTimeField(auto_now_add=True)
#     slug_post = models.SlugField(max_length=100, blank=True, unique=True)
#
#     def save(self):
#         self.slug_post = slugify(self.judul_post)
#         super(Artikel, self).save()
#
#     def __str__(self):
#         return "{} | {}".format(self.id, self.judul_post)
#
#
# class Kategori(models.Model):
#     nama_kategori = models.CharField(max_length=50, unique=True)
#     slug_kategori = models.SlugField(blank=True, unique=True)
#
#     class META:
#         ordering = ['nama_kategori']
#
#     def save(self):
#         self.slug_kategori = slugify(self.nama_kategori)
#         super().save()
#
#     def __str__(self):
#         return self.nama_kategori

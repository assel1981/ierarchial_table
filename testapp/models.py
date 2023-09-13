from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children',
                            db_index=True, verbose_name='Родительская категория')

        # 'self', null=True, blank=True, on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return self.name

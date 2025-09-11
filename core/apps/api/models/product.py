from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class ProductModel(AbstractBaseModel):
    title = models.CharField(verbose_name=_("Nomi"), max_length=255)
    description = models.TextField(verbose_name=_("Tavsif"), blank=True, null=True)
    category = models.ManyToManyField("api.CategoryModel", blank=True, null=True)
    image = models.CharField(verbose_name=_("Rasm"), max_length=200, blank=True, null=True)
    price = models.DecimalField(verbose_name=_("Narx"), max_digits=12, decimal_places=2, blank=True, null=True)
    

    def __str__(self):
        return str(self.title)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "product"
        verbose_name = _("ProductModel")
        verbose_name_plural = _("ProductModels")

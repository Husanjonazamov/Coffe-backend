from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

PAGES = [
    {
        "seperator": False,
        "items": [
            {
                "title": _("Home page"),
                "icon": "home",
                "link": reverse_lazy("admin:index"),
            }
        ],
    },
    {
        "title": _("Foydalanuvchilar bo'limi"),
        "separator": True,  # Top border
        "items": [
            {
                "title": _("Foydalanuvchilar"),
                "icon": "group",
                "link": reverse_lazy("admin:accounts_user_changelist"),
            },
           
        ],
    },
     {
        "title": _("Mahsulotlar"),
        "separator": True,  # Top border
        "items": [
            {
                "title": _("Coffelar"),
                "icon": "group",
                "link": reverse_lazy("admin:api_productmodel_changelist"),
            },
            {
                "title": _("Kategoryalar"),
                "icon": "group",
                "link": reverse_lazy("admin:api_categorymodel_changelist"),
            },
           
        ],
    },
]

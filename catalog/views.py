from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

SECTIONS = [
    {"name": "Кожа", "slug": "koja", "image": "catalog/img/photo_1.png"},
    {"name": "Игровые рукава", "slug": "rukava", "image": "catalog/img/photo_2.png"},
    {"name": "Одежда", "slug": "odezhda", "image": "catalog/img/photo_3.png"},
    {"name": "Столы", "slug": "stoly", "image": "catalog/img/photo_4.png"},
]

# Create your views here.
def catalog_home(request):
    return render(request, "catalog/catalog_home.html", {"sections": SECTIONS})

def catalog_section(request, section_slug):
    section = get_object_or_404(
        {s["slug"]: s for s in SECTIONS}, section_slug
    )
    # Здесь подгрузи товары section, например, items = Item.objects.filter(section=section_slug)
    items = []  # заменишь на свои товары
    return render(request, "catalog/catalog_section.html", {
        "section": section,
        "items": items
    })
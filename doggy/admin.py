from django.contrib import admin

# Register your models here.
from doggy.models import Animal, Breed, Temper, Address, Colour, Medicament, Vaccination, Health

# class AnimalAdmin(admin.ModelAdmin):
#     pass


class AnimalAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'gender',
                    'breed',
                    'date_of_birth',
                    'health_state',
                    'status',
                    'created']
    ordering = ['address', '-created', 'date_of_birth']
    list_filter = ['address', 'breed']
    search_fields = ['breed', 'address']
    search_help_text = 'Поиск по породе или приюту'

    readonly_fields = ['created']
    fieldsets = [
        ('Имя животного', {
            'classes': 'wide',
            'fields': ['name']
        }),
        ('Подробности', {
            'classes': ['collapse'],  # Поле свернуто
            'description': 'Подробное описание',
            'fields': ['gender',
                       'date_of_birth',
                       'weight',
                       'height',
                       'temper',
                       'image',
                       'type_fur',
                       'colour',
                       'life_story'], },
         ),
        ('Адрес', {
            'fields': ['address']
        }),
        (None, {
            'fields': ['created']
        }),
    ]


admin.site.register(Animal, AnimalAdmin)
admin.site.register(Breed)
admin.site.register(Temper)
admin.site.register(Address)
admin.site.register(Colour)
admin.site.register(Medicament)
admin.site.register(Vaccination)
admin.site.register(Health)


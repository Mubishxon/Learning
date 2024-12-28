from django.contrib import admin
from .models import About, Categories, Carousel, Team, Testimonial, Courses
# Register your models here.
admin.site.register(Carousel)
admin.site.register(Team)
admin.site.register(Testimonial)
admin.site.register(About)
admin.site.register(Categories)

@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}



from django.urls import path
from .views import index, about,  contact,  team, testimonial, courses, blog404, carouseldetail, aboutdetail, categoriesdetail, coursesdetail, teamdetail, testimonialdetail, CoursesUpdateView, CoursesDeleteView, CoursesCreateView
urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('team/', team, name='team'),
    path('testimonial/',  testimonial, name='testimonial'),
    path('courses/', courses, name='courses'),
    path('blog404/', blog404, name='blog404'),
    path('carouseldetail/<int:id>/', carouseldetail, name='carouseldetail'),
    path('aboutdetail/<int:id>/', aboutdetail, name='aboutdetail'),
    path('categoriesdetail/<int:id>/', categoriesdetail, name='categoriesdetail'),
    path('coursesdetail/<slug:courses>/', coursesdetail, name='coursesdetail'),
    path('teamdetail/<int:id>/', teamdetail, name='teamdetail'),
    path('testimonialdetail/<int:id>/', testimonialdetail, name='testimonialdetail'),
    path('courses/edit/<slug>/', CoursesUpdateView.as_view(), name='coursesUpdate'),
    path('courses/delete/<slug>/', CoursesDeleteView.as_view(), name='coursesDelete'),
    path('courses/create', CoursesCreateView.as_view(), name='coursesCreate'),
]
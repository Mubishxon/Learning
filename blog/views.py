from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import About,  Categories, Carousel,  Team, Testimonial, Courses
from .forms import ContactForm
from django.views.generic import UpdateView, CreateView,  DeleteView
from django.urls import reverse_lazy
# Create your views here.
class CoursesUpdateView(UpdateView):
    model = Courses
    fields = ('name', 'bio', 'img', 'price', 'price2')
    template_name = 'CoursesEdit.html'

class CoursesDeleteView(DeleteView):
    model = Courses
    template_name = 'CoursesDelete.html'
    success_url = reverse_lazy('index')

class CoursesCreateView(CreateView):
    model = Courses
    template_name = 'CoursesCreateView.html'
    fields = ('name', 'bio', 'img', 'price', 'price2')

def Coursesdetail(request, courses):
    courses = get_object_or_404(Courses, slug=courses)
    context = {
        'courses': courses
    }
    return render(request, 'coursesDetailView', context=context)

def index(request):
    categories = Categories.objects.all()
    about = About.objects.all()
    courses = Courses.objects.all()
    team = Team.objects.all()
    testimonial = Testimonial.objects.all()
    carousel = Carousel.objects.all()
    contact = ContactForm(request.POST or None)
    if request.method == "POST" and contact.is_valid():
        contact.save()
        return HttpResponse("<h2>So'rovingiz muvaffaqiyatli amalga oshirildi. Rahmat!")
    context = {
        "categories": categories,
        "about": about,
        "carousel": carousel,
        "team": team,
        "testimonial": testimonial,
        "courses": courses,
        "contact": contact
    }
    render(request, 'index.html', context=context)
def about(request):
    about = About.objects.all()
    context = {
        'about': about
    }
    return render(request, 'about.html', context=context)
def courses(request):
    courses = Courses.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'courses.html', context=context)
def contact(request):
    carousel = Carousel.objects.all()
    context = {
        'carousel': carousel
    }
    return render(request, 'contact.html', context=context)
def team(request):
    team = Team.objects.all()
    context = {
        'team': team
    }
    return render(request, 'team.html', context=context)
def testimonial(request):
    testimonial = Testimonial.objects.all()
    context = {
        'testimonial': testimonial
    }
    return render(request, 'testimonial.html', context=context)
def contact(request):
    contact =ContactForm(request.POST or None)
    if request.method == "POST" and contact.is_valid():
        contact.save()
        return HttpResponse("<h2>So'rovingiz muvaffaqiyatli amalga oshirildi. Rahmat!")
    context = {
        "contact": contact
    }
    return render(request, 'contact.html', context=context)
def blog404(request):
    categories = Categories.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'blog404.html', context=context)

def carouseldetail(request, id):
    carousel = Carousel.objects.get(id=id)
    context = {
        'x': carousel
    }
    return render(request, 'carouseldetail.html', context=context)

def categoriesdetail(request, id):
    categories = Categories.objects.get(id=id)
    context = {
        'x': categories
    }
    return render(request, 'categoriesdetail.html', context=context)

def teamdetail(request, id):
    team = Team.objects.get(id=id)
    context = {
        'x': team
    }
    return render(request, 'teamdetail.html', context=context)

def testimonialdetail(request, id):
    testimonial = Testimonial.objects.get(id=id)
    context = {
        'x': testimonial
    }
    return render(request, 'testimonialdetail.html', context=context)

def coursesdetail(request, courses):
    courses = get_object_or_404(Courses, slug=courses)
    context = {
        'courses': courses
    }
    return render(request, 'coursesdetail.html', context=context)

def aboutdetail(request, id):
    about = About.objects.get(id=id)
    context = {
        'x': about
    }
    return render(request, 'aboutdetail.html', context=context)
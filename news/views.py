from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

# Web Scrapping
import requests
from bs4 import BeautifulSoup
from .models import Article
from .forms import *
from datetime import datetime

# Paginator
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Menampilkan template
def news(request):
    global article_index
    filter_form = FilterForm()
    article_form = ArticleForm()
    context = {'filter_form': filter_form, 'article_form': article_form}
    return render(request, 'news.html', context)

# Scrapping website UN News
def scrapping_web_un():
    # Inspiration: https://www.geeksforgeeks.org/extract-json-from-html-using-beautifulsoup-in-python/
    # Cek apakah data article atau tidak
    first_time = not Article.objects.exists()
    # Load data dari halaman 1-8
    for index in range(0, 8):
        if index == 0:
            base_url = "https://news.un.org/en/news/topic/climate-change"
        else:
            base_url = "https://news.un.org/en/news/topic/climate-change?page="+str(index)

        # Request halaman html dan di-parse menjadi struktur tree.
        page = requests.get(base_url)
        soup = BeautifulSoup(page.text, "html.parser")

        # Mengambil setiap article
        articles = soup.find_all('div', attrs={"class": "views-row"})
        # Iterasi setiap article untuk mengambil gambar, judul, text, dan link.
        for article in articles:
            try:
                image = article.find('source', attrs={"media":"(max-width: 991px)"})['srcset']
                link = "https://news.un.org" + article.find('article')['about']
                title = article.find('span', attrs={"class":"field field--name-title field--type-string field--label-hidden"}).text
                date_str = article.find('time', attrs={"class":"datetime"}).text
                date = datetime.strptime(date_str, "%d %B %Y").date()
                region = article.find('div', attrs={"class":"field field--name-field-news-region field--type-entity-reference field--label-hidden field__items"}).text.strip('\n')
                description = article.find('div', attrs={"class":"node__content clearfix"}).text.strip('\n')

                if first_time:
                    # Menyimpan objek article
                    article_obj = Article(admin_created=False, image=image, link=link, title=title, date=date, region=region, description=description)
                    article_obj.save()
                else:
                    # Menyimpan objek article yang belum di-update
                    latest_article = Article.objects.filter(admin_created=False).order_by("-date")[0]

                    if latest_article.title != title:
                        article_obj = Article(admin_created=False, image=image, link=link, title=title, date=date, region=region, description=description)
                        article_obj.save()
                    else:
                        return
            except:
                continue

# Inisiasi article pertama kali berbentuk json
def init_articles(request):
    if request.method == 'GET':
        # Mengambil data dari website UN News
        #Article.objects.all().delete()
        scrapping_web_un()

        # Membuat paginator
        articles = Article.objects.order_by("-date")
        paginator = Paginator(articles, 10)
        page_end = paginator.num_pages

        articles = Article.objects.order_by("-date")[0:10]
        return HttpResponse("["+serializers.serialize("json", articles)+", "+str(page_end)+"]", content_type="application/json")
    return HttpResponse('')

# Menampilkan article sesuai region berbentuk json
def show_articles(request):
    if request.method == "GET":
        region = request.GET.get('region')

        # Membuat paginator
        # Inspiration: https://stackoverflow.com/questions/62305524/how-to-do-ajax-pagination-in-django
        if region == 'all': 
            articles = Article.objects.all().order_by("-date")
        else:
            articles = Article.objects.filter(region__icontains=region).order_by("-date")
        paginator = Paginator(articles, 10)
        page_end = paginator.num_pages
        page_num = int(request.GET.get('page_num', 1))
        start = (page_num-1)*10
        end = page_num*10

        if region == 'all': 
            articles = Article.objects.all().order_by("-date")[start:end]
        else:
            articles = Article.objects.filter(region__icontains=region).order_by("-date")[start:end]

        return HttpResponse("["+serializers.serialize("json", articles)+", "+str(page_end)+"]", content_type="application/json")
    return HttpResponse('')

# Menambah article
def add_article(request):
    if request.method == "POST":
        form = ArticleForm()
        instance = form.save(commit=False)
        instance.admin_created = True
        instance.image = ""
        instance.link = ""
        instance.title = request.POST.get('title')
        instance.region = " ".join(word.capitalize() for word in request.POST.get('region').split(" "))
        instance.description = request.POST.get('description')
        instance.save()
        return HttpResponse('')
    return HttpResponse('')

# Delete article
def delete_article(request, id):
    if request.method == "DELETE":
        article = Article.objects.get(pk=id)
        article.delete()

        articles = Article.objects.all().order_by("-date")[0:2]
        return HttpResponse(serializers.serialize("json", articles), content_type="application/json")
    return HttpResponse('')

def json(request):
    if request.method == 'GET':
        articles = Article.objects.all().order_by("-date")
        return HttpResponse(serializers.serialize("json", articles), content_type="application/json")
    return HttpResponse('')
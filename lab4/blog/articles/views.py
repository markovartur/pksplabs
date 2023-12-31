from articles.models import Article
from django.shortcuts import render

def archive(request):
	return render(request, 'archive.html', {"posts":Article.objects.all()})
	
def get_article(request, article_id):
	try:
		post = Article.objects.get(id=article_id)
		return render(request, 'article.html', {"post": post})
	except Article.DoesNotExist:
		raise Http404
		

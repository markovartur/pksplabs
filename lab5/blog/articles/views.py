from articles.models import Article
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required

def archive(request):
	return render(request, 'archive.html', {"posts":Article.objects.all()})
	
def get_article(request, article_id):
	try:
		post = Article.objects.get(id=article_id)
		return render(request, 'article.html', {"post": post})
	except Article.DoesNotExist:
		raise Http404
		
def create_article(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			form = {'text': request.POST["text"],'title': request.POST["title"]}
			if form["text"] and form["title"]:
				if len(Article.objects.filter(title=form["title"])) == 0:
					article = Article.objects.create(text=form["text"],title=form["title"],
					author=request.user)
					return redirect('get_article', article_id=article.id)
				else:
					form['errors'] = "Статья с таким названием уже есть"
					return render(request, 'create_article.html', {'form': form})
			else:
				form['errors'] = "Не все поля заполнены"
				return render(request, 'create_article.html', {'form': form})
		else:
			return render(request, 'create_article.html', {})
	else:
		raise Http404
		

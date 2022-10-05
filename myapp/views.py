from django.shortcuts import render, HttpResponse
import random
# Create your views here.
topics = [
    {'id':1, 'title':'routing','body':'routing is...'},
    {'id':2, 'title':'view','body':'view is...'},
    {'id':3, 'title':'model','body':'model is...'}
]
def HTMLtemplate(articleTag):
    global topics
    ol=''
    for topic in topics:
        ol+=f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return HttpResponse(f'''
    <html>
    <body>
        <h1><a href="/">Django</a></h1>
        <ol>
            {ol} 
        </ol>
        {articleTag}
        <ul>
        <li></li>
        <li><a href = "/create">create</a></li>
        <li></li>
        </ul>
    </body>    
    </html>
    ''')

def index(request):
    article='''
    <h2>Welcome</h2>
    Hello, Django! Here is homepage.
    '''
    return HttpResponse(HTMLtemplate(article))

def create(request):
    return HttpResponse('Welcome create page!')

def read(request, id):
    global topics
    for topic in topics:
        if topic['id']==int(id):
            title=topic['title']
            body=topic['body']
            break
    
    article=f'''
    <h2>{title}</h2>
    {body}
    
    '''
    return HttpResponse(HTMLtemplate(article))
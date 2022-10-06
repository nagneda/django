from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
import random
# Create your views here.
nextid=4
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
        <li><a href="">update</a></li>
        <li><a href = "/create/">create</a></li>
        <li><a href="">delete</a></li>
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

@csrf_exempt
def create(request):
    
    if request.method=='GET':
        article='''
        <form action="/create/" method="POST">
            <p><input type="text" name="title" placeholder="Enter the title.."></p>
            <p><textarea name="body" placeholder="body"></textarea></p>
            <p><input type="submit" value="제출!"></p>
        </form>
        '''
        return HttpResponse(HTMLtemplate(article))
    elif request.method=='POST':
        global nextid
        title=request.POST['title'] # request.POST는 FORM태그에서 전송한 데이터를 딕셔너리형태로 저장하고 있음.
        body=request.POST['body']# flask의 request.form과 같은 뜻임.
        topics.append({'id':nextid,'title':title,'body':body})
        url='/read/'+str(nextid)
        nextid+=1
        return redirect(url)
    
    

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
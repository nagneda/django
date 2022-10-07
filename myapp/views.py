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


def HTMLtemplate(articleTag, id=None):
    contextUI=''
    if id!=None:
        contextUI=f'''
        <li><a href="/update/{id}/">update</a></li>
        <li>
            <form action="/delete/" method="POST">
                <input type="hidden" name="id" value={id}>
                <input type="submit" value="delete">
            </form>
        </li>
        '''
    # flask에서는 hidden form tag없이 form 태그를 delete/{id}의 형태로 줬고 route값도 delete/<int:id>/ 였음.
    # 어차피 id값을 갖고 있으니 delete클릭시 id 파라미터로 넘기고 delete route에서 해당id삭제 django때와 flask때가 방법은 다르지만
    # 둘 다 동작은 할 것 같다.  
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
        <li><a href = "/create/">create</a></li>
        {contextUI}
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
        nextid+=1
        return redirect(f'/read/{nextid-1}')# nextid 증감전에 변수만들고 redirect '변수명'해도 상관없음.

@csrf_exempt
def update(request, id):
     if request.method=='GET':
        global topics
        for topic in topics:
            if topic['id']==int(id):
                title=topic['title']
                body=topic['body']
        article=f'''
        <form action="/update/{id}/" method="POST">
            <p><input type="text" name="title" value={title}></p>
            <p><textarea name="body" placeholder="body">{body}</textarea></p>
            <p><input type="submit" value="수정!"></p>
        </form>
        '''
        return HttpResponse(HTMLtemplate(article))

     elif request.method=='POST':
        for topic in topics:
            if topic['id']==int(id):
                topic['title']=request.POST['title']
                topic['body']=request.POST['body']
                break
        return redirect(f'/read/{id}/')# nextid 증감전에 변수만들고 redirect '변수명'해도 상관없음.
@csrf_exempt
def delete(request):
    global topics
    if request.method=="POST":
        id = request.POST['id']
        for topic in topics:
            if topic['id']==int(id):
                topics.remove(topic)
                break
    
    return redirect('/')

    

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
    return HttpResponse(HTMLtemplate(article,id))

    
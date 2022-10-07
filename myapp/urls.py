
from django.urls import path
from myapp import views
urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('read/<id>/', views.read),
    path('delete/', views.delete),
    path('update/<id>/', views.update)
]
# myproject urls.py의 파일에서 myapp urls.py로 넘어옴.위의 urlpatterens의 리스트 내역은 flask의 @app.route의 url주소 나타내는 형태.
# 다만 라우터마다 함수가 지정돼있지는 않고 urls.py에 작성된 함수를 골라서 사용할 수 있는 모습. flask에서는 공통적으로 사용하려는 함수는
# 밖으로 빼놔야 라우터에서 공통 사용이 가능했다. 불러올 함수 형태는 파일명.함수명(views.index) > views.py의 views, views.py의 index함수를 불러오겠다는 것
from django.urls import path
from main.views import show_main, create_product, show_xml, show_json, show_json_by_id, show_xml_by_id
from main.views import register, login_user, logout_user, hapus, tambah, kurang, get_product_json, add_product_ajax
from main.views import *
app_name = 'main'

#url untuk app main
urlpatterns = [
    #url homepage app main
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name = 'show_xml'),
    path('json/', show_json, name = 'show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'), 
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('hapus/<int:id>/', hapus, name ='hapus'),
    path('tambah/<int:id>/', tambah, name ='tambah'),
    path('kurang/<int:id>/', kurang, name ='kurang'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-ajax/', add_product_ajax, name='add_product_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]
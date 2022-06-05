from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register_page,name='register'),
    path('cash-man/',views.cash_male_page,name='cash-man'),
    path('cash-woman/',views.cash_woman_page,name='cash-woman'),
    path('total-cash',views.total_cash,name='total-cash'),
    path('cash-man/<pk>/delete/',views.deleteman.as_view(template_name='app/delete.html'),name='delete-man'),
    path('cash-woman/<pk>/delete/',views.deletewoman.as_view(template_name='app/delete2.html'),name='delete-woman'),
    path('delete-all/',views.delete_all,name='delete-all'),
    path('delete-all-woman/',views.delete_all_woman,name='delete-all-woman')

]

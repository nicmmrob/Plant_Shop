from django.urls import path
from plants import views as plants_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', plants_views.index, name='index'),
    path('api/plants/', plants_views.plant_list),
    path('api/plants/<int:pk>/', plants_views.plant_detail),
    path('api/plants/published/', plants_views.plant_list_published)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
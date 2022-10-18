from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('kotxeak/', views.kotxeak, name='kotxeak'),
    path('kotxeak/add/', views.addkotxe, name='addkotxe'),
    path('kotxeak/add/addrecord/', views.addrecordkotxe, name='addrecordkotxe'),
    path('kotxeak/delete/<int:id>', views.deletekotxe, name='deletekotxe'),
    
    path('pertsonak/', views.pertsonak, name='pertsonak'),
    path('pertsonak/add/', views.addpertsona, name='addpertsona'),
    path('pertsonak/add/addrecord/', views.addrecordpertsona, name='addrecordpertsona'),
    path('pertsonak/delete/<int:id>', views.deletepertsona, name='deletepertsona'),
    
    path('kotxeak/alokatu/', views.kotxeaalokatu, name='kotxeaalokatu'),
    path('kotxeak/alokatu/todb/', views.kotxeaalokatutodb, name='kotxeaalokatutodb'),
    path('kotxeak/alokatu/amaitu/<int:id>', views.alokatuamaitu, name='alokatuamaitu'),
]
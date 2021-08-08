from django.contrib import admin
from django.urls import path
from resume_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomeView.as_view(), name='home'),
    path('<int:pk>', views.CandidateView.as_view(), name='candidate'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
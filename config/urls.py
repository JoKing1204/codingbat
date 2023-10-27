from django.contrib import admin
from django.urls import path

from app.views import warmup_1, warmup_2, string_2, logic_2

urlpatterns = [
    path("Warmup-1/<int:n>/", warmup_1),
    path("Warmup-2/<str:res>/", warmup_2),
    path("String-2/<str:c>/", string_2),
    path("Logic-2/<int:a>/<int:b>/<int:c>/", logic_2),
    path("admin/", admin.site.urls),
]

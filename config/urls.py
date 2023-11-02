from django.contrib import admin
from django.urls import path

from app.views import warmup_1, warmup_2, string_2, logic_2

urlpatterns = [
    path("Warmup-1/near-hundred/<int:n>/", warmup_1),
    path("Warmup-2/String-Splosion/<str:res>/", warmup_2),
    path("String-2/cat-dog/<str:c>/", string_2),
    path("Logic-2/lone-sum/<int:a>/<int:b>/<int:c>/", logic_2),
    path("admin/", admin.site.urls),
]

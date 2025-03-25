from django.views.generic import View
from .mixins import JsonResponseMixin, ObjectMixin, UserPermissionMixin
from django.contrib.auth.models import User  # Імпортуємо модель User
from django.http import HttpResponse

class MyView(JsonResponseMixin, ObjectMixin, UserPermissionMixin, View):
    model = User  # Тепер модель User визначена

    def get(self, request, *args, **kwargs):
        # Перевірка прав доступу
        self.check_permission(request.user)

        # Отримання об'єкта
        user = self.get_object(kwargs['pk'])

        # Повернення JSON відповіді
        return self.render_json({'username': user.username})

class AnotherView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, world!")

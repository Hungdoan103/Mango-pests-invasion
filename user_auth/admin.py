from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Đăng ký User mặc định với giao diện quản trị được tùy chỉnh
# (Sẽ sử dụng User mặc định thay vì CustomUser để đơn giản)

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

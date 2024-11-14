from django.shortcuts import redirect
from .models import UserProfile

def doctor_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login_doctor')  # Перенаправляє на сторінку авторизації лікаря
        
        profile = UserProfile.objects.filter(user=request.user).first()
        if profile is None or profile.role != 'doctor':
            return redirect('home')  # Або сторінка з повідомленням про помилку

        return view_func(request, *args, **kwargs)
    return _wrapped_view

def pharmacist_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login_pharmacist')  # Перенаправляє на сторінку авторизації аптекаря
        
        profile = UserProfile.objects.filter(user=request.user).first()
        if profile is None or profile.role != 'pharmacist':
            return redirect('home')  # Або сторінка з повідомленням про помилку

        return view_func(request, *args, **kwargs)
    return _wrapped_view

def patient_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login_patient')  # Перенаправляє на сторінку авторизації пацієнта
        
        profile = UserProfile.objects.filter(user=request.user).first()
        if profile is None or profile.role != 'patient':
            return redirect('home')  # Або сторінка з повідомленням про помилку

        return view_func(request, *args, **kwargs)
    return _wrapped_view
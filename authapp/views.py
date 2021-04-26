from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.contrib import auth
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, UpdateView
from django.contrib import messages


from authapp.models import User, UserProfile
from basketapp.models import Basket
from authapp.forms import UserRegisterForm, UserLoginForm, UserEditForm, UserProfileEditForm


class LoginFormView(LoginView):
    model = User
    success_url = '/'
    template_name = 'authapp/login.html'
    form_class = UserLoginForm
    title = 'Авторизация'


class RegisterListView(FormView):
    model = User
    template_name = 'authapp/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('auth:login')

    def get_context_data(self, **kwargs):
        context = super(RegisterListView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Регистрация'
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = form.save()
            if self.send_verify_mail(user):
                messages.success(request, 'Вы успешно зарегистрировались!'
                                          ' Для авторизации профиля пройдите по ссылке направленной '
                                          'на электронную почту ')
                return redirect(self.success_url)

            return redirect(self.success_url)

        return render(request, self.template_name, {'form': form})

    def send_verify_mail(self, user):
        verify_link = reverse_lazy('authapp:verify', args=[user.email, user.activation_key])

        title = f'Для активации учетной записи {user.username} пройдите по ссылке'

        messages = f'Для подтверждения учетной записи {user.username} пройдите по ссылке: \n{settings.DOMAIN_NAME}' \
                   f'{verify_link}'

        return send_mail(title, messages, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)

    def verify(self, email, activation_key):
        try:
            user = User.objects.get(email=email)
            if user.activation_key == activation_key and not user.is_activation_key_expires():
                user.is_active = True
                user.save()
                auth.login(self, user)
                return render(self, 'mainapp/index.html')
            else:
                print(f'error activation user: {user}')
                return render(self, 'authapp/verification.html')
        except Exception as e:
            print(f'error activation user : {e.args}')
            return HttpResponseRedirect(reverse('index'))


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


class ProfileEdit(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserEditForm
    form_class_second = UserProfileEditForm
    success_url = reverse_lazy('auth:profile')
    template_name = 'authapp/profile.html'

    def get_object(self):
        return get_object_or_404(User, pk=self.request.user.pk)

    def get_context_data(self, **kwargs):
        context = super(ProfileEdit, self).get_context_data(**kwargs)

        self_pk = self.object.pk
        user = User.objects.get(pk=self_pk)
        context['profile_form'] = self.form_class_second(instance=user.userprofile)
        context['baskets'] = Basket.objects.filter(user=user)
        return context

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        user = User.objects.get(pk=self.request.user.pk)
        edit_form = UserEditForm(data=request.POST, files=request.FILES, instance=user)
        profile_form = UserProfileEditForm(data=request.POST, files=request.FILES, instance=user.userprofile)

        if edit_form.is_valid() and profile_form.is_valid():
            edit_form.save()
            user.userprofile.save()
            return HttpResponseRedirect(self.success_url)

        return render(request, self.template_name, {
            'form': edit_form,
            'profile_form': profile_form,
        })

from django.contrib.auth.base_user import BaseUserManager

class CustomUser(BaseUserManager):
    use_in_migrations=True

    def create_user(self,email,user_name,first_name,password,**extra_fields):
        if not email:
            raise ValueError('The must provide email address')
        email = self.normalize_email(email)
        user = self.model(email=email,user_name=user_name,first_name=first_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,user_name,first_name,password,**extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser must have is_sactive=True.')

        return self.create_user(email,user_name,first_name,password,**extra_fields)
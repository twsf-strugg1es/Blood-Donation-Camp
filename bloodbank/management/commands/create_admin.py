from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Delete all admin users and create a new admin user'

    def handle(self, *args, **options):
        # Delete all existing superusers
        superusers = User.objects.filter(is_superuser=True)
        superuser_count = superusers.count()
        
        if superuser_count > 0:
            superusers.delete()
            self.stdout.write(
                self.style.WARNING(f'Deleted {superuser_count} existing admin user(s)')
            )
        else:
            self.stdout.write('No existing admin users found')
        
        # Create new admin user
        admin_email = 'admin@email.com'
        admin_password = '123456'
        
        # Check if admin already exists (in case of duplicate attempts)
        if User.objects.filter(username=admin_email).exists():
            self.stdout.write(self.style.ERROR(f'Admin user {admin_email} already exists!'))
            return
        
        # Create superuser
        admin_user = User.objects.create_superuser(
            username=admin_email,
            email=admin_email,
            password=admin_password,
            first_name='Admin',
            last_name='User'
        )
        
        self.stdout.write(
            self.style.SUCCESS(
                f'\n✓ Successfully created new admin user!\n'
                f'Email: {admin_email}\n'
                f'Password: {admin_password}\n'
                f'Login at: http://127.0.0.1:8000/admin/'
            )
        )

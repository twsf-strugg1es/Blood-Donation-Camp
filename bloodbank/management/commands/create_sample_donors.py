from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from bloodbank.models import UserProfile

class Command(BaseCommand):
    help = 'Create sample blood donors with 5 donors for each blood group'

    def handle(self, *args, **options):
        blood_groups = ['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-']
        zones = ['North', 'South', 'East', 'West', 'Central']
        
        donor_count = 0
        
        for blood_group in blood_groups:
            for i in range(1, 6):  # Create 5 donors for each blood group
                email = f'donor_{blood_group.replace("+", "plus").replace("-", "minus")}_{i}@bloodbank.com'
                username = f'donor_{blood_group.replace("+", "plus").replace("-", "minus")}_{i}'
                
                # Check if user already exists
                if User.objects.filter(username=username).exists():
                    self.stdout.write(f'User {username} already exists, skipping...')
                    continue
                
                # Create user
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password='donor123',
                    first_name=f'Donor',
                    last_name=f'{blood_group} {i}'
                )
                
                # Create profile
                zone = zones[(donor_count) % len(zones)]
                profile = UserProfile.objects.create(
                    user=user,
                    phone_number=f'9{8000000 + donor_count:07d}',
                    age=20 + (i % 45),
                    address=f'{i} {blood_group} Street, {zone}',
                    gender='Male' if donor_count % 2 == 0 else 'Female',
                    zone=zone,
                    blood=blood_group,
                    is_donor=True,
                    working_zone=zone
                )
                
                donor_count += 1
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Created donor: {username} ({blood_group}) in {zone} zone'
                    )
                )
        
        self.stdout.write(
            self.style.SUCCESS(f'\nSuccessfully created {donor_count} sample donors!')
        )

from django.core.management.base import BaseCommand
from bloodbank.models import BloodBankInfo

class Command(BaseCommand):
    help = 'Create sample blood bank inventory for all zones'

    def handle(self, *args, **options):
        zones = ['North', 'South', 'East', 'West', 'Central']
        
        for zone in zones:
            # Check if blood bank already exists for this zone
            if BloodBankInfo.objects.filter(branch_zone=zone).exists():
                self.stdout.write(f'Blood bank for {zone} zone already exists, skipping...')
                continue
            
            # Create blood bank with initial inventory (50 units per blood type)
            blood_bank = BloodBankInfo.objects.create(
                branch_zone=zone,
                a_positive=50,
                a_negative=30,
                b_positive=50,
                b_negative=30,
                o_positive=60,  # O+ is universal donor, so more stock
                o_negative=40,
                ab_positive=25,
                ab_negative=20
            )
            
            self.stdout.write(
                self.style.SUCCESS(
                    f'Created blood bank for {zone} zone with initial inventory'
                )
            )
        
        self.stdout.write(
            self.style.SUCCESS(f'\nSuccessfully initialized blood bank inventory for all zones!')
        )

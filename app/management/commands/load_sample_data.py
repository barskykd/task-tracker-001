import base64

from django.core.management.base import BaseCommand
from django.core.management import call_command
from allauth.socialaccount.models import SocialApp
from app.models import Task

# Obfuscated to circumvent github detection.
SAMPLE_CLIENT_ID=b'OTUwMjIyOTM0MzM1LXIwb3Q1b2k3ZnRrM21pOGNma3A4dWppOWJiMXU2ZzE5LmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29t'
SAMPLE_CLIENT_KEY=b'R09DU1BYLVh4UlFFVWtMZEgxMXZHT0ZGbk50WVpSVWVIVXk='

class Command(BaseCommand):
    help = "Load sample data if database is empty"

    def handle(self, *args, **options):
        if Task.objects.count() == 0:
            call_command("loaddata", "sample_data.json")
            obj = SocialApp.objects.create(
                provider="google",
                provider_id="",
                name="Google",
                client_id=base64.b64decode(SAMPLE_CLIENT_ID).decode(),
                secret=base64.b64decode(SAMPLE_CLIENT_KEY).decode()                
                )
            obj.sites.set([1])

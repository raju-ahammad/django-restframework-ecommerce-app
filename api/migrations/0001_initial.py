
# Create your tests here.
from api.user.models import CustomUser
from django.db import migrations


class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(name="raju", 
                          email="raju@gmail.com", 
                          is_staff=True, 
                          is_superuser=True, 
                          phone="01722863302", 
                          gender="Male"
                          )
        user.set_password("Ra123456")
        user.save()
        
    dependencies = [
        
    ]    
    
    operations = [
        migrations.RunPython(seed_data),
    ]    

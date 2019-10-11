from django.db import models

# Create your models here.
#title
#pub_date
#body
#images
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

#Add blog app settings
#create a migration
#migration
#add to admin

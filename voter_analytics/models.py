# vote_analytics/models.py
from django.db import models
from django.conf import settings

# Create your models here.

class Voter(models.Model):
    ''' Encapsulates our voter model '''
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    street_number = models.CharField(max_length=10)
    street_name = models.CharField(max_length=100)
    apartment_number = models.CharField(max_length=10, blank=True)
    zip_code = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    date_of_registration = models.DateField()
    party_affiliation = models.CharField(max_length=50)
    precinct_number = models.CharField(max_length=100)
    v20state = models.BooleanField()
    v21town = models.BooleanField()
    v21primary = models.BooleanField()
    v22general = models.BooleanField()
    v23town = models.BooleanField()
    voter_score = models.IntegerField()


    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.precinct_number}"
    
def load_data():
    ''' Load data records from CSV file into Django model instances. '''

    Voter.objects.all().delete()  # we clear existing records

    filename = '/Users/yuribychkov/Desktop/django/newton_voters.csv'  # Update with your CSV file path
    with open(filename) as f:
        f.readline()  # discard headers
        for line in f:
            try:
                line = line.strip()
                fields = line.split(',')

                # Strip whitespace and remove any unwanted characters
                fields = [field.strip().replace('“', '').replace('”', '') for field in fields]

                # create an  instance of Voter object
                voter = Voter(
                    last_name=fields[1],
                    first_name=fields[2],
                    street_number=fields[3],
                    street_name=fields[4],
                    apartment_number=fields[5],
                    zip_code=fields[6],  # make sure this is treated as a string
                    date_of_birth=fields[7],  # make sure this is in YYYY-MM-DD format
                    date_of_registration=fields[8],  # make sure this is in YYYY-MM-DD format
                    party_affiliation=fields[9].strip(),
                    precinct_number=fields[10].strip(), 
                    v20state=fields[11].strip().upper() == 'TRUE',
                    v21town=fields[12].strip().upper() == 'TRUE',
                    v21primary=fields[13].strip().upper() == 'TRUE',
                    v22general=fields[14].strip().upper() == 'TRUE',
                    v23town=fields[15].strip().upper() == 'TRUE',
                    voter_score=int(fields[16]),
                )
                voter.save()  # save our instance to the database
                print(f'Created voter: {voter}')
            except Exception as e:
                print(f"Exception on {fields}: {e}")  # print the exception message
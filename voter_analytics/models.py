# vote_analytics/models.py
from django.db import models
import csv
import os
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
        filename = '/Users/yuribychkov/Desktop/django/newton_voters.csv'
        with open(filename) as f:
            f.readline()  # discard headers
            for line in f:
                line = line.strip()
                fields = line.split(',')
                # show which value in each field

                # create instance of Vote object
                voter = Voter(
                    last_name=fields[0],
                    first_name=fields[1],
                    street_number=fields[2],
                    street_name=fields[3],
                    apartment_number=fields[4],
                    zip_code=fields[5],
                    date_of_birth=fields[6],
                    date_of_registration=fields[7],
                    party_affiliation=fields[8],
                    precinct_number=fields[9],
                    v20state=fields[10] == 'True',
                    v21town=fields[11] == 'True',
                    v21primary=fields[12] == 'True',
                    v22general=fields[13] == 'True',
                    v23town=fields[14] == 'True',
                    voter_score=fields[15],
                )
                print(f'Created voter: {voter}')
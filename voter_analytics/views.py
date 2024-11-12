# voter_analytics/views.py

# Create your views here.
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import * # import all of the models
from django.db.models.query import QuerySet
from typing import Any

import plotly
import plotly.graph_objects as go
import plotly.offline as pyo
from django.db.models import Count

# Create your views here.
class VoterListView(ListView):
    model = Voter
    template_name = 'voter_analytics/voter_list.html'
    context_object_name = 'voters'
    paginate_by = 100

    def get_queryset(self):
        qs = super().get_queryset()

        # filter by party affiliation
        party_affiliation = self.request.GET.get('party_affiliation')
        if party_affiliation:
            qs = qs.filter(party_affiliation=party_affiliation)

        # filter by minimum date of birth
        min_dob = self.request.GET.get('min_dob')
        if min_dob:
            qs = qs.filter(date_of_birth__gte=min_dob)

        # filter by maximum date of birth
        max_dob = self.request.GET.get('max_dob')
        if max_dob:
            qs = qs.filter(date_of_birth__lte=max_dob)

        # filter by voter score
        voter_score = self.request.GET.get('voter_score')
        if voter_score:
            qs = qs.filter(voter_score=voter_score)

        # filter by voted in elections
        voted_in_elections = self.request.GET.getlist('voted_in_elections')
        if voted_in_elections:
            qs = qs.filter(voted_in_elections__in=voted_in_elections)

        return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['years'] = list(range(1900, 2024))
        return context
        

class VoterDetailView(DetailView):
    ''' Display a single Voter on an individual page '''
    template_name = 'voter_analytics/voter_detail.html'
    model = Voter
    context_object_name = 'voter'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ''' Add more context data if we want '''
        context = super().get_context_data(**kwargs)
        voter = context['voter'] # get voter object

        # add google maps
        context['google_maps_link'] = f"https://www.google.com/maps/search/?api=1&query={voter.street_number}+{voter.street_name},+{voter.zip_code}"
        return context
    

class GraphsView(ListView):
    model = Voter
    template_name = 'voter_analytics/graphs.html'
    context_object_name = 'voters'
    paginate_by = 100

    def get_queryset(self):
        qs = super().get_queryset()

        # filter by party affiliation
        party_affiliation = self.request.GET.get('party_affiliation')
        if party_affiliation:
            qs = qs.filter(party_affiliation=party_affiliation)

        # filter by minimum date of birth
        min_dob = self.request.GET.get('min_dob')
        if min_dob:
            qs = qs.filter(date_of_birth__gte=min_dob)

        # filter by maximum date of birth
        max_dob = self.request.GET.get('max_dob')
        if max_dob:
            qs = qs.filter(date_of_birth__lte=max_dob)

        # filter by voter score
        voter_score = self.request.GET.get('voter_score')
        if voter_score:
            qs = qs.filter(voter_score=voter_score)

        # filter by voted in elections
        voted_in_elections = self.request.GET.getlist('voted_in_elections')
        if voted_in_elections:
            qs = qs.filter(voted_in_elections__in=voted_in_elections)

        return qs
        

    def get_context_data(self, **kwargs):
        ''' '''
        context = super().get_context_data(**kwargs)
        voters = self.get_queryset() # filtered voters

        # https://forum.djangoproject.com/t/how-to-count-model-objects-based-on-date/19761
        # need to count the seperate ids 

        # birth year (bar)
        year_data = voters.values('date_of_birth__year').annotate(count=Count('id'))
        context['year_chart'] = plotly.offline.plot({
            'data': [go.Bar(
                x=[d['date_of_birth__year'] for d in year_data], 
                y=[d['count'] for d in year_data])],
            'layout': go.Layout(
                xaxis_title="Birth Year", 
                yaxis_title="Number of Voters"
                )
        }, output_type='div', auto_open=False)

        # party affiliation (pie)
        party_data = voters.values('party_affiliation').annotate(count=Count('id'))
        context['party_chart'] = plotly.offline.plot({
            'data': [go.Pie(
                labels=[d['party_affiliation'] for d in party_data], 
                values=[d['count'] for d in party_data])],
        }, output_type='div', auto_open=False)

        # elections (bar)
        election_counts = { '2020 State': voters.filter(v20state=True).count(), 
                            '2021 Primary': voters.filter(v21primary=True).count(), 
                            '2021 Town': voters.filter(v21town=True).count(), 
                            '2022 General': voters.filter(v22general=True).count(), 
                            '2023 Town': voters.filter(v23town=True).count()}
        context['election_chart'] = plotly.offline.plot({
            'data': [go.Bar(
                x=list(election_counts.keys()), 
                y=list(election_counts.values()))],
            'layout': go.Layout(
                xaxis_title="Election", 
                yaxis_title="Number of Voters")
        }, output_type='div', auto_open=False)

        # easier for dropdown if we just add it here
        context['years'] = list(range(1900, 2024))
        return context
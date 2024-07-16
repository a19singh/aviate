import json
import logging

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status, serializers
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from django.core import serializers as django_serializers
from rest_framework.views import APIView
from django.db.models import Case, When, Value, IntegerField

from .models import Applicant
from .serializers import ApplicantSerializer

class ApplicantView(viewsets.ModelViewSet):
    """
    A ViewSet for listing, retrieving, creating, updating, and deleting application instances.

    ## Endpoints

    - `GET /names/` - List all names.
    - `GET /names/{id}/` - Retrieve a specific name by ID.
    - `POST /names/` - Create a new name.
    - `PATCH /names/{id}/` - Partially update a specific name by ID.
    - `DELETE /names/{id}/` - Delete a specific name by ID.

    ## Responses

    ### Success

    - **200 OK**: For successful retrieval and updates.
    - **201 Created**: For successful creation.
    - **204 No Content**: For successful deletion.

    ### Error

    - **400 Bad Request**: If the request data is invalid.
    - **404 Not Found**: If the specified Name instance does not exist.
    """
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ["email", "contact", "name"]
    filterset_fields = {
        "email": ["exact"],
        "name": ["icontains"],
        "contact": ["exact"],
        "age": ["gte", "lte"],
        "experience": ["gte", "lte"],
        "expected_salary": ["gte", "lte"],
    }

class ApplicantSortedView(APIView):
    """
    An APIView for listing, all application with respect to a relevance based search.

    ## Endpoints

    - `GET /names/` - List all names.

    ## Responses

    ### Success

    - **200 OK**: For successful retrieval and updates.

    ### Error

    - **400 Bad Request**: If the request data is invalid.
    - **404 Not Found**: If the specified Name instance does not exist.
    """
    def get(self, request, **kwargs):
        try:
            query = request.GET['name']
            query_words = query.lower().split()
            # Exact match case
            exact_match = Case(
                When(name__iexact=query, then=Value(1)),
                default=Value(0),
                output_field=IntegerField()
            )
            # Partial match cases
            partial_matches = [
                Case(
                    When(name__icontains=word, then=Value(1)),
                    default=Value(0),
                    output_field=IntegerField()
                )
                for word in query_words
            ]

            # Sum of partial matches
            partial_match_sum = partial_matches[0]
            for partial_match in partial_matches[1:]:
                partial_match_sum += partial_match

            # Adding two temp fields for filteration namely exact and partial match
            # then ordering the results by the temp fields
            queryset = Applicant.objects.annotate(
                exact_match=exact_match,
                partial_match=partial_match_sum
            ).order_by('-exact_match', '-partial_match')

            serializer = ApplicantSerializer(queryset, many=True)
            return Response(serializer.data, status=200)
        except KeyError as e:
            return Response({"message": "A search param 'name' is required."}, status=400)

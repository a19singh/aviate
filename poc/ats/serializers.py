import logging
import re

from rest_framework import serializers
from .models import Applicant 

logger = logging.getLogger(__name__)

class ApplicantSerializer(serializers.ModelSerializer):
    """
    Serializer to validate Applicant models values.
    """
    
    class Meta:
        model = Applicant
        fields = '__all__'

    def update(self, instance, validated_data):
        """
        Overwritten update method to allow updates to the 'status' field only.

        This method restricts updates to the 'status' field of the Name instance.
        All other fields will remain unchanged.
        If the 'status' field is not provided in the request,
        a validation error will be raised which 
        in turn will return a 400 Bad Request response. 
        """
        # checking only a single key should be coming
        # if that single key is not status key then raise validation error
        if not (len(validated_data) == 1 and validated_data.get('status')):
            raise serializers.ValidationError({
                "message": "Only application status can be updated"
            })
        return super().update(instance, validated_data)


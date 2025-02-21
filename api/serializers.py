from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    college_email = serializers.EmailField()
    college_roll_number = serializers.CharField()
    input_string = serializers.CharField()

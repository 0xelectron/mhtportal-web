from rest_framework.serializers import ModelSerializer
from events.models import (Event, EventParticipant)
from base.models import (Participant, Address)
from base.serializers import (ParticipantSerializer,
                                AddressSerializer)


class EventSerializer(ModelSerializer):
    """EventSerializer serializes Event model to json
    object and vice versa.
    """
    venue = AddressSerializer()

    class Meta:
        model = Event
        fields = '__all__'



    def create(self, validated_data):
        address_data = validated_data.pop('venue')

        # Create address and link it with event
        try:
            address = Address.objects.get(**address_data)
        # What should do I here? Probably there are similar Addressess
        except Exception as e:
            address = Address.objects.create(**address_data)
        event = Event.objects.create(venue=address, **validated_data)

        return event



class EventParticipantSerializer(ModelSerializer):
    """EventParticipantSerializer serializes EventPariticpant model
    to json object and vice versa.
    """
    #event = EventSerializer()
    participant = ParticipantSerializer()

    class Meta:
        model = EventParticipant
        fields = '__all__'


    def create(self, validated_data):
        # event_data = validated_data.pop('event')
        participant_data = validated_data.pop('participant')

        # Create participant and link him with event
        try:
            participant = Participant.objects.get(**participant_data)
        # What should do I here? Probably there are similar participants
        except Exception as e:
            participant = Participant.objects.create(**participant_data)

        event_participant = EventParticipant.objects.create(participant=participant, **validated_data)

        return event_participant

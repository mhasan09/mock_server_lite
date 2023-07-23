import json
from django.test import TestCase
from datetime import datetime
from mock_server.models import Response
from utils.helpers import parse_all_responses_data, parse_single_response_data


class ResponseParsingTestCase(TestCase):
    def setUp(self):
        self.response_data = [
            {
                "id": 1,
                "title": "user_data",
                "content": '{"username": "JohnDoe123", "email": "johndoe123@example.com", "age": 28, "is_active": true}',
                "created_at": datetime(2023, 7, 23, 23, 10, 58, 797492),
            },
            {
                "id": 2,
                "title": "football_match_data",
                "content": '{"match_id": "12345", "date": "2023-07-23", "time": "19:00", "venue": "City Stadium", "city": "New York", "home_team": "New York FC", "away_team": "Los Angeles '
                           'United", "home_team_score": 2, "away_team_score": 1, "status": "completed", "referee": "John Smith", "attendance": 35000, "highlights": [{"minute": 15, '
                           '"description": "Goal! New York FC scores the opening goal."}, {"minute": 42, "description": "Yellow card shown to a player from Los Angeles United."}, '
                           '{"minute": 67, "description": "Substitution: John Doe in, Jack Johnson out for New York FC."}, {"minute": 85, "description": "Goal! Los Angeles United '
                           'equalizes."}, {"minute": 90, "description": "Goal! New York FC scores the winning goal in stoppage time."}]}',
                "created_at": datetime(2023, 7, 23, 23, 11, 33, 202621),
            },
        ]

        for response_info in self.response_data:
            Response.objects.create(**response_info)

    def test_parse_all_responses_data(self):
        responses = Response.objects.all()

        parsed_data = parse_all_responses_data(responses)

        for i, response in enumerate(responses):
            expected_result = {
                "id": response.id,
                "title": response.title,
                "content": json.loads(response.content),
                "created_at": response.created_at.strftime("%Y-%m-%d %H:%M:%S.%f"),
            }
            self.assertEqual(parsed_data[i], expected_result)

    def test_parse_single_response_data(self):
        response = Response.objects.first()

        parsed_data = parse_single_response_data(response)

        expected_result = {
            "id": response.id,
            "title": response.title,
            "content": json.loads(response.content),
            "created_at": response.created_at.strftime("%Y-%m-%d %H:%M:%S.%f"),
        }
        self.assertEqual(parsed_data, expected_result)


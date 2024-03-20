import dataclasses
import unittest
import requests_mock

from client.RestClient import RestClient
from client.api.dto import User, UserAttributes, UserBrief
from client.api.exceptions import ErrorResponseCode


class UserTest(unittest.TestCase):

    def test_get_users_empty_succeeds(self):
        with requests_mock.Mocker() as mock:
            # mock
            mock.get('http://gateway-service/api/user', json=[])
            # test
            response = RestClient().get_users()
            self.assertEqual([], response)

    def test_get_user_succeeds(self):
        with requests_mock.Mocker() as mock:
            exp = [
                User(id='8638c043-5145-4be8-a3e4-4b79991b0a16', username='mweise',
                     attributes=UserAttributes(theme='dark'))
            ]
            # mock
            mock.get('http://gateway-service/api/user', json=[dataclasses.asdict(exp[0])])
            # test
            response = RestClient().get_users()
            self.assertEqual(exp, response)

    def test_get_user_fails(self):
        with requests_mock.Mocker() as mock:
            # mock
            mock.get('http://gateway-service/api/user', status_code=404)
            # test
            try:
                response = RestClient().get_users()
            except ErrorResponseCode as e:
                pass

    def test_create_user_succeeds(self):
        with requests_mock.Mocker() as mock:
            exp = UserBrief(id='8638c043-5145-4be8-a3e4-4b79991b0a16', username='mweise')
            # mock
            mock.post('http://gateway-service/api/user', json=dataclasses.asdict(exp), status_code=201)
            # test
            response = RestClient().create_user(username='mweise', password='s3cr3t', email='mweise@example.com')
            self.assertEqual(exp, response)

    def test_create_user_bad_request_fails(self):
        with requests_mock.Mocker() as mock:
            exp = UserBrief(id='8638c043-5145-4be8-a3e4-4b79991b0a16', username='mweise')
            # mock
            mock.post('http://gateway-service/api/user', json=dataclasses.asdict(exp), status_code=400)
            # test
            try:
                response = RestClient().create_user(username='mweise', password='s3cr3t', email='mweise@example.com')
            except ErrorResponseCode as e:
                pass

    def test_create_user_username_exists_fails(self):
        with requests_mock.Mocker() as mock:
            exp = UserBrief(id='8638c043-5145-4be8-a3e4-4b79991b0a16', username='mweise')
            # mock
            mock.post('http://gateway-service/api/user', json=dataclasses.asdict(exp), status_code=409)
            # test
            try:
                response = RestClient().create_user(username='mweise', password='s3cr3t', email='mweise@example.com')
            except ErrorResponseCode as e:
                pass

    def test_create_user_default_role_not_exists_fails(self):
        with requests_mock.Mocker() as mock:
            exp = UserBrief(id='8638c043-5145-4be8-a3e4-4b79991b0a16', username='mweise')
            # mock
            mock.post('http://gateway-service/api/user', json=dataclasses.asdict(exp), status_code=404)
            # test
            try:
                response = RestClient().create_user(username='mweise', password='s3cr3t', email='mweise@example.com')
            except ErrorResponseCode as e:
                pass

    def test_create_user_emails_exists_fails(self):
        with requests_mock.Mocker() as mock:
            exp = UserBrief(id='8638c043-5145-4be8-a3e4-4b79991b0a16', username='mweise')
            # mock
            mock.post('http://gateway-service/api/user', json=dataclasses.asdict(exp), status_code=417)
            # test
            try:
                response = RestClient().create_user(username='mweise', password='s3cr3t', email='mweise@example.com')
            except ErrorResponseCode as e:
                pass

    def test_get_user_succeeds(self):
        with requests_mock.Mocker() as mock:
            exp = User(id='8638c043-5145-4be8-a3e4-4b79991b0a16', username='mweise',
                       attributes=UserAttributes(theme='dark'))
            # mock
            mock.get('http://gateway-service/api/user/8638c043-5145-4be8-a3e4-4b79991b0a16',
                     json=dataclasses.asdict(exp))
            # test
            response = RestClient().get_user(user_id='8638c043-5145-4be8-a3e4-4b79991b0a16')
            self.assertEqual(exp, response)

    def test_get_user_not_found_fails(self):
        with requests_mock.Mocker() as mock:
            # mock
            mock.get('http://gateway-service/api/user/8638c043-5145-4be8-a3e4-4b79991b0a16', status_code=404)
            # test
            try:
                response = RestClient().get_user(user_id='8638c043-5145-4be8-a3e4-4b79991b0a16')
            except ErrorResponseCode as e:
                pass

    def test_update_user_succeeds(self):
        with requests_mock.Mocker() as mock:
            exp = User(id='8638c043-5145-4be8-a3e4-4b79991b0a16', username='mweise', given_name='Martin',
                       attributes=UserAttributes(theme='dark'))
            # mock
            mock.put('http://gateway-service/api/user/8638c043-5145-4be8-a3e4-4b79991b0a16', status_code=202,
                     json=dataclasses.asdict(exp))
            # test
            response = RestClient().update_user(user_id='8638c043-5145-4be8-a3e4-4b79991b0a16', firstname='Martin')
            self.assertEqual(exp, response)

    def test_update_user_not_found_fails(self):
        with requests_mock.Mocker() as mock:
            # mock
            mock.put('http://gateway-service/api/user/8638c043-5145-4be8-a3e4-4b79991b0a16', status_code=404)
            # test
            try:
                response = RestClient().update_user(user_id='8638c043-5145-4be8-a3e4-4b79991b0a16', firstname='Martin')
            except ErrorResponseCode as e:
                pass

    def test_update_user_foreign_fails(self):
        with requests_mock.Mocker() as mock:
            # mock
            mock.put('http://gateway-service/api/user/8638c043-5145-4be8-a3e4-4b79991b0a16', status_code=405)
            # test
            try:
                response = RestClient().update_user(user_id='8638c043-5145-4be8-a3e4-4b79991b0a16', firstname='Martin')
            except ErrorResponseCode as e:
                pass

    def test_update_user_theme_succeeds(self):
        with requests_mock.Mocker() as mock:
            exp = User(id='8638c043-5145-4be8-a3e4-4b79991b0a16', username='mweise', given_name='Martin',
                       attributes=UserAttributes(theme='dark'))
            # mock
            mock.put('http://gateway-service/api/user/8638c043-5145-4be8-a3e4-4b79991b0a16/theme', status_code=202,
                     json=dataclasses.asdict(exp))
            # test
            response = RestClient().update_user_theme(user_id='8638c043-5145-4be8-a3e4-4b79991b0a16', theme='dark')
            self.assertEqual(exp, response)

    def test_update_user_theme_not_found_fails(self):
        with requests_mock.Mocker() as mock:
            # mock
            mock.put('http://gateway-service/api/user/8638c043-5145-4be8-a3e4-4b79991b0a16/theme', status_code=404)
            # test
            try:
                response = RestClient().update_user_theme(user_id='8638c043-5145-4be8-a3e4-4b79991b0a16', theme='dark')
            except ErrorResponseCode as e:
                pass

    def test_update_user_theme_foreign_fails(self):
        with requests_mock.Mocker() as mock:
            # mock
            mock.put('http://gateway-service/api/user/8638c043-5145-4be8-a3e4-4b79991b0a16/theme', status_code=405)
            # test
            try:
                response = RestClient().update_user_theme(user_id='8638c043-5145-4be8-a3e4-4b79991b0a16', theme='dark')
            except ErrorResponseCode as e:
                pass

    def test_update_user_password_succeeds(self):
        with requests_mock.Mocker() as mock:
            exp = User(id='8638c043-5145-4be8-a3e4-4b79991b0a16', username='mweise', given_name='Martin',
                       attributes=UserAttributes(theme='dark'))
            # mock
            mock.put('http://gateway-service/api/user/8638c043-5145-4be8-a3e4-4b79991b0a16/password', status_code=202,
                     json=dataclasses.asdict(exp))
            # test
            response = RestClient().update_user_password(user_id='8638c043-5145-4be8-a3e4-4b79991b0a16',
                                                         password='s3cr3t1n0rm4t10n')
            self.assertEqual(exp, response)

    def test_update_user_password_not_found_fails(self):
        with requests_mock.Mocker() as mock:
            # mock
            mock.put('http://gateway-service/api/user/8638c043-5145-4be8-a3e4-4b79991b0a16/password', status_code=404)
            # test
            try:
                response = RestClient().update_user_password(user_id='8638c043-5145-4be8-a3e4-4b79991b0a16',
                                                             password='s3cr3t1n0rm4t10n')
            except ErrorResponseCode as e:
                pass

    def test_update_user_password_foreign_fails(self):
        with requests_mock.Mocker() as mock:
            # mock
            mock.put('http://gateway-service/api/user/8638c043-5145-4be8-a3e4-4b79991b0a16/password', status_code=405)
            # test
            try:
                response = RestClient().update_user_password(user_id='8638c043-5145-4be8-a3e4-4b79991b0a16',
                                                             password='s3cr3t1n0rm4t10n')
            except ErrorResponseCode as e:
                pass

    def test_update_user_password_keycloak_fails(self):
        with requests_mock.Mocker() as mock:
            # mock
            mock.put('http://gateway-service/api/user/8638c043-5145-4be8-a3e4-4b79991b0a16/password', status_code=503)
            # test
            try:
                response = RestClient().update_user_password(user_id='8638c043-5145-4be8-a3e4-4b79991b0a16',
                                                             password='s3cr3t1n0rm4t10n')
            except ErrorResponseCode as e:
                pass


if __name__ == "__main__":
    unittest.main()

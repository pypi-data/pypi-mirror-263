import unittest
import requests_mock
import dataclasses

from client.RestClient import RestClient

from client.api.dto import Database, User, Container, Image, UserAttributes
from client.api.exceptions import ErrorResponseCode


class DatabaseTest(unittest.TestCase):

    def test_get_databases_empty(self):
        with requests_mock.Mocker() as mock:
            # mock
            mock.get('/api/database', json=[])
            # test
            response = RestClient().get_databases()
            self.assertEqual([], response)

    def test_get_databases_succeeds(self):
        exp = [
            Database(
                id=1,
                name='test',
                creator=User(id='8638c043-5145-4be8-a3e4-4b79991b0a16', username='mweise',
                             attributes=UserAttributes(theme='light')),
                owner=User(id='8638c043-5145-4be8-a3e4-4b79991b0a16', username='mweise',
                           attributes=UserAttributes(theme='light')),
                contact=User(id='8638c043-5145-4be8-a3e4-4b79991b0a16', username='mweise',
                             attributes=UserAttributes(theme='light')),
                created='2024-01-01 00:00:00',
                exchange_name='dbrepo',
                internal_name='test_abcd',
                is_public=True,
                container=Container(
                    id=1,
                    name='MariaDB Galera 11.1.3',
                    internal_name='mariadb',
                    host='data-db',
                    port=3306,
                    sidecar_host='data-db-sidecar',
                    sidecar_port=3305,
                    created='2024-01-01 00:00:00',
                    image=Image(
                        id=1,
                        registry='docker.io',
                        name='mariadb',
                        version='11.2.2',
                        dialect='org.hibernate.dialect.MariaDBDialect',
                        driver_class='org.mariadb.jdbc.Driver',
                        jdbc_method='mariadb',
                        default_port=3306
                    )
                )
            )
        ]
        with requests_mock.Mocker() as mock:
            # mock
            mock.get('/api/database', json=[dataclasses.asdict(exp[0])])
            # test
            response = RestClient().get_databases()
            self.assertEqual(exp, response)

    def test_get_database_succeeds(self):
        exp = Database(
            id=1,
            name='test',
            creator=User(id='8638c043-5145-4be8-a3e4-4b79991b0a16', username='mweise',
                         attributes=UserAttributes(theme='light')),
            owner=User(id='8638c043-5145-4be8-a3e4-4b79991b0a16', username='mweise',
                       attributes=UserAttributes(theme='light')),
            contact=User(id='8638c043-5145-4be8-a3e4-4b79991b0a16', username='mweise',
                         attributes=UserAttributes(theme='light')),
            created='2024-01-01 00:00:00',
            exchange_name='dbrepo',
            internal_name='test_abcd',
            is_public=True,
            container=Container(
                id=1,
                name='MariaDB Galera 11.1.3',
                internal_name='mariadb',
                host='data-db',
                port=3306,
                sidecar_host='data-db-sidecar',
                sidecar_port=3305,
                created='2024-01-01 00:00:00',
                image=Image(
                    id=1,
                    registry='docker.io',
                    name='mariadb',
                    version='11.2.2',
                    dialect='org.hibernate.dialect.MariaDBDialect',
                    driver_class='org.mariadb.jdbc.Driver',
                    jdbc_method='mariadb',
                    default_port=3306
                )
            )
        )
        with requests_mock.Mocker() as mock:
            # mock
            mock.get('/api/database/1', json=dataclasses.asdict(exp))
            # test
            response = RestClient().get_database(1)
            self.assertEqual(exp, response)

    def test_get_database_not_found_fails(self):
        with requests_mock.Mocker() as mock:
            # mock
            mock.get('/api/database/1', status_code=404)
            # test
            try:
                response = RestClient().get_database(1)
            except ErrorResponseCode as e:
                pass

    def test_get_database_invalid_dto_fails(self):
        try:
            exp = Database()
        except TypeError as e:
            pass

    def test_get_database_unauthorized_fails(self):
        with requests_mock.Mocker() as mock:
            # mock
            mock.get('/api/database/1', status_code=401)
            # test
            try:
                response = RestClient().get_database(1)
            except ErrorResponseCode as e:
                pass

    def test_create_database_unauthorized_fails(self):
        with requests_mock.Mocker() as mock:
            # mock
            mock.post('/api/database', status_code=401)
            # test
            try:
                response = RestClient().create_database(name='test', container_id=1, is_public=True)
            except ErrorResponseCode as e:
                pass

    def test_create_database_succeeds(self):
        exp = Database(
            id=1,
            name='test',
            creator=User(id='8638c043-5145-4be8-a3e4-4b79991b0a16', username='mweise',
                         attributes=UserAttributes(theme='light')),
            owner=User(id='8638c043-5145-4be8-a3e4-4b79991b0a16', username='mweise',
                       attributes=UserAttributes(theme='light')),
            contact=User(id='8638c043-5145-4be8-a3e4-4b79991b0a16', username='mweise',
                         attributes=UserAttributes(theme='light')),
            created='2024-01-01 00:00:00',
            exchange_name='dbrepo',
            internal_name='test_abcd',
            is_public=True,
            container=Container(
                id=1,
                name='MariaDB Galera 11.1.3',
                internal_name='mariadb',
                host='data-db',
                port=3306,
                sidecar_host='data-db-sidecar',
                sidecar_port=3305,
                created='2024-01-01 00:00:00',
                image=Image(
                    id=1,
                    registry='docker.io',
                    name='mariadb',
                    version='11.2.2',
                    dialect='org.hibernate.dialect.MariaDBDialect',
                    driver_class='org.mariadb.jdbc.Driver',
                    jdbc_method='mariadb',
                    default_port=3306
                )
            )
        )
        with requests_mock.Mocker() as mock:
            # mock
            mock.post('/api/database', json=dataclasses.asdict(exp), status_code=201)
            # test
            response = RestClient().create_database(name='test', container_id=1, is_public=True)
            self.assertEqual(response.name, 'test')


if __name__ == "__main__":
    unittest.main()

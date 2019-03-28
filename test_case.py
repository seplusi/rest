import unittest
import json
import requests


class TestPostitWebApplication(unittest.TestCase):

#    @unittest.skip('')
    def test_get_all_albums(self):
        """
            Tests retrieving all albums
        """
        json_load = self._perform_get_and_validate('albums')
        for album in json_load:
            assert sorted(list(album.keys())) == ['id', 'title']
            assert type(album['id']) == int
            assert isinstance(album['title'], str)
        assert (len(json_load) == 30)

#    @unittest.skip('')
    def test_get_individual_album(self):
        """
            Tests retrieving a single album
        """
        json_load = self._perform_get_and_validate('albums/1')
        assert sorted(list(json_load.keys())) == ['id', 'title']
        assert type(json_load['id']) == int
        assert isinstance(json_load['title'], str)
        assert type(json_load) == dict

#    @unittest.skip('')
    def test_get_all_users(self):
        """
             Tests retrieving all users
        """
        json_load = self._perform_get_and_validate('users')
        for user in json_load:
            assert sorted(list(user.keys())) == ['id', 'name']
            assert type(user['id']) == int
            assert isinstance(user['name'], str)
        assert (len(json_load) == 10)

#    @unittest.skip('')
    def test_get_individual_user(self):
        """
            Tests retrieving a single album
        """
        json_load = self._perform_get_and_validate('users/1')
        assert sorted(list(json_load.keys())) == ['id', 'name']
        assert type(json_load['id']) == int
        assert isinstance(json_load['name'], str)
        assert type(json_load) == dict

#    @unittest.skip('')
    def test_non_existant_resource(self):
        """
            Tests retrieving a single album
        """
        json_load = self._perform_get_and_validate('albix', status_code=404, ok=False)
        assert json_load == {}
    
    def _perform_get_and_validate(self, resource, status_code=200, ok=True,
                                  endpoint='https://my-json-server.typicode.com/seplusi/rest'):
        """
            Method that performs the get and validates basic and common data
            
        :param resource: String with the resource to be retrieved from rest API
        :param status_code: Integer with the return code from rest API
        :param ok: Boolean
        :param endpoint: String with the endpoint. For future REST API implementations
        :return: The retrieved data from the API in json formar
        """
        var = requests.get(url='%s/%s' % (endpoint, resource))
        assert var.status_code == status_code
        assert var.ok if ok else not (var.ok)
        
        return json.loads(var.text)

if __name__ == '__main__':
    unittest.main(verbosity=3)

import unittest
import json
import requests


class TestPostitWebApplication(unittest.TestCase):

#    @unittest.skip('')
    def test_get_all_albums(self):
        """
            Tests retrieving all albums
        """
        var = requests.get('https://my-json-server.typicode.com/seplusi/rest/albums')
        json_load = json.loads(var.text)
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
        response = requests.get('https://my-json-server.typicode.com/seplusi/rest/albums/1')
        json_load = json.loads(response.text)
        assert sorted(list(json_load.keys())) == ['id', 'title']
        assert type(json_load['id']) == int
        assert isinstance(json_load['title'], str)
        assert type(json_load) == dict

#    @unittest.skip('')
    def test_get_all_users(self):
        """
             Tests retrieving all users
        """
        response = requests.get('https://my-json-server.typicode.com/seplusi/rest/users')
        json_load = json.loads(response.text)
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
        response = requests.get('https://my-json-server.typicode.com/seplusi/rest/users/1')
        json_load = json.loads(response.text)
        assert sorted(list(json_load.keys())) == ['id', 'name']
        assert type(json_load['id']) == int
        assert isinstance(json_load['name'], str)
        assert type(json_load) == dict
    

if __name__ == '__main__':
    unittest.main(verbosity=3)
import requests
import os
from pprint import pp, pprint

url_hero = 'https://superheroapi.com/api/2619421814940190'


def full_info(name):
    url_search = url_hero + '/search/' + name
    resp_hero = requests.get(url_search)
    return resp_hero.json()


def search_id(name):
    url_search = url_hero + '/search/' + name
    resp_hero = requests.get(url_search)
    id = resp_hero.json()['results'][0]['id']
    return id


def max_intelligence():
    resp_Thanos = requests.get(url_hero + '/' + search_id('Thanos'))
    resp_Hulk = requests.get(url_hero + '/' + search_id('Hulk'))
    resp_CA = requests.get(url_hero + '/' + search_id('Captain America'))
    int_dict = {'Thanos': int(resp_Thanos.json()['powerstats']['intelligence']),
                'Hulk': int(resp_Hulk.json()['powerstats']['intelligence']),
                'Captain America': int(resp_CA.json()['powerstats']['intelligence'])}
    max_int = max(int_dict, key=int_dict.get)
    return max_int


# print(max_intelligence())

# -------------------------задание 2------------------------------------------
class YaUploader:

    def __init__(self, token: str):
        self.token = token

    def upload(self, file_list, path_to_files):
        count = 0
        for file_path in file_list:
            url = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload/'
            headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}
            params = {'path': file_path, 'overwrite': True}
            up_link = requests.get(url, params=params, headers=headers)
            response = requests.put(up_link.json()['href'],
                                    data=open(os.path.join(path_to_files, file_path), 'rb'),
                                    headers=headers)
            response.raise_for_status()
            if response.status_code == 201:
                count += 1
                print(f'File {count} of {len(file_list)} uploaded')


# if __name__ == '__main__':
#     path_to_file = os.path.join(os.getcwd(), 'upload')
#     upload_list = ['picture.jpg', 'lecture.pdf', 'sound.mp3']
#     token = '...'
#     uploader = YaUploader(token)
#     result = uploader.upload(upload_list, path_to_file)



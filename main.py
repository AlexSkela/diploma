import time
import os

import requests

from pprint import pprint

TOKEN_VK = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'
TOKEN_YA = " "

class VK_photo:

    def __init__(self, id, token_vk, token_YA):

        self.id = id
        self.token_vk = token_vk
        self.token_YA = token_YA


    def _save_photo(self):

        url = 'https://api.vk.com/method/photos.get'
        params = {
            'owner_id' : self.id,
            'album_id' : 'profile',
            'extended' : '1',
            'photo_sizes' : '0',
            'access_token': self.token_vk,
            'v' : '5.126'
        }
        res = requests.get(url, params=params)
        res1 = res.json()

        return res1

    def photo_list(self):

        items = self._save_photo()['response']['items']
        photo_info = []
        info = {}
        likes_count = []
        repeat_likes_count = []

        for like in items:
            likes_count.append(like['likes']['count'])

        for like in likes_count:
            if likes_count.count(like) > 1:
                repeat_likes_count.append(like)

        for item in items:
            like = item['likes']['count']
            date_photo = 'today'
            info = {
                'size': item['sizes'][-1]['type'],
                'link': item['sizes'][-1]['url']
            }

        if like in repeat_likes_count:
            info['file_name'] = f'{like}_{date_photo}.jpg'
            photo_info.append(info)

        else:
            info['file_name'] = f'{like}.jpg'
            photo_info.append(info)

        return photo_info

        # pprint(res1)
        pprint(photo_info)

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token_YA)
        }

    def yadisk_photo(self, folder):
        folder_create = f'https://cloud-api.yandex.net/v1/disk/resources?path={folder}'
        headers = self.get_headers()
        # params = {'href': folder_create, 'templated': 'true'}
        response = requests.get(folder_create, headers=headers)
        pprint(response.json())
        return response.json()


    # def uploud_to_disk(self, folder):
    #     href = self._yadisk_photo(folder=).get('href', )
    #     response = requests.put(href, self.photo_list()[0]['link'])
    #     response.raise_for_status()
    #     if response.status_code == 201:
    #         print('Файлы успешно загружены')

if __name__ == '__main__':
    new_id = VK_photo('552934290', token_vk=TOKEN_VK, token_YA=TOKEN_YA)
    # pprint(new_id.save_photo())
    new_id.photo_list()
    new_id.yadisk_photo(folder='diploma_1')
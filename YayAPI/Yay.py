from urllib.parse import quote
import requests


class Yay:
    def __init__(self) -> None:
        self.HOST = 'api.yay.space'

    def Timeline(self) -> dict:
        """
        Yayのタイムラインを取得します。
        :rtype: dict
        """
        response = requests.get(f'https://{self.HOST}/v1/web/posts/public_timeline?number=100')
        if response:
            return {'success': True,
                    'data': response.json()['posts']}
        else:
            return {'success': False}

    def UserSearch(self, nickname: str = None, biography: str = None, vip: bool = None,
                   recently_created: bool = None, not_recent_gomimushi: bool = None) -> dict:
        """
        ユーザーを検索します。
        :param nickname: ニックネーム
        :type nickname: str
        :param biography: 自己紹介
        :type biography: str
        :param vip: VIPユーザーのみを出力します。
        :type vip: bool
        :param recently_created: 最近アカウントを作成したユーザーを除外します。
        :type recently_created: bool
        :param not_recent_gomimushi: 最近ゴミ虫になったユーザーを除外します。
        :type not_recent_gomimushi: bool
        :rtype: dict
        """
        params = {
            'nickname': nickname,
            'biography': biography,
            'not_recent_gomimushi': not_recent_gomimushi,
            'recently_created': recently_created,
            'vip': vip,
            'number': '100',
        }

        response = requests.get(f'https://{self.HOST}/v1/web/users/search', params=params)
        if response:
            return {'success': True,
                    'data': response.json()['users']}
        else:
            raise {'success': False}

    def TagSearch(self, tag: str) -> dict:
        """
        ハッシュタグを検索します。
        :param tag: ハッシュタグ
        :type tag: str
        :rtype: dict
        """
        response = requests.post(f'https://{self.HOST}/v1/posts/recommended_tag', json={
            'tag': tag,
        })
        if response:
            return {'success': True,
                    'data': response.json()['tags']}
        else:
            raise {'success': False}

    def KeywordSearch(self, keyword: str) -> dict:
        """
        指定のハッシュタグが含まれている投稿を検索します。
        :param keyword: ハッシュタグを検索します。
        :type keyword: str
        :rtype: dict
        """
        response = requests.get(
            f'https://{self.HOST}/v2/posts/tags/{quote(keyword)}?number=100',
        )
        if response:
            return {'success': True,
                    'data': response.json()['posts']}
        else:
            return {'success': False}

    def PostData(self, post_id: str) -> dict:
        """
        投稿データを取得します。
        :param post_id: 投稿id
        :type post_id: str
        :rtype: dict
        """
        response = requests.get(f'https://{self.HOST}/v2/posts/{post_id}')
        if response:
            return {'success': True,
                    'data': response.json()}
        else:
            return {'success': False}

    def UserData(self, user_id: str) -> dict:
        """
        ユーザーデータを取得します。
        :param user_id: ユーザーid
        :type user_id: str
        :rtype: dict
        """
        response = requests.get(f'https://{self.HOST}/v2/users/{user_id}')
        if response:
            return {'success': True,
                    'data': response.json()}
        else:
            return {'success': False}

    def UserActiveCall(self, user_id: str) -> dict:
        """
        ユーザーが通話をしているか確認します。
        :param user_id: ユーザーid
        :type user_id: str
        :rtype: dict
        """
        response = requests.get(f'https://{self.HOST}/v1/posts/active_call?user_id={user_id}')
        if response:
            return {'success': True,
                    'data': response.json()}
        else:
            return {'success': False}

    def UserTimeline(self, user_id: str) -> dict:
        """
        ユーザー投稿データを取得します。
        :param user_id: ユーザーid
        :type user_id:str
        :rtype: dict
        """
        response = requests.get(f'https://{self.HOST}/v2/posts/user_timeline?number=100&user_id={user_id}')
        if response:
            return {'success': True,
                    'data': response.json()}
        else:
            return {'success': False}

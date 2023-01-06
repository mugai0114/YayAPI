# YayAPI

yay.spaceの非公開APIです。

# 特徴

* タイムラインの取得
* ユーザーの詳細データの取得
* ハッシュタグ等の検索

# インストール
```
pip install YayAPI
```

# 使用方法

```python
from YayAPI import Yay

api = Yay()

api.Timeline()  # タイムラインの取得
api.UserSearch(nickname='Konn', biography='hello@konn.ink')  # ユーザーの検索
api.TagSearch(tag='YouName')  # ハッシュタグの検索
```
# 支援
[![Build](https://www.buymeacoffee.com/assets/img/custom_images/yellow_img.png)](https://www.buymeacoffee.com/Konn)

[PayPal](https://paypal.me/konnkoko)
# 注意

これは、非公式のAPIです、一切責任を負いません。 自己責任でご使用下さい。
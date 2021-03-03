# detect-qrcode
画像からQRコード検出スクリプト

## install
```sh
# mac（色々バージョン調節必要だった）
brew install zbar
```

## setup
```sh
make setup-mac

# start
source venv/bin/activate

# stop
deactivate
```

## execute
```sh
python main.py 'images/xxxx.jpg'
```
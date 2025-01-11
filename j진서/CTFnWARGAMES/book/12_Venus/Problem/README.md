# PPCTower

- Security Camp 2016 CTF Problem [Venus]

## 問題ファイルの実行環境

- Python 3
- python-qrcode

「Ubuntu 16.04.2 LTS」を用いて問題を解くことを想定しているため、Pythonのバージョンは「3.5.2」を使用します。  
また、python-qrcodeを使用してQRコードを生成するため、以下のコマンドを実行してインストールしてください。

```
sudo apt install python-qrcode
```

## 問題ファイルの実行

以下のコマンドを実行すると、`localhost:24154`で問題ファイルが実行されます。

```
python PPCTower.py
```

ホストやポートを変更したい場合には以下のコマンドを実行します。  
(例 : `0.0.0.0:24154`で問題ファイルを実行する場合)

```
python PPCTower.py 0.0.0.0 24154
```

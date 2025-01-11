# PPCTower solver

- Security Camp 2016 CTF Problem [Venus] solver

## ソルバーの実行環境

- Python 2
- qrtools

「Ubuntu 16.04.2 LTS」を用いて問題を解くことを想定しているため、Pythonのバージョンは「2.7.12」を使用します。  
また、qrtoolsを使用してQRコードの読み取りを行うため、以下のコマンドを実行してインストールしてください。

```
sudo python -m pip install qrtools
sudo apt install python-zbar
sudo python -m pip install pillow
```

## ソルバーの実行

以下のコマンドを実行すると、`localhost:24154`で実行されている問題を解き始めます。

```
$ python solver.py
```
ホストやポートを変更したい場合には以下の部分を変更してください。

```
client.connect(('127.0.0.1', 24154))
```

## 注意事項

環境によっては動作しない可能性があります。あくまでも参考程度にご確認ください。
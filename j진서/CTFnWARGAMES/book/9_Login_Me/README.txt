---Login Me 問題サーバの構築手順---

1, Dockerをインストールします（Windowsの場合、Virtual Box等を使ってLinux上で作業することをお勧めします）
   この手順に関しては、読者の皆様ご自身で調べていただければ幸いです。

2, ./dockerディレクトリをカレントとして、root権限を持つアカウントで以下のコマンドを実行し、Docker imageを構築します。これには少し時間がかかる場合があります
---
cd ./docker
docker build -t ctf_loginme ./ 
---

3, 手順2が完了したら、root権限を持つアカウントで以下のコマンドを実行します。
---
docker run -it -p 8080:80 ctf_loginme
---

4, 手順3のコマンドを実行したサーバの8080番ポートにアクセスすれば、問題にアクセスできます。。本文中のIP,Port番号等は適宜自分のものに置き換えてください。
   なお、8080番ポートを既に使用している場合は、コマンドの8080の箇所を適宜空いているポート番号に変更してください。

5,  終了させたい時はCtrl-Cで抜けてください。終了するまでに少し時間がかかる場合があります。

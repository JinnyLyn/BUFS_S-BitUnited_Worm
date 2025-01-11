# サイバーコロッセオ×SECCON 2017 弐

## 実行に必要なソフトウェア
* VirtualBox (5.1.24での動作を確認)


## 事前準備

1. BIOS/UEFIでVT-xの有効化
2. VirtualBoxのインストール
3. VirtualBoxに問題サーバのディスクイメージをインポート
4. VirtualBoxでのNICの設定  
VirtualBoxで該当仮想マシンを右クリック->Setting->Network の順に開く  
VirtualBoxのホストマシンからアクセスする場合 : Host-Only AdapterやBridged Adapterを選択  
別のホストから問題サーバにアクセスする場合：Bridged Adapterを選択    
なお, これらについては適宜変更してください  
5. 問題サーバを起動
6. user:root, password:root で問題サーバにログイン
7. `ip` コマンドや`ifconfig`コマンドで問題サーバのIPアドレスを調べる

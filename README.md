# AWSのMLサービスを使ってみよう

## Cloud9でSDKを実行するための準備
### 1. IAMユーザーの作成とIAMポリシーのアタッチ

- **ルートユーザーは使わないこと！**
- 利用したいサービスごとに最小限のIAMポリシーを用意しましょう

### 2. Cloud9環境の作成

- スペックはデフォルトでOKです

### 3. すぐに動かすための手順

```
# pip の upgrade
$ sudo pip3 install --upgrade pip
$ hash -r

# pip の バージョン確認
$ pip -V
pip 21.0.1 from /usr/local/lib/python3.7/site-packages/pip (python 3.7)
```

```
# リポジトリのクローン
$ git clone https://github.com/mohira-books/aws-ml-services-with-cloud9.git
$ cd aws-ml-services-with-cloud9

# 必要なモジュールのinstall 
$ pip install -r requirements.txt 
```

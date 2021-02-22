# AWSのMLサービスを使ってみよう
AWSのMLサービスを体験するためのリポジトリです。

素早く体験するために、AWS Cloud9 環境 での実行を想定しています(Credentialsの設定をする必要がないため)。

しかし、[AWS SDK for Python | AWS](https://aws.amazon.com/jp/sdk-for-python/)の設定を行えば別の環境でも実行可能です。

## Cloud9でSDKを実行するための準備
### 1. IAMユーザーの作成とIAMポリシーのアタッチ

- **ルートユーザーは使わないこと！**
- 利用したいサービスごとに最小限のIAMポリシーを用意しましょう

### 2. AWS SDK 利用のための設定

- Cloud9環境の場合は特に設定しなくてもOKです
-
別の環境で実行する場合は、[Quickstart — Boto3 Docs](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration)
を参考に設定をしてください

### 3. Cloud9環境の作成

- スペックはデフォルトでOKです

### 4. すぐに動かすための手順

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

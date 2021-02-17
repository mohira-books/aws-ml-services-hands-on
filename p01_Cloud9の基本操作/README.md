## 環境の作り方

## AWS Cloud9とはなにか？

- ブラウザだけで開発(≒プログラミング)できる環境を提供してくれるサービス
- いわゆる、ブラウザベースのIDE(Integrated Development Environment; 統合開発環境)
  - :memo: PyCharmもIDEの1つ
- 公式: [AWS Cloud9](https://aws.amazon.com/jp/cloud9/)

### Cloud9のつかいどころ

- 実験段階での開発には相当に便利！
    - 環境を用意するのがカンタン
    - 環境を捨てるのもカンタン ← 重要！
    - AWSの他のサービスとの連携がカンタン
- 実開発に使えるかというと、まだまだという感じ。しかし、発展しつつあるので今後に期待。

## 基本操作
Pythonファイルの作成と編集、およびPythonプログラムの実行方法を確認します。

### 例題: Cloud9環境の作成方法
次の資料を参考にしてください。

https://docs.google.com/presentation/d/1Mu91u_0ncpc5qSdFlcAymGgjZtAOYv7XTSPVuDBobwk/

### 例題: Pythonプログラムの作成と実行

- 新規ファイル作成: File > New File > `hello.py` と入力する
- 編集: 下記の内容を入力する
- ファイルの保存: File > Save
    - :memo: ショートカットキーを覚えると効率的
- 画面上部の「▶ Run」をクリックする

```python
print('Hello Cloud9')
```

### 演習: Pythonプログラムの作成と実行

- 新規ファイル `goodbye.py` を作成にしてください
- `goodbye.py` を下記の内容にして保存してください
- `goodbye.py` を実行し、画面に `Goodbye Cloud9` を表示されることを確認してください

```python
print('Goodbye Cloud9')
```

## ファイルアップロードとファイルダウンロード
ローカルにある画像ファイルや音声ファイルなどをCloud9環境で操作したいことはよくあります。

Cloud9では簡単にアップロードとダウンロードができます。

### 例題: ローカルマシンからのファイルアップロード

- File > Upload Local Files...
    - :memo: ドラッグアンドドロップ でも実行可能

### 例題: ローカルマシンからへファイルダウンロード

- プロジェクトまるごとダウンロード: File > Download Project
- 特定ファイルのダウンロード: 右クリック > Download

## 設定の編集
### 例題: フォントサイズの調整
左上のCloudのマーク > Preference > User Settings > Code Editor > Font size



# Cloud9サンプルコード

## `boto3` のインストール
Cloud9のターミナルで下記のコマンドを実行してください。

```
sudo pip3 install boto3
```

## 使い方

- `get_text_detection.py` を編集し、バケット名とファイル名を記入します
- `get_text_detection.py` を実行し、ジョブを作成します
    - ジョブIDは、`text_detection_log.txt` に追記されていきます
- しばらく待ちます
- `start_text_detection.py` にジョブIDを記入して、実行します。
    - ジョブIDは、`text_detection_log.txt` を見て確認してください
    - 結果が、画面に出力されます
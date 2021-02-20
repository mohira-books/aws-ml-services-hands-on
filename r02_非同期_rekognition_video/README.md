# Rekognition ビデオのテキスト検出

## 参考

- [保存済みビデオ内のテキストの検出 - Amazon Rekognition](https://docs.aws.amazon.com/ja_jp/rekognition/latest/dg/text-detecting-video-procedure.html)

## 使い方

- `start_text_detection.py` を編集し、バケット名とファイル名を記入します
- `start_text_detection.py` を実行し、ジョブを作成します
    - ジョブIDは、`text_detection_log.txt` に追記されていきます
- しばらく待ちます
- `get_text_detection.py` にジョブIDを記入して、実行します。
    - ジョブIDは、`text_detection_log.txt` を見て確認してください
    - 結果が、画面に出力されます
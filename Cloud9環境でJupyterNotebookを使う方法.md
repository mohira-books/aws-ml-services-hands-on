# Cloud9環境でJupyterNotebookを使う方法
## 目標
Jupyter Notebook を Cloud9環境で実行し、ブラウザでJupyter使えるようにする。

## 必要なライブラリをインストール

```
$ sudo pip3 install --upgrade pip
$ pip install jupyter
$ pip install numpy pandas matplotlib seaborn tqdm # 必要なデータ分析系ライブラリを追加
```

## JupyterNotebookの起動

- トークン(`d569b8208dc1db2cc719ca5e0159ae3c907b12cc1e132c15`)は後で使う

```
$ jupyter notebook --ip 0.0.0.0 --port 8080 --no-browser
[I 04:57:19.687 NotebookApp] Writing notebook server cookie secret to /home/ec2-user/.local/share/jupyter/runtime/notebook_cookie_secret
[I 04:57:20.603 NotebookApp] Serving notebooks from local directory: /home/ec2-user/environment
[I 04:57:20.603 NotebookApp] Jupyter Notebook 6.2.0 is running at:
[I 04:57:20.603 NotebookApp] http://ip-172-31-20-142.ap-northeast-1.compute.internal:8080/?token=d569b8208dc1db2cc719ca5e0159ae3c907b12cc1e132c15
[I 04:57:20.604 NotebookApp]  or http://127.0.0.1:8080/?token=d569b8208dc1db2cc719ca5e0159ae3c907b12cc1e132c15
[I 04:57:20.604 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 04:57:20.608 NotebookApp] 
   
    To access the notebook, open this file in a browser:
        file:///home/ec2-user/.local/share/jupyter/runtime/nbserver-6732-open.html
    Or copy and paste one of these URLs:
        http://ip-172-31-20-142.ap-northeast-1.compute.internal:8080/?token=d569b8208dc1db2cc719ca5e0159ae3c907b12cc1e132c15
     or http://127.0.0.1:8080/?token=d569b8208dc1db2cc719ca5e0159ae3c907b12cc1e132c15 ← この token が重要！
     
```

## Previewして使うまで
### 「Preview」をクリックする > 「Preview Running Application」
<img width="720" alt="image.png (438.7 kB)" src="https://img.esa.io/uploads/production/attachments/6586/2021/02/25/21054/ca666720-20fe-4877-b1de-0a28f1061bc0.png">

### 右下にブラウザがでてくる
<img width="720" alt="image.png (382.4 kB)" src="https://img.esa.io/uploads/production/attachments/6586/2021/02/25/21054/943fd751-db11-4fa2-8629-bc09f7d487c0.png">

### 右下のブラウザのURLをコピーする

- 一見URLは表示されていないが、URLバーをクリックすると表示される
-
ex: `https://e3c4139e6baa4bc998d8fd11d257ef6e.vfs.cloud9.ap-northeast-1.amazonaws.com/`

<img width="720" alt="image.png (409.9 kB)" src="https://img.esa.io/uploads/production/attachments/6586/2021/02/25/21054/0d354397-86e1-40f0-8347-155cf0615493.png">

### コピーしたURLを別タブに貼り付ける
<img width="720" alt="image.png (274.5 kB)" src="https://img.esa.io/uploads/production/attachments/6586/2021/02/25/21054/a5608d3f-508d-4ff6-8ef9-ab64b1852941.png">

### Password or token に トークンを貼り付ける > Log in
<img width="720" alt="image.png (274.8 kB)" src="https://img.esa.io/uploads/production/attachments/6586/2021/02/25/21054/b0e22fb9-52e3-4064-8167-2ad8933091e0.png">

### これでOK！
<img width="720" alt="image.png (147.9 kB)" src="https://img.esa.io/uploads/production/attachments/6586/2021/02/25/21054/9519529c-ef99-4bd4-9091-350cba175b74.png">




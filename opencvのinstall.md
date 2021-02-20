# Cloud9環境でOpenCVを使う方法

## 参考
- 【Cloud9】”pip install –upgrade pip” すると pip が使えなくなった時の対処方法｜ぬるぽ開発
- [add libgl to Anaconda docker images · Issue #49 · ContinuumIO/docker-images](https://github.com/ContinuumIO/docker-images/issues/49)

## 目標
-  このPythonファイルの実行を目指す == boto3 と OpenCV のインストールが目標

```python
# check.py
import boto3
print(boto3)

import cv2
print(cv2)
```

## 手順

```sh
# pipのバージョンをあげる
$ sudo pip3 install --upgrade pip

# 再読み込み
$ hash -r

# boto3 install
$ pip install boto3 # <-- sudo不要 pip3 でも pip でも動作する

# opencv install
$ pip install opencv-python # <-- sudo不要 pip3 でも pip でも動作する

# この時点では、こんなエラーになる
# ImportError: libGL.so.1: cannot open shared object file: No such file or directory
$ python3 check.py

# 必要なものインストール
$ sudo yum install -y mesa-libGL.x86_64

# 動作確認
$ python3 check.py
<module 'boto3' from '/home/ec2-user/.local/lib/python3.7/site-packages/boto3/__init__.py'>
<module 'cv2.cv2' from '/home/ec2-user/.local/lib/python3.7/site-packages/cv2/cv2.cpython-37m-x86_64-linux-gnu.so'>
```

## `pip3` じゃなくて `pip` なのはなぜ？
- 実は `pip3` でもいけます。
- というか、現状では、 pip コマンドも pip3コマンドも結局は同じプログラムが動くようになっています。

 
```
$ pip -V
pip 21.0.1 from /usr/local/lib/python3.7/site-packages/pip (python 3.7)

$ pip3 -V
pip 21.0.1 from /usr/local/lib/python3.7/site-packages/pip (python 3.7) 
```

で、なぜ、 `pip` も `pip3` も同じ様になっているかというと、 upgradeしたあとで色々設定されたからです。
ついでに `sudo` が不要になったのも、このタイミングで設定がなされたからです。
 
ちなみに、Cloud9環境作成時点だとこうなっています
 
```
# 初期状態ではこうなっています == pip と pip3 が別の実体を指している
$ pip -V
pip 9.0.3 from /usr/lib/python2.7/site-packages (python 2.7)

$ pip3 -V
pip 9.0.3 from /usr/lib/python3.7/site-packages (python 3.7)
```

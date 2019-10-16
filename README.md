# json_parser

labelmeで作成したjsonファイルをimage-labelling-toolのjsonファイルの様式にパースを行います.
scriptの中にあるjson_parser.pyをlabelmeで作成したjsonファイルとイメージファイルが入っているフォルダにコピーし、pythonで実行してください.

例
dataset/にlabelmeで作成したjsonファイルとイメージファイルがあるものとします.

```
$ cd dataset
$ ls
IMG_5640.JPG	IMG_5641.JPG	IMG_5642.JPG
IMG_5640.json	IMG_5641.json	IMG_5642.json
```

```
$ cd ..
$ git clone https://github.com/Yu1313321/json_parser.git
$ cp ./json_parser/script/json_parser.py ./dataset/
$ cd dataset
$ python json_parser.py
$ ls
IMG_5640.JPG			IMG_5641__labels.json
IMG_5640.json			IMG_5642.JPG
IMG_5640__labels.json	IMG_5642.json
IMG_5641.JPG			IMG_5642__labels.json
IMG_5641.json			json_parser.py
```
labelmeのjsonファイル"hoge.json"をパースするとimage-labelling-toolのjsonファイルの名前は"hoge__labels.json"となります。

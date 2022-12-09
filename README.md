# easy-ocr-tool
EasyOCRを使って画像読み込みを行うツールです  

## EasyOCRツール仕様
picturesフォルダ配下に読み込ませたい画像を配置ください。
その後、exec_ocr.pyを実行すれば、画像内のテキストをコンソールに出力します。


## スタブ利用の前提  
ローカル環境に「Python」がインストールされていることを前提とします  
  
### （参考）Pythonインストールの仕方  
インストールの仕方は特に問いませんが、  
Chocolateyを使ったインストールが楽ですのでおすすめです  

- ChocolateyによるPythonインストール手順  
https://qiita.com/ns_k/items/bedaa80f4a5129e4eef4  


## ローカルセットアップ手順(１回だけ行えばOK)
- コマンドラインでeasy-ocr-toolに移動
```
cd C:\xxxx\easy-ocr-tool 
```

- 仮想環境作成
```
python -m venv .env
```

- 仮想環境アクティベート
```
[Power Shell]
.env/Scripts/Activate.ps1

[Shell]
.env/Scripts/activate
```

- 関連モジュールインストール
```
[Power Shell]
python -m pip install -r requirements.txt

※なんでかはわからないが、pip installがうまく動かない
　python -m pip install　なら大丈夫

[Shell]
pip install -r requirements.txt
```

## EasyOCR起動手順
- （前準備）画像配置

easy-ocr-tool/pictures/配下に画像を配置します（複数画像OK）


- コマンドラインでeasy-ocr-toolに移動
```
cd C:\xxxx\easy-ocr-tool 
```

- 仮想環境アクティベート
```
[Power Shell]
.env/Scripts/Activate.ps1

[Shell]
.env/Scripts/activate
```

- アプリ起動
```
python exec_ocr.py
```



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
  
- Chocolateyインストール手順  
https://e4-odessa.itechh.ne.jp/%E9%96%8B%E7%99%BA%E8%B3%87%E6%96%99/%E9%96%8B%E7%99%BA%E7%92%B0%E5%A2%83%E6%A7%8B%E7%AF%89#Chocolatey%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB  

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



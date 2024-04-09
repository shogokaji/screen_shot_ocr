## scrrenshot_extractor
## 環境構築
### 必要ライブラリをインストール
```sh
pip install -r requirements.txt
```

### tesseractをインストール
```sh
brew install tesseract
```
使用する言語の学習データを[リポジトリ](https://github.com/tesseract-ocr/tessdata)から取得。
`brew list tesseract`でで確認して、share/tessdata/配下に配置（[参考](https://dev.classmethod.jp/articles/ocr-on-a-mac-device-with-pytesseract/)）

## 実行方法
実行ファイルは以下2つです。
### ▼ screen_shot.py
デスクトップの最新の画像からOCRででテキスト抽出し、クリップボードに保存します。  
対象拡張子は[.jpg, .jpeg, .png. .heic]です。  
※ heicはpngに変換してからテキストを抽出します。  
  
ファイル実行時の引数で解析に使用する学習データの言語を指定できます。  
使用できる言語は、`pytesseract.get_languages()`で確認できます。  
```python
pytesseract.get_languages()
# => ['eng', 'jpn', 'jpn_vert', 'osd', 'snum']

# 日本語データで解析して抽出する場合（指定しない場合、デフォルトのengが使用されます）
python image-extract.py jpn
```
### ▼ capture.py
キャプチャ範囲を選択してOCRを行いテキストを抽出します。  
ファイルを実行すると、範囲選択待受状態になります。  
ファイル実行後の2クリック目の座標からリリースした地点をキャプチャの範囲とします。（画像は保存されません）  
抽出完了後にクリップボードにテキストを保存します。  

### 備考
学習データは管理されておらず、抽出精度は辞書依存のため精度はお試し利用レベルです。

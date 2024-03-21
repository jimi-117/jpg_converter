import os
from pdf2docx import Converter

pdfs_folder = 'pdfs'  # PDFファイルが格納されているフォルダ
docs_folder = 'docs'  # DOCXファイルを保存するフォルダ

# docsフォルダが存在しない場合は作成
if not os.path.exists(docs_folder):
    os.makedirs(docs_folder)

# pdfsフォルダ内の全PDFファイルをリストアップ
pdf_files = [f for f in os.listdir(pdfs_folder) if f.endswith('.pdf')]

# 各PDFファイルをDOCXに変換
for pdf_file in pdf_files:
    pdf_path = os.path.join(pdfs_folder, pdf_file)
    docx_path = os.path.join(docs_folder, os.path.splitext(pdf_file)[0] + '.docx')
    
    # コンバータを作成
    cv = Converter(pdf_path)
    
    # PDFをDOCXに変換
    cv.convert(docx_path)
    
    # コンバータを閉じる
    cv.close()

print("変換が完了しました。")

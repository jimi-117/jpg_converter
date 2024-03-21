import os
import img2pdf
from PIL import Image

if __name__ == '__main__':
    output_folder = "./pdfs"  # 現在のディレクトリに対する相対パス
    images_folder = "./images"  # 現在のディレクトリに対する相対パス
    extension = ".jpg"  # 拡張子がJPEGのものを対象

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # imagesフォルダ内のすべてのJPEGファイルに対して処理
    for img_name in os.listdir(images_folder):
        if img_name.endswith(extension):
            img_path = os.path.join(images_folder, img_name)
            pdf_path = os.path.join(output_folder, os.path.splitext(img_name)[0] + '.pdf')
            try:
                with open(pdf_path, "wb") as f:
                    f.write(img2pdf.convert([Image.open(img_path).filename]))
            except Exception as e:
                print(f"エラーが発生しました: {e}")
                continue

    print('JPEGファイルのPDFへの変換が完了しました。')

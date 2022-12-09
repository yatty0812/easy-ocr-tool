import easyocr
import os
import glob


def exec_ocr():
    reader = easyocr.Reader(['en','ja']) # this needs to run only once to load the model into memory

    # 処理ルート
    proc_root_dir = os.path.dirname(os.path.abspath(__file__))
    # 処理ルートディレクトリループ
    images = glob.glob(f"{proc_root_dir}/pictures/*")

    print("ORC実行！")
    for img in images:
        result = reader.readtext(img, detail=0)
        print(f"{img} --------------------------")
        print(result)

        # TEST
        #if True:
        #    break
        
    print("ORC終了！")



if __name__ == "__main__":
    exec_ocr()

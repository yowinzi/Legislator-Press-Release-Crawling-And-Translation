import googletrans
import os
import time

def main():

    translator = googletrans.Translator()

    source = os.getcwd() + '/Chinese/'
    
    target = os.getcwd() + '/English/'

    files = os.listdir(source)

    for file in files:

        fp = open(source+file, "r", encoding="utf-8")
        texts = fp.readlines()

        result = ''
        for text_ in texts:
            result += translator.translate(text_,src='zh-tw',dest= 'en').text
            time.sleep(2)

        fp.close()

        fp = open(target+file, "w", encoding="utf-8")
        fp.write(result)
        fp.close()
        


if __name__ == '__main__':

    main()

import pandas as pd

from langdetect import detect
from google_trans_new import google_translator  

translate_count = 0

#simple function to detect and translate text 
def detect_and_translate(text,target_lang):
    try: 
        result_lang = detect(text)
    except:
        return text
        
    if result_lang == target_lang:
        return text 
    
    else:
        translator = google_translator()
        translate_text = translator.translate(text,lang_src=result_lang,lang_tgt=target_lang)
        translate_count = translate_count + 1
        print('translate_count: ', translate_count)
        return translate_text 

# sentence = "I hope that, when I've built up my savings, I'll be able to travel to Mexico"

# print(detect_and_translate(sentence,target_lang='sw'))

data = pd.read_csv('../reviews.csv')
data.fillna('none', inplace=True)

for index, row in data['comments'].iteritems():
    res = detect_and_translate(row, 'en')
    data.loc[index, 'translated_comment'] = res
    print(index+1, " / 243184 completed")

data.to_csv('reviews_with_translations.csv')

# [done] check with index printed in for loop for tracking
# can try multithreading if this takes longer. Code in readme repo

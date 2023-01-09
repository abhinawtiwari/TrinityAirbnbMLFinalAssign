import pandas as pd

from langdetect import detect
from google_trans_new import google_translator  

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
        return translate_text 

# sentence = "I hope that, when I've built up my savings, I'll be able to travel to Mexico"

# print(detect_and_translate(sentence,target_lang='sw'))

data = pd.read_csv('../reviews.csv')
data.fillna('none', inplace=True)
data = data.head(100)

for index, row in data['comments'].iteritems():
    res = detect_and_translate(row, 'en')
    data.loc[index, 'translated_comment'] = res

data.to_csv('reviews_with_translations.csv')
# from google_trans_new import google_translator

# translator = google_translator()

from googletrans import Translator

translator = Translator()

# sentence = "Tanzania ni nchi inayoongoza kwa utalii barani afrika"
# # translate_text = translator.translate(sentence,lang_tgt='en') 
# translate_text = translator.translate(sentence) 

# print(translate_text.text)


translated_text = translator.translate('안녕하세요.')
print(translated_text.text)

# translated_text = translator.translate('안녕하세요.', dest='ja')
# print(translated_text.text)

# translated_text = translator.translate('veritas lux mea', src='la')
# print(translated_text.text)
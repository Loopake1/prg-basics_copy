word = input("Enter a word to translate: ")
translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}
if word.lower() in translations.keys():
    print(translations[word.lower()],'translation to polish')
else:
    print('There is no translation for such a word')
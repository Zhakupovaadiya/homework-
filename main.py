
def analyze_text(text):
    text = text.lower()
    vowels = "aeiouy"

    clean_text = ""
    for i in range(len(text)):
        if text[i].isalpha() or text[i]==" ":
            clean_text += text[i]
    un_vow=""
    for i in range(len(clean_text)):
        if clean_text[i] in vowels and clean_text[i] not in un_vow:
            un_vow += clean_text[i]
    words = clean_text.split()
    result = []
    for word in words:
        if len(word)>=5:
            if word[0] == word[-1]:
                if word not in result:
                    result.append(word)
text="Hello. Effective. America. america."
print(analyze_text(text))



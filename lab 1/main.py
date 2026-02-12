#1
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

#2
def lambda_fun(l):
    words=l.split()
    words = filter(lambda w: not any(ch.isdigit() for ch in w), l)
    words = map(lambda w: W[::-1], words)
    words = filter(lambda w: len(w) % 2 == 0, words)
    return " ".join(words)
print(lambda_fun(["hello", "world"]))

#3
def top_k_words(text, k):
    text = text.lower()

    cleaned = " "
    for i in text:
        if i.isalpha() or i==" ":
            cleaned += i
    words = cleaned.split()
    counts = {}
    for word in words:
        if word not in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    sorted_w = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    result=[]
    for i in range(min(k, len(sorted_w))):
        result.append(sorted_w[i][0])
    return result
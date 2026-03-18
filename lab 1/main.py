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
    return result
text="Hello. Effective. America. america."
print(analyze_text(text))

#2
def lambda_fun(l):
    words=l.split()
    words = filter(lambda w: not any(ch.isdigit() for ch in w), words)
    words = map(lambda w: w[::-1], words)
    words = filter(lambda w: len(w) % 2 == 0, words)
    return " ".join(words)
print(lambda_fun("python"))

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
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    sorted_w = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    result=[]
    for i in range(min(k, len(sorted_w))):
        result.append(sorted_w[i][0])
    return result
print(top_k_words("hi world", 3))

#4
process = lambda a: " ".join(
    word.lower()
    for word in a.split()
    if sum(1 for c in word if c.isupper()) == 1
    and not word[0].isupper()
    and not word[-1].isupper()
)
print(process("aBc WoRld teSt"))

#5
def compress_text(text):
    result = ""
    count = 1
    for i in range(1, len(text)):
        if text[i].lower() == text[i-1].lower():
            count +=1
        else:
            if count>1:
                result += text[i-1]+str(count)
            else:
                result += text[i-1]
            count = 1
    if count>1:
        result += text[-1]+str(count)
    else:
        result += text[-1]
    return result
print(compress_text("aaBBcDDD"))

#6
filter_words = lambda text: list(
    filter(lambda w: len(w) >= 4 and len(set(w.lower())) == len(w) and not any(c.isdigit() for c in w), text.split())
)
print(filter_words("apple moon asdf test12 board"))

#7
def palindrome_words(text):
    clean_text = ""
    for p in text:
        if p.isalpha() or p==" ":
            clean_text += p
        else:
            clean_text += " "
    words = clean_text.lower().split()
    unique = []

    for word in words:
        if len(word)>=3:
            if word == word[::-1]:
                unique.append(word)
    unique.sort(key=lambda x: len(x), reverse=True)
    return unique
text = "level fourty radar apple"
print(palindrome_words(text))

#8
transform_text = lambda text: " ".join(
    map(lambda w: w if any(c.isdigit() for c in w)
    else ("VOWEL" if w[0].lower() in "aeiou" else "CONSONANT"), text.split())
)
print(transform_text("apple test25 dog"))

#9
def alternate_case_blocks(text, n):
    result = ""
    block_index = 0
    for i in range(0, len(text), n):
        block = text[i:i+n]
        if block_index % 2 == 0:
            result += block.upper()
        else:
            result += block.lower()
        block_index += 1
    return result
print(alternate_case_blocks("HelloWorld", 3))

#10
count_words = lambda text: sum(
    1 for w in text.split() if any(c.isdigit() for c in w) and not w[0].isdigit() and len(w) >= 5
)
print(count_words("test1 banana 123home hello2"))

#11
def common_unique_chars(s1,s2):
    result = ""
    for ch in s1:
        if ch != " " and not ch.isdigit():
            if ch in s2 and ch not in result:
                result += ch
    return result
print(common_unique_chars("hello world", "yellow bird"))

#14
filter_words = lambda text: ",".join(
    filter(lambda w: len(set(c.lower() for c in w if c.isalpha())) > 3 and
    all(w.lower().count(v)<=1 for v in "aeiou"), text.split())
)
print(filter_words("planet moon sky cloud"))

#16
def transform_list(nums):
    result = []
    for num in nums:
        if num < 0:
            continue
        if num%2 == 0:
            result.append(num ** 2 )
        else:
            if num > 10:
                s = 0
                for digit in str(num):
                    s += int(digit)
                result.append(s)
            else:
                result.append(num)
    return result
print(transform_list([1, 2, -3, 4, 5, -6, 7, 8, 9]))

#17
process_nums = lambda nums: list(
    map(lambda x: x**2, filter(lambda x: (x%3==0 or x%5==0) and x%15 != 0 and len(str(abs(x)))%2==1, nums))
)
print(process_nums([1, 2, 3, 30, 5, -6, 7, 111, 9]))

#18
def flatten_and_filter(lst):
    result = []
    stack = lst.copy()
    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(item)
        elif isinstance(item, (int, float)):
            if (
                item>0 and
                item%4 != 0 and
                len(str(int(abs(item))))>1
            ):
                result.append(item)
    return sorted(result)
lst = [1,[12, -5, [33, [44, 101]]], 7]
print(flatten_and_filter(lst))

#19
func = lambda a, b: [x for x, y in zip(a,b) if x ==y and x%2 == 0]
a=[2,3,4,6,7]
b=[2,5,4,9,7]
print(func(a,b))

#20
def max_subbary_sum(nums, k):
    max_sum = None
    n = len(nums)
    for i in range(n-k+1):
        window = nums[i:i+k]
        valid = True
        for x in window:
            if x<=0:
                valid = False
                break
        if valid:
            current_sum = 0
            for x in window:
                current_sum += x
            if max_sum is None or current_sum > max_sum:
                max_sum = current_sum
    return max_sum
print(max_subbary_sum([1,2,0,4,8,6], 3))

#21
func = lambda lst: [
    s.upper()
    for s in lst
    if s.isalpha() and len(s)>4 and len(set(s)) == len(s)
]
lst = ["hello","1234","banana","python","world"]
print(func(lst))

#22
def group_by_parity_and_sort(nums):
    evens = []
    odds = []
    for num in nums:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
    for arr in (evens, odds):
        n = len(arr)
        for i in range(n):
            for j in range(0,n-i-1):
                if arr[j]>arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    return evens+odds
nums = [5,2,9,4,7,1,6]
print(group_by_parity_and_sort(nums))

#23
func = lambda lst: [
    x for i, x in enumerate(lst)
    if i>1
    and all(i%j != 0 for j in range(2, int(i**0.5)+1))
    and x%2 != 0
    and x > sum(lst)/len(lst)
]
lst=[1,5,11,7,2,9]
print(func(lst))

#24
def longest_increasing_sublist(nums):
    if not nums:
        return []
    max_sub = []
    current_sub = [nums[0]]
    for i in range(1,len(nums)):
        if nums[i] > nums[i-1]:
            current_sub.append(nums[i])
        else:
            if len(current_sub)>len(max_sub):
                max_sub = current_sub
            current_sub = [nums[i]]
    if len(current_sub)>len(max_sub):
        max_sub = current_sub
    return max_sub
nums = [1, 2, 3, 1, 2, 5, 6, 1]
print(longest_increasing_sublist(nums))

#25
func = lambda lst: [
    sum(sub)/len(sub)
    for sub in lst
    if len(sub)>=3 and sum(sub)%2==0
]
data = [[1, 2, 3], [2, 2, 2], [1, 1], [4, 4, 4, 4]]
print(func(data))

#26
def remove_duplicates_keep_last(nums):
    seen = []
    result = []
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] not in seen:
            seen.append(nums[i])
            result.insert(0, nums[i])
    return result
nums = [1, 2, 3, 2, 4, 1, 5]
print(remove_duplicates_keep_last(nums))

#27
func = lambda lst: sorted(lst, key=lambda x: (-len(x), x))[:5]

words = ["apple", "hi", "banana", "cat", "alphabet", "dog", "zebra"]
print(func(words))

#28
def moving_average(nums, k):
    result = []
    for i in range(len(nums) - k + 1):
        window = nums[i:i + k]
        valid = True
        for x in window:
            if x < 0:
                valid = False
                break
        if valid:
            s = 0
            for x in window:
                s += x
            result.append(s / k)
    return result

nums = [1, 2, 3, -1, 5, 6]
k = 3
print(moving_average(nums, k))

#29
func = lambda a, b: [
    x for x in a
    if x not in b and x > sum(a) / len(a)
]

a = [1, 5, 10, 3, 8]
b = [3, 8]
print(func(a, b))

#30
def analyze_strings_list(words):
    result = []
    for word in words:
        has_digit = False
        for ch in word:
            if ch.isdigit():
                has_digit = True
                break
        if has_digit:
            continue
        if len(word) % 2 == 0:
            new_word = word[::-1]
        else:
            new_word = word.upper()
        if new_word not in result:
            result.append(new_word)
    return result

words = ["hello", "test1", "abc", "deed", "abc", "wow"]
print(analyze_strings_list(words))

#31
def invert_unique(d):
    result = {}
    for key in d:
        value = d[key]
        if value not in result:
            result[value] = []
        if key not in result[value]:
            result[value].append(key)
    return result
d = {'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 3}
print(invert_unique(d))

#32
func = lambda s: {
    x for x in s
    if x > sum(s)/len(s) and x % 2 != 0 and x % 5 != 0
}

s = {1, 3, 5, 7, 10, 11}
print(func(s))
#33
def merge_dicts_sum(d1, d2):
    result = {}
    for key in d1:
        result[key] = d1[key]
    for key in d2:
        if key in result:
            result[key] += d2[key]
        else:
            result[key] = d2[key]
    return result
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
print(merge_dicts_sum(d1, d2))

#34
def filter_sets(sets_list):
    result = []
    for s in sets_list:
        if len(s) > 3:
            has_negative = False
            has_even = False
            for x in s:
                if x < 0:
                    has_negative = True
                if x % 2 == 0:
                    has_even = True
            if not has_negative and has_even:
                result.append(s)
    return result
sets_list = [{1,2,3,4}, {1,-2,3,4}, {1,3,5}, {2,4,6,8}]
print(filter_sets(sets_list))

#35
func = lambda d: sorted(d, key=lambda k: (-d[k], k))[:5]

d = {'a':5,'b':2,'c':5,'d':3,'e':1,'f':4}
print(func(d))

#36
def deep_sum(d):
    total = 0
    for key in d:
        value = d[key]
        if isinstance(value, int):
            total += value
        elif isinstance(value, list):
            for x in value:
                total += x
        elif isinstance(value, dict):
            total += deep_sum(value)
    return total
d = {'a': 1, 'b': [2,3], 'c': {'d': 4, 'e': [5,6]}}
print(deep_sum(d))

#37
func = lambda a, b: {x for x in a ^ b if x % 2 == 0}
a = {1,2,3,4}
b = {3,4,5,6}
print(func(a, b))

#38
def sort_dict_by_value_length(d):
    items = list(d.items())
    n = len(items)
    for i in range(n):
        for j in range(n - i - 1):
            if (len(items[j][1]) > len(items[j+1][1]) or
               (len(items[j][1]) == len(items[j+1][1]) and items[j][0] > items[j+1][0])):
                items[j], items[j+1] = items[j+1], items[j]
    return items
d = {'a':'hi', 'b':'hello', 'c':'hey', 'd':'a'}
print(sort_dict_by_value_length(d))

#39
def common_elements_all(sets_list):
    if not sets_list:
        return set()
    result = sets_list[0].copy()
    for s in sets_list[1:]:
        new_result = set()
        for x in result:
            if x in s:
                new_result.add(x)
        result = new_result
    return result
sets_list = [{1,2,3}, {2,3,4}, {2,5,3}]
print(common_elements_all(sets_list))

#40
func = lambda d: {
    k: sorted([x for x in v if x % 2 != 0])
    for k, v in d.items()
    if [x for x in v if x % 2 != 0]
}
d = {'a':[1,2,3], 'b':[2,4], 'c':[5,7]}
print(func(d))

#41
def group_by_length(words):
    result = {}
    for word in words:
        l = len(word)
        if l not in result:
            result[l] = []
        if word not in result[l]:
            result[l].append(word)
    return result
words = ["hi","hello","hey","hi","world"]
print(group_by_length(words))

#42
func = lambda s: {
    x for x in s
    if x.isalpha() and len(x) > 4 and len(set(x)) == len(x)
}
s = {"hello","world","abcde","aabbc","12345"}
print(func(s))

#43
def invert_dict_strict(d):
    result = {}
    count = {}
    for k in d:
        v = d[k]
        count[v] = count.get(v, 0) + 1
    for k in d:
        v = d[k]
        if count[v] == 1:
            result[v] = k
    return result
d = {'a':1,'b':2,'c':1,'d':3}
print(invert_dict_strict(d))

#44
def top_k_frequent(nums, k):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    items = list(freq.items())
    n = len(items)
    for i in range(n):
        for j in range(n - i - 1):
            if (items[j][1] < items[j+1][1] or
               (items[j][1] == items[j+1][1] and items[j][0] > items[j+1][0])):
                items[j], items[j+1] = items[j+1], items[j]
    result = set()
    for i in range(min(k, len(items))):
        result.add(items[i][0])
    return result
nums = [1,1,2,2,3,3,3,4]
print(top_k_frequent(nums, 2))

#45
func = lambda d: {
    k: v for k, v in d.items()
    if v >= sum(d.values())/len(d) and v % 2 != 0
}
d = {'a':1,'b':4,'c':5,'d':7}
print(func(d))
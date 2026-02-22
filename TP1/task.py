# ! were making it to the maang companies with this one !
# made with rage and tears by rahim


data = [ 
    'Today she cooked 4 bourak. Later, she added two chamiyya and 1 pizza.',
    'Five pizza were ready, but 3 bourak burned!',
    'We only had 8 chamiyya, no pizza, and one tea.',
    'Is 6 too much? I ate nine bourak lol.'
]

numbers = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
}

punctuation = ".…,;:’'\"-()[]{}“”"


def normalise(text):
    cleaned_text = ""
    text = text.lower()
    
    for char in text:
        if char in punctuation:
            continue
        elif char in numbers:
            cleaned_text += numbers[char]
        elif char == "?" or char == "!":
            cleaned_text += " " + char
        else:
            cleaned_text += char
    
    cleaned_text = cleaned_text.split()
    cleaned_text = " ".join(cleaned_text)
    
    return cleaned_text

def tokenize(text):
    return text.split()


for sentence in data:
    normalized = normalise(sentence)
    print(normalized)
    print(tokenize(normalized))
def index_text(filename):
    word_index = {}
    try:
        file = open(filename, 'r', encoding='utf-8')
        line_number = 0
        while True:
            line = file.readline()
            if not line:
                break
            words = line.lower().split()
            unique_words = []
            for word in words:
                if word not in unique_words:
                    unique_words.append(word)
            for word in unique_words:
                if word not in word_index:
                    word_index[word] = []
                if line_number not in word_index[word]:
                    word_index[word].append(line_number)
            line_number += 1
        file.close()
    except FileNotFoundError:
        print(f"Fel: Filen {filename} hittades inte.")
        return None
    return word_index


def important_words(an_index, stop_words):
    if not an_index:
        return []
    
    """Skapa frekvenslista utan stoppord"""
    freq_list = []
    for word in an_index:
        if word not in stop_words:
            freq_list.append((word, len(an_index[word])))
    
    n = len(freq_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if freq_list[j][1] < freq_list[j+1][1]:
                freq_list[j], freq_list[j+1] = freq_list[j+1], freq_list[j]
    
    """Hämta de 5 vanligaste orden"""
    top_words = []
    for i in range(min(5, len(freq_list))):
        top_words.append(freq_list[i][0])
    
    return top_words



def main():
    stop_words = ['och', 'jag', 'som', 'det', 'för']
    
    while True:
        filename = input("Ange en textfil: ").strip()
        if not filename:
            break
            
        word_index = index_text(filename)
        if word_index is None:
            continue
            
        top_words = important_words(word_index, stop_words)
        
        print("De viktigaste orden är:")
        for word in top_words:
            print(word)
        
        another = input("Vill du testa en annan fil? (j/n): ").lower()
        if another != 'j':
            break

if __name__ == "__main__":
    main()
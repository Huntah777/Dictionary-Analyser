def clean_text(text):
    """
    Simple helper to remove punctuation and lower case the text.
    """
    text = text.lower()
    for char in '-.,\n':
        text = text.replace(char, ' ')
    return text.split()


def analyze_frequency(words_list):
    """
    Create a dictionary that counts how many times each word appears.
    """
    frequency_dict = {}

    for word in words_list:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1

    return frequency_dict


def improved_analyse_frequency(words_list):
    frequency_dict = {}

    for word in words_list:
        frequency_dict[word] = frequency_dict.get(word, 0) + 1


def find_stats(freq_dict):
    """
    Find the most common and least common words.
    """
    if not freq_dict:
        return None, None

    # Find the key with the maximum value (Most Common)
    most_common = max(freq_dict, key=freq_dict.get)

    # Find the key with the minimum value (Least Common)
    least_common = min(freq_dict, key=freq_dict.get)

    return most_common, least_common


def filter_threshold(freq_dict, threshold):
    """
    Return a NEW dictionary containing only words
    that appear more than 'threshold' times.
    """
    result = {}

    #Loop through items. If value > threshold, add to 'result' dictionary.
    for key, value in freq_dict.items():
        if value > threshold:
            result[key] = value
    return result


# --- Main Execution ---
if __name__ == "__main__":
    sample_text = """
    Python is great. Python is dynamic. 
    Dictionaries are useful. Dictionaries are key-value pairs.
    Python is fun.
    """

    # 1. Clean the text
    words = clean_text(sample_text)

    # 2. Run your analysis
    word_counts = analyze_frequency(words)
    print(f"Full Counts: {word_counts}")

    # 3. Get Stats
    most, least = find_stats(word_counts)
    print(f"Most common: {most}")
    print(f"Least common: {least}")

    # 4. Filter
    popular_words = filter_threshold(word_counts, 1)
    print(f"Words appearing more than once: {popular_words}")

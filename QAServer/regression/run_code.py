import sys
import csv as csv
from format_answers import FormatAnswer
from calculate_features import get_all_scores

protocol_list = ['num_words', 'num_characters', 'num_misspelled', 'bin_start_interrogative', 'bin_end_qmark',
                 'num_interrogative', 'bin_start_small', 'avg_word_sentence', 'num_sentences', 'bin_url',
                 'readability_score', 'num_punctuations', 'bin_taboo', # 'grammar_check'
                 'Average IDF', 'Entropy', 'Polarity', 'Subjectivity']
formatanswers_func_list = ['get_total_words', 'get_total_number_of_characters', 'number_of_misspelled_words',
             'check_interrogative_start', 'check_question_mark_end', 'number_of_interrogative_words',
             'check_small_letter_start', 'average_words_per_sentence', 'get_number_of_sentences',
             'check_if_url_present', 'get_readability_score', 'number_of_punctuation_marks', 'check_for_profanity'] #'grammar_check']

with open(sys.argv[1], 'r',  encoding='ISO-8859-1',) as f:
    with open(sys.argv[2], 'w', encoding='ISO-8859-1', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        reader = csv.reader(f)
        row = next(reader)  # pass the file to our csv reader
        new_row = row
        new_row = row + protocol_list
        wr.writerow(new_row)
        # count = 1

        for row in reader:
            if len(row) < 1:
                continue

            content = row[0]
            print(content)
            new_row = row

            obj = FormatAnswer(content)
            for func in formatanswers_func_list:
                method = getattr(obj, func)
                new_row.append(str(method()))
            text, idf, H, polarity, subjectivity = get_all_scores(content)
            new_row.append(idf)
            new_row.append(H)
            new_row.append(polarity)
            new_row.append(subjectivity)

            wr.writerow(new_row)

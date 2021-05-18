#!/usr/bin/env python3

import json
import csv
import pprint
import re
import string
from nltk.corpus import stopwords

import nltk
nltk.download('stopwords')

def clean_question(quest, stop_words):
    # Clean an input string
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', quest)
    cleantext = " ".join([w for w in cleantext.split(" ") if w.lower() not in stop_words])
    # Remove punctuation
    cleantext = cleantext.translate(str.maketrans('', '', string.punctuation))
    #cleantext = cleantext.replace("\"", "")
    #cleantext = cleantext.replace("\'", "")
    return cleantext


if __name__ == '__main__':
    f = open("rawdata/jeopardy.json")
    data = json.loads(f.read())

    questions = {}
    for i, question in enumerate(data):
        show_id = question['show_number']
        category = question['category']
        question_str = question['question']
        answer_str = question['answer']
        q_and_a = {'question': question_str, 'answer': answer_str}
        entry = {category: [q_and_a]}
        if show_id not in questions:
            questions[show_id] = entry
        else:
            if category not in questions[show_id]:
                questions[show_id][category] = [q_and_a]
            else:
                questions[show_id][category].append(q_and_a)

    with open("rawdata/processed.json", "w") as outfile:
        json.dump(questions, outfile)

    # Split the processed json into train, dev, and test sets
    f = open("rawdata/processed.json", "r")
    questions = json.loads(f.read())
    print(f"Number of entries: {len(questions)}")
    shows = list(questions)
    
    
    stop_words = set(stopwords.words('english')) 
    f = open("data/all_data.qa-cat", "a")
    count = 0
    for show in shows:
        current_show = questions[show]
        categories = list(current_show)
        for category in categories:
            q_and_as = current_show[category] # List
            to_write = f"{category.lower()}\t"
            f.write(to_write)
            for q_and_a in q_and_as:
                count +=1
                question = q_and_a["question"].strip('\'').strip()
                question = clean_question(question, stop_words)
                answer = q_and_a["answer"].strip().lower()
                answer = [w for w in answer.split(" ") if w.lower() not in stop_words]
                answer = " ".join(answer)
                to_write = f" {question} {answer} "
                f.write(to_write)
            f.write("\n")
    print(count)
    
            
classes = [{'school_class': '1a', 'scores': [3, 1, 5, 2, 1, 2]}, {'school_class': '1b', 'scores': [4, 1, 2, 5, 5, 1]},
           {'school_class': '2a', 'scores': [4, 4, 5, 5, 4, 2]}, {'school_class': '2b', 'scores': [2, 5, 4, 3, 1, 1]},
           {'school_class': '3a', 'scores': [2, 5, 2, 4, 5, 3]}, {'school_class': '3b', 'scores': [4, 5, 1, 5, 4, 4]},
           {'school_class': '4a', 'scores': [1, 1, 3, 3, 3, 5]}, {'school_class': '4b', 'scores': [5, 2, 4, 3, 4, 2]},
           {'school_class': '5a', 'scores': [4, 3, 4, 3, 4, 3]}, {'school_class': '5b', 'scores': [1, 4, 3, 3, 4, 5]},
           {'school_class': '6a', 'scores': [4, 5, 1, 4, 4, 4]}, {'school_class': '6b', 'scores': [2, 5, 3, 4, 4, 3]},
           {'school_class': '7a', 'scores': [4, 1, 1, 1, 1, 5]}, {'school_class': '7b', 'scores': [3, 5, 1, 1, 3, 3]},
           {'school_class': '8a', 'scores': [4, 3, 1, 2, 4, 2]}, {'school_class': '8b', 'scores': [1, 5, 4, 1, 1, 5]},
           {'school_class': '9a', 'scores': [4, 5, 2, 4, 1, 5]}, {'school_class': '9b', 'scores': [3, 3, 5, 2, 3, 4]},
           {'school_class': '10a', 'scores': [2, 2, 4, 5, 3, 1]}, {'school_class': '10b', 'scores': [3, 5, 5, 1, 3, 5]}]
total_scores = 0
count = 0
for clazz in classes:
    class_name = clazz['school_class']
    all_scores = clazz['scores']
    median = sum(all_scores) // len(all_scores)
    total_scores += sum(all_scores)
    count += len(all_scores)
    print(class_name, median)
print('total', total_scores // count)

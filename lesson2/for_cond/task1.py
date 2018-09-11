#import random
import statistics

#[{'school_class': str(c) + random.choice(['a', 'b', 'c']), 'scores': [random.randint(2,5) for x in range(1,10)]} for c in range(1,10)]

my_data = [
    {'school_class': '1a', 'scores': [5, 3, 2, 5, 2, 2, 2, 3, 3]},
    {'school_class': '2a', 'scores': [3, 4, 4, 3, 3, 5, 3, 5, 4]},
    {'school_class': '3b', 'scores': [5, 5, 2, 4, 5, 2, 3, 2, 5]},
    {'school_class': '4c', 'scores': [2, 3, 4, 5, 4, 5, 5, 2, 2]},
    {'school_class': '5a', 'scores': [2, 3, 2, 4, 2, 3, 5, 3, 5]},
    {'school_class': '6b', 'scores': [2, 3, 5, 4, 4, 5, 2, 2, 2]},
    {'school_class': '7a', 'scores': [3, 4, 5, 2, 3, 3, 5, 2, 5]},
    {'school_class': '8c', 'scores': [2, 4, 4, 4, 3, 3, 3, 5, 5]},
    {'school_class': '9c', 'scores': [4, 3, 3, 5, 5, 3, 5, 5, 2]},
]


def mean_scores(lst, general=False):
    if general:
        all_scores_list = []
        for class_dict in lst:
            all_scores_list.extend(class_dict['scores'])
        print(f"mean in school = {statistics.mean(all_scores_list)}")
        return None

    for class_dict in lst:
        print(f"mean in class {class_dict['school_class']} = {statistics.mean(class_dict['scores'])}")

mean_scores(my_data, general=True)

mean_scores(my_data)
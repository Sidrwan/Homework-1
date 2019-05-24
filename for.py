school = [{'school_class': '4a', 'scores': [3,4,4,5,2]}, 
            {'school_class': '4b', 'scores': [5,3,4,4,2]}, 
            {'school_class': '4c', 'scores': [3,5,2,5,3]}]

def great_point_average(other):
    list_score1 = list()
    for point in school:
        for grades in point['scores']:
            list_score1.append(grades)
        return(list_score1)

result = sum(great_point_average(school))/len(great_point_average(school))
print("Средний бал по школе",result)




for grades2 in school:
    list_score2 = sum(grades2['scores'])/len(grades2['scores'])
    print("Средний бал по классам", list_score2)

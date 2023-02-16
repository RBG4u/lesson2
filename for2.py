stock = [
		{'name': 'iPhone 12', 'stock': 24, 'price': 65432.1,
                'discount': 25},
		{'name': 'Samsung Galaxy S21', 'stock': 8, 'price': 50000.0,
                'discount': 10},
		{'name': '', 'stock': 18, 'price': 10000.0, 'discount': 10}
]

def discounted(price, discount, max_discount=30, tele_name=""):
    price = abs(price)
    discount = abs(discount)
    max_discount = abs(max_discount)
    if max_discount >= 100:
        raise ValueError("Слишком большая максимальная скидка")
    if discount >= max_discount:
        return price
    elif "iphone" in tele_name.lower() or not tele_name:
        return price
    else:
        return price - (price * discount / 100)
    
for tele in stock:
    tele['price_final'] = discounted(tele['price'], tele['discount'], tele_name = tele['name'])

print(stock)

classes = [
    {'name': '3А', 'scores': [3,4,4,5,2]},
    {'name': '3Б', 'scores': [5,5,3,2,2]},
    {'name': '3В', 'scores': [4,5,3,5,4]},
]

def count_average(students_scores):
    scores_sum = 0
    for score in students_scores:
        scores_sum += score
    scores_avg = scores_sum / len(students_scores)
    return scores_avg
avg_scores_sum = 0
for one_class in classes:
    class_score_avg = count_average(one_class['scores'])
    print(f"Средняя оценка для класса {one_class['name']}: {class_score_avg}")
    avg_scores_sum += class_score_avg



#for one_class in classes:
  #  avg_scores_sum += count_average(one_class['scores'])

school_avg = round(avg_scores_sum/len(classes), 1)
print(f'Средняя по школе: {school_avg}')

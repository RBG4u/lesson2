#while True:
#    user_say = input('Скажи что-нибудь: ')
#    if user_say.lower() == 'пока':
#        print('Ну пока')
#        break
#    else:
#        print('Сам ты {}'.format(user_say.lower()))


#humans = ['Вася', 'Маша', 'Паша', 'Никита', 'Валера', 'Витя']
#list = 0
#def name_search(lists):
 #   while lists[list] != 'Маша':
  #      lists[list] = humans.pop()
   #     print(lists[list])
    #print('Маша нашлась')

#print(name_search(humans))

def find_person(name):
    humans = ['Вася', 'Маша', 'Паша', 'Никита', 'Валера', 'Витя']
    list = 0
    try:
        while list != name:
            list = humans.pop()
        print(f'{name} найдено')
    except IndexError:
        print(f'Имя "{name}" не найдено')
humans = ['Вася', 'Маша', 'Паша', 'Никита', 'Валера', 'Витя']
print(humans)
find_person(str.capitalize(input('Введите имя: ')))


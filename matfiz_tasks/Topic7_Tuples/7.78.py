'''
'   Task #7.78
'   Created by Andrii Demchenko
'   Computer Mathematics, 1st grade
'
'   Task: Заданий вектор ГРУПА, компонентами якого ГРУПА(x) є
'         множини імен людей із вказаного списку тих,
'         що були в гостях у людини з ім'ям X (X∉ГРУПА[X]).
'         Визначити процедуру пошуку хоча б одної людини,
'          яка була в гостях в усіх
'         інших людей, імена яких містяться в компонентах вектора ГРУПА.
'''

# {1,2,3,4,5,6} - people

people = {1,2,3,4,5,6}
group = {1:{2,3,4,5},2:{1,5,6},3:{1,2,6},
         4:{1,2,3,5,6},5:{1,4},6:{1,2,4,5}}

final_set = set()
for p in people:
    for g in group:
        st = set(people)
        st.remove(p)
        if st == group[p]:
            final_set.add(p)

print(final_set)
        

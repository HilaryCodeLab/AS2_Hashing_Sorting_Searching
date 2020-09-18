from read_csv import read_csv
from operator import attrgetter
from binary_search import find


# setting variable to chess player's attribute
by_lname = attrgetter('lname')

arr = read_csv('chess-players.csv')
arr.sort(key=by_lname)

# Invoke find method from binary_search.py
result = find(arr, value='Zhao', key=by_lname)

if (result):
    print("Player found in the list")
    print(f'First Name: {result.fname}, Last Name: {result.lname}, Country: {result.country}, Born: {result.born}, '
          f'Died: {result.died}')

else:
    print("Not found Player")



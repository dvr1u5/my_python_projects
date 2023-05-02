N = int(input())
citiesdict = {}
for i in range(N):
    cities = input()
    space = cities.find(' ')
    country = cities[:space]
    cities = cities[space + 1::]
    citieslist = list(map(str, cities.split()))
    for j in citieslist:
        citiesdict[j] = country
M = int(input())
for i in range(M):
    cities2 = input()
    print(citiesdict[cities2])

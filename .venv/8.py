rost = []
rost_in = ""

while rost_in != '!':
    rost_in = input('Введите рост претендентов или введите "!" для выхода ')
    if rost_in != '!':
        rost.append(int(rost_in))


rost_cosmo = []
for i in range(len(rost)):
    if (int(rost[i]) >= 150 and int(rost[i]) <= 190):
        rost_cosmo.append(rost[i])

print('количество подходящих кандидатур: ' + str(len(rost_cosmo)))
print('Минимальный рост: ' + str(min(rost_cosmo)) + ' Максимальный рост: ' + str(max(rost_cosmo)))
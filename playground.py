list_ = []


for i in range(0,10):
    dict_ = {}
    dict_['Hi'] = f'Hello {i}'
    dict_['Bye'] = f'Goodbye {i}'
    list_.append(dict_)

list_.append({'count':len(list_)})

print(list_[-1])
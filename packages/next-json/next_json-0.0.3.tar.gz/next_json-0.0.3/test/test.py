from next_json.next_json_obj import NextJson

foo = NextJson()

foo.a = 1
foo.c.d = '牛逼'
foo['hh'] = '非常牛逼'

for key, value in foo.items():
    print(f'key={key}', f'value={value}')

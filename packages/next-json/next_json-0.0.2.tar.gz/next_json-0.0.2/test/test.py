from next_json.next_json_obj import NextJson

foo = NextJson('{"a": 1, "b": 2}')
foo.a = 'hh'
print(foo)

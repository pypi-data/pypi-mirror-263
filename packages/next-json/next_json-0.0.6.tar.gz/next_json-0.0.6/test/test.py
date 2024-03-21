from next_json.next_json_obj import NextJson

foo = NextJson()
foo.on('set', lambda k, v: print(f'检测到属性修改: key={k} value={v}'))
foo.once('set', lambda k, v: print(f'检测到属性修改(这个函数只触发一次): key={k} value={v}'))
foo.on('get', lambda k, d, v: print(f'检测到属性获取: key={k} default={d} value={v}'))
foo.on('del', lambda k: print(f'检测到属性删除: key={k}'))

foo.a = 1
foo.c.d = '牛逼'
foo['hh'] = '非常牛逼'
del foo.hh
# del不存在的属性不会报错
del foo.hh

print(foo)

from next_json.next_json_obj import NextJson

foo = NextJson()
foo.on('set', lambda k, v: print(f'检测到属性修改: key={k} value={v}'))
foo.once('set', lambda k, v: print(f'检测到属性修改(这个函数只触发一次): key={k} value={v}'))
foo.on('get', lambda k, d, v: print(f'检测到属性获取: key={k} default={d} value={v}'))
foo.on('del', lambda k: print(f'检测到属性删除: key={k}'))

foo.a = 1
foo.c.d = '牛逼'
foo['hh'] = '非常牛逼'
print('删除属性', foo.pop('hh'))
print('删除属性', foo.popitem())
print('foo1', foo)
foo.update({
    "a": 233,
    "c": 6666,
    "d": {}
})
print('foo2', foo)
foo.update('{"a": "哈哈哈","c": 9999999}')
print('foo3', foo)
foo.update(nb='非常牛逼', nb2='6666')
print('foo4', foo)
print('set default1', foo.set_default('nb', 1))
print('set default2', foo.set_default('nb666', 666))
print('values=', foo.values())
print('keys=', foo.keys())
print('items=', foo.items())
print(foo)

### 方便快捷Json数据处理

支持用[]和.访问以及修改属性

支持get(键,默认值) 方法获取属性

支持set(键,属性) 方法修改属性
如果要访问get和set的属性名字,使用['get']和['set']
否则将会获取到方法实例,赋值直接赋值即可

### 初始化

```python
from next_json.next_json_obj import NextJson

foo = NextJson()  # 等于NextJson({})
foo1 = NextJson({"a": 1, "b": 2})
foo2 = NextJson('{"a": 1, "b": 2}')
foo3 = NextJson(a=1, b=2)

```

```python
from next_json.next_json_obj import NextJson

foo = NextJson()  # 或NextJson({}) 支持python字典,json字符串,其他NextJson对象,
# 支持NextJson(a=1,b=2) 具名参数初始化

foo.a.b = 1
foo.get = '牛逼不'
print(foo.get('get'))
```
```angular2html
输出为: 牛逼不
```

访问和函数名相同的属性需要使用[]获取,否则将会获取到函数实例,例如foo['get']
foo.get会获取到get函数本身,赋值可直接使用foo.get = 1赋值


支持del删除属性,删除存在属性不会报错

支持迭代器获取key访问属性

支持len()获取长度

支持in语法判断值是否存在

支持str转json字符串

支持监听属性修改获取以及删除

不存在的属性连续访问返回新的空NextJson对象,

空对象布尔判断返回false,如果对该对象添加新的属性

那么该对象将会自动添加到父NextJson中,键为获取该对象时使用的键,例子:

```python
from next_json import NextJson

obj = NextJson()  # 或NextJson({})支持传入字典，或json字符串
print(obj)
test = obj.hh
test.bb = 1
test2 = obj.hh2
print(obj)
```

输出结果为:

```
{}
{"hh": {"bb": 1}}
```

hh和hh2对象会在访问hh和hh2属性时创建,由于hh2没有做任何更改,则不会被添加到父对象实例中

所有的键在传入时自动转换为字符串
所有的不可被json序列化的值会被转换为字符串(NextJson对象除外)
所有的dict对象的值会被自动转换为新的nextJson对象

### 事件监听

```python
from next_json.next_json_obj import NextJson

foo = NextJson()
foo.on('set', lambda k, v: print(f'检测到属性修改: key={k} value={v}'))
foo.once('set', lambda k, v: print(f'检测到属性修改(这个函数只触发一次): key={k} value={v}'))
foo.on('get', lambda k, v: print(f'检测到属性获取: key={k} default={v}'))
foo.on('del', lambda k: print(f'检测到属性删除: key={k}'))

foo.a = 1
foo.c.d = '牛逼'
foo['hh'] = '非常牛逼'
del foo.hh
# del不存在的属性不会报错
del foo.hh

print(foo)
```

#### 输出
```angular2html
检测到属性修改: key=a value=1
检测到属性修改(这个函数只触发一次): key=a value=1
检测到属性获取: key=c default={}
检测到属性修改: key=c value={}
检测到属性修改: key=hh value=非常牛逼
检测到属性删除: key=hh
{"a": 1, "c": {"d": "牛逼"}}
```

### 函数

```angular2html
get(key) 获取属性

set(key,value) 设置属性

to_dict() 转为python字典

on(event,函数) 监听事件 event为set,get,del

once(event,函数) 监听事件,只触发一次

off(event,函数) 取消监听事件

replace_data(data) 替换数据 data可以为python字典或json数据

items() 迭代器,返回key和value,与字典相同

```

### 文件管理类

manager = NextConfigManager("config.json")

即可得到配置文件管理对象,文件不存在自动创建

存在则自动读取并解析json内容

对manager.config对象的一切读写都会在python进程结束后自动保存
可调用save()方法主动保存,线程安全,save方法加锁

```python
from next_json import NextConfigManager, JsonDictManager, NextJson

# NextConfigManager管理json配置


manager = NextConfigManager("config.json")
manager.config.a = 1
manager.config.b = 4

config = manager.config
# 更改属性
config.a = 'hh'
config.b = 1
# json不能序列化的对象在保存会被转为字符串 {"a": "hh", "b": 1, "c": "<class '__main__.JsonDictManager'>"}
config['c'] = JsonDictManager
config[111] = '非常牛逼'
config['111'] = '非常牛逼2'
# 获取属性,可使用.或者[]
print(config.c)  # 输出 <class '__main__.JsonDictManager'>
print(config['c'])  # 输出 <class '__main__.JsonDictManager'>
# 获取key为hh的值,为空返回1
print(config.get('hh', 1))
print(config)
# ccc属性不存在,自动新建空字典
config.ccc.ddd = 1
config.arr = []
config.arr.append(1)
# 添加字典会被自动转换为另一个config对象,继承访问方式和修改方式
config.obj = {}
config.obj.c = 1
config.obj.d = '牛逼不'
# 不存在的属性连续调用不会报错，而是返回false
if not config.xxx.bbb.ccc.ddd:
    print('hh')
print(config)
# 迭代
for key in manager.config:
    print(f'key={key}', f'value={manager.config[key]}')
# 删除键值对
del manager.config.a
del manager.config['a']

# 转为python dict对象
manager.config.to_dict()

# 获取长度
print(len(manager.config))
# 默认python进程关闭后自动save()
# manager.save()

# instant_save=True开启后，任何属性更改后立即自动save一次
# manager = NextConfigManager("config.json", instant_save=True)


```
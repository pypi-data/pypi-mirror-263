from next_json import NextConfigManager, JsonDictManager, NextJson

# NextConfigManager管理json配置


manager = NextConfigManager("config.json")
manager.config.a = 1
manager.config.b = 4

config = manager.config
# 更改属性
config.a = 'hh'
config.b = 1
# json不能序列化的对象会被转为字符串 {"a": "hh", "b": 1, "c": "<class '__main__.JsonDictManager'>"}
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
print('objh', config.obj)
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
# del manager.config['a']

# 转为python dict对象
manager.config.to_dict()

# 获取长度
print(len(manager.config))
# 默认python进程关闭后自动save()
# manager.save()

# instant_save=True开启后，任何属性更改后立即自动save一次
# manager = NextConfigManager("config.json", instant_save=True)
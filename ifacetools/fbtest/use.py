# -*- coding: utf-8 -*-
# @Time    : 2019/8/12 0012 23:40
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : use.py
# @Software: PyCharm
import factory
from fbtest.userfc import UserFactory

seq=[]
uf=UserFactory()
print(uf.__dict__)
seq.append(uf.__dict__)
seq.append(UserFactory().__dict__)
print(seq)


list=[]
fss=factory.build_batch(UserFactory,4)
for fs in fss:
    list.append(fs.__dict__)
print(list)

uff=UserFactory(shipped=True)
print(uff.__dict__)
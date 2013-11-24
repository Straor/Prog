# -*- coding: utf-8 -*-
#comment marchent les opérateurs logiques
a=True
b=True
print("vrai et vrai",a and b)
print("vrai ou vrai",a or b)
print("pas(vrai et vrai)",not (a and b))
print("pas(vrai ou vrai)",not(a or b))
a=False
b=False
print("faux et faux", a and b)
print("faux ou faux",a or b)
print("pas(faux et faux)", not(a and b))
print("pas(faux ou faux)",not(a or b))
a=False
b=True
print("faux et vrai", a and b)
print("faux ou vrai",a or b)
print("pas(faux et vrai)",not(a and b))
print("pas(faux ou vrai)",not(a or b))
a=True
b=False
print("vrai et faux",a and b)
print("vrai ou faux",a or b)
print("pas(vrai et faux)",not(a and b))
print("not(vrai ou faux)",not(a or b))

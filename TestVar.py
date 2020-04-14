from matplotlib._color_data import TABLEAU_COLORS
from matplotlib._color_data import BASE_COLORS

TABLEAU_COLORS2 = (
    ('blue', '#1f77b4'),
    ('orange', '#ff7f0e'),
    ('green', '#2ca02c'),
    ('red', '#d62728'),
    ('purple', '#9467bd'),
    ('brown', '#8c564b'),
    ('pink', '#e377c2'),
    ('gray', '#7f7f7f'),
    ('olive', '#bcbd22'),
    ('cyan', '#17becf'),
)


# def myfunc(a,b):
#     a=4
#     b=5
#     print(a,b)
# myfunc(3,3)

#------- ПРОВЕРЕНО: РАБОТАЕТ
# rtk=len(TABLEAU_COLORS2)
# print(rtk)
# for i in range(rtk*2):
#     k=i % rtk
#     if k==0: print(' ')
#     (name,value)=TABLEAU_COLORS2[k]
#     print(k,' ', name,' ',value)
#------- ПРОВЕРЕНО: РАБОТАЕТ

# Проверено 2
# keylist=list(BASE_COLORS)
# print(keylist)
#
# rtk=len(BASE_COLORS)
# print('len=',rtk)
# for i in range(rtk*2):
#     k=i % rtk
#     if k==0: print(' ')
#     value=BASE_COLORS[keylist[k]]
#     print(k,' ', keylist[k],' ',value)
# Проверено 2

lenb=len(BASE_COLORS)
print('len(BASE_COLORS) = ',lenb)
z=0
for i in BASE_COLORS:
    print(z,' ',i,'  ',BASE_COLORS[i]) # BASE_COLORS[k]
    z=z+1

print('normal shut down')
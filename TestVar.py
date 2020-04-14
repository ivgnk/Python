from matplotlib._color_data import TABLEAU_COLORS

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

rtk=len(TABLEAU_COLORS2)
print(rtk)
for i in range(rtk*2):
    k=i % rtk
    if k==0: print(' ')
    (name,value)=TABLEAU_COLORS2[k]
    print(k,' ', name,' ',value)

print('normal shut down')
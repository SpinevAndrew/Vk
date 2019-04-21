import vk
import glob
session = vk.Session(access_token = '9ad47888f2bac9b52c71bf79ac37540e5db43e8d3eb47003674339ed256e358e68fe71fa4625c7d997620')
api = vk.API(session, v = '5.92')
list_input = glob.glob('*.txt')
for i in list_input:
    fin = open(i, 'r')
    s = []
    while True:
        line = fin.readline()
        if len(line) == 0:
            break
        line = line[15:]
        s.append(line)
    fin.close()

    spisok = set(s)
    fout = open(i,'w')
    itog_spisok = api.users.get(user_ids = spisok, fields = id)
    for il in range(len(itog_spisok)):
        fout.write('{}\n'.format(str(itog_spisok[il]['id'])))
    fout.close()
    
__version__ = '0.2'

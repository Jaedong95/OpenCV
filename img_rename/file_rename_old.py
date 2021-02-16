import os
input_path = 'TLH_19_1000/P1_preparation/img'
file_list_input = os.listdir(input_path)

idx = 0
new_name = "TLH_19_"

for i in file_list_input:
    idx += 1
    os.rename('TLH_19_1000/P1_preparation/img/{0}'.format(i),
              'TLH_19_1000/P1_preparation/img/' + new_name + '{0}.jpg'.format(idx))
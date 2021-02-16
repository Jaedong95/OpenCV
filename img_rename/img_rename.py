import os

input_path = 'OBGyn/TLH_21/TLH_21/img'
file_list_input = os.listdir(input_path)

idx = 0
for i in file_list_input:
    idx += 1
    os.rename('OBGyn/TLH_21/TLH_21/img/{0}'.format(i),
              'OBGyn/TLH_21/TLH_21/img_renamed/{0}.jpg'.format(idx))

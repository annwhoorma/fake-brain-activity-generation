import json
data = json.load(open('dataset_test_conn/label1/1.json'))

def str_to_list(src, depth=1, dtype=float):
    dst = []
    if depth == 2:
        src = src[1:-1].split('], ')
        src = list(map(lambda x: x[1:], src))
        src[-1] = src[-1][:-1]
        for i, l in enumerate(src):
            dst.append(l.split(', '))
            dst[-1] = list(map(dtype, dst[-1]))
    elif depth == 1:
        dst = src[1:-1].split(', ')
        dst = list(map(dtype, dst)) 
    return dst

edge_index = str_to_list(data['edge_index'], depth=2)
edge_attr =  str_to_list(data['edge_attr'])

print(edge_index)
print()
print(edge_attr)

for idx, attr in zip(zip(edge_index[0], edge_index[1]), edge_attr):
  with open('script.txt', 'a') as f:
    f.write(f'{idx}: {attr}\n')
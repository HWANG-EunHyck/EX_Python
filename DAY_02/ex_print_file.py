filename = '헛소리.txt'

msg = '헛소리 mk2'
f = open(filename, mode = 'w', encoding= 'utf=8')
f.write('에헤이')
f.write('\n')
print('에헤이 에헤이 에헤이','쿨쿨', sep = '-',file = f)
print(f'뭐라 할까 {msg}\n{msg} {msg}', file = f )
print('아라리 아라리 %s' %msg,file = f)
f.close()

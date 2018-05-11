name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
key=None
val=None
l=list()
d=dict()
lt=list()
for line in handle:
    if not line.startswith('From '):
        continue
    h=line.split()
    hr=h[5].split(':')
    hrs=hr[0]
    l.append(hrs)
for name in l:
    d[name]=d.get(name,0)+1
for k,v in sorted([(k,v) for k,v in d.items()]):
    print(k,v)

import sys
lino = sys.stdin.readlines()

def render_contact(filename):
    h = {}
    with open(filename, 'r') as num:
       for line in num:
            name, number = line.strip().split()
            h[name] = number
    return h


h = render_contact(sys.argv[1])

for patt in lino:
    name = patt.strip()
    print(f"Name: {name}")
    if name in h:
        print(f"Phone: {h[name]}")
    else:
        print("No such contact")

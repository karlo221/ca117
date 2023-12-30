from email.message import EmailMessage
import sys
lino = sys.stdin.readlines()

def render_contact(filename):
    h = {}
    with open(filename, 'r') as num:
       for line in num:
            name, number, email = line.strip().split()
            h[name] = number
            h[email] = email
    return h


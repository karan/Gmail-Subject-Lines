import gmaillib

f=open('subjects.txt', 'w')
account=gmaillib.account('', '')
emails = account.inbox(start=0, amount=5000)

for email in emails:
    if email.subject is not None:
        f.write(email.subject + '\n')
f.close()

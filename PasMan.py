def stored():
    use = input("Enter a username: ")
    pas = input("Enter a pasword: ")

    with open('pas.txt', 'a') as f:
        print("\n" + f.write(str(use) + ' | ' + str(pas)))
    
def view():
    with open('pas.txt', 'r') as f:
        for i in f.readlines():
            u = i.split('|')
            print('\nUSERNAME::' + str(u[0]) + '  PASSWORD::' + str(u[1]))


sp = 'Welcome \n PasMan'
print(sp)
op = input("Choose only one option [add/view]: ")
if op=="add":
    stored()
    input()
else:
    view()
    input()


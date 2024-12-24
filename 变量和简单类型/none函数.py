def Hello(name, password):
    if name == 'admin' and password == '123456':
        print('Hello, admin!')
        return 'success'
    else:
        print('Wrong username or password.')
        return None


a = Hello('admin', 'admin')
print(a)

import requests
from hashlib import sha512


class ValidateKEY:

    def checkactivation(self):

        activationkey = 'admin'
        hash_user = sha512(activationkey.encode()).hexdigest()
        userlogin = requests.get('https://site-7jo322wz2q-uc.a.run.app/d3d92938c54d99e82a6e0509a517b80e02dcdb3851b96956cb50ce29ef22bc3178176d53f43584212ed7dcfed9136efa6c1ffe8081bec8c51a02566a105d32ef').json()
        USERINFO = userlogin
        for usr in USERINFO:
            if hash_user in usr['b14361404c078ffd549c03db443c3fede2f3e534d73f78f77301ed97d4a436a9fd9db05ee8b325c0ad36438b43fec8510c204fc1c1edb21d0941c00e9e2c1ce2']:
                return True
            
            else:
                return False

            

                
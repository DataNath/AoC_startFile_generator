import random
import string

if __name__ != '__main__':

    def random_cookie(length: int = 128) -> None:

        set = string.ascii_letters + string.digits

        cookie = ''.join(random.choices(set, k=length))

        return(cookie)
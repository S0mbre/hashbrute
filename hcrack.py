# coding: utf-8

import hashlib
import time
import sys
#from dask.distributed import as_completed, Client as DaskClient

PASSWORDS = '10-million-password-list-top-1000000.txt'
CODEC = 'ascii'
EACHROW = 100

test_hash = '0c78b5c5dad8981f2b68b112cf2fc05f90b590bd'
test_salt = '123==-!(fdf)'
test_pass = 'arina1999'
test_iters = 100000

thash = '4E2Up8pZEiAU6dsYTfFp/02zig8='
tsalt = 'f1AA9ipMNUMngpiAuYzWqg=='
titers = 100000

def gethash(password, salt='', iters=1):
    ghash = None
    for _ in range(iters):
        try:
            ghash = hashlib.sha1((salt + password).encode(CODEC) if ghash is None else ghash.hexdigest().encode(CODEC))  
        except:
            break

    return ghash.hexdigest() if ghash else None

def crack():
    if len(sys.argv) < 2:
        print('USAGE:\npython hcrack.py <HASH> [ <SALT> = "" ] [ <ITERATIONS> = 1 ]')
        return

    myhash = sys.argv[1]
    salt = sys.argv[2] if len(sys.argv) > 2 else ''    
    iters = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    lrow = 0

    start = time.time()

    with open(PASSWORDS, 'r') as filepass:
        for guess in filepass:
            try:
                g = guess.rstrip()
                ghash = None
                for _ in range(iters):
                    try:
                        ghash = hashlib.sha1((salt + g).encode(CODEC) if ghash is None else ghash.hexdigest().encode(CODEC))                        
                       
                    except Exception as err:
                        print(err)
                        break
                
                lrow += 1
                if lrow > 0 and (lrow % EACHROW == 0):
                    print(f'ROWS: {lrow}, ELAPSED: {time.time() - start:.1f} sec.')

                if ghash.hexdigest() == myhash:
                    print(f'FOUND PASS: {g}')
                    break

            except Exception as err:
                print(err)
                break            

    print(f'FINISHED ({time.time() - start:.1f} sec. total time)')

# -------------------------------------------------------------------- #

if __name__ == '__main__':
    crack()
    #print(gethash(test_pass, test_salt, test_iters))
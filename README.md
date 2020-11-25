# Encryptopy
Make your python scripts unreadable by applying a XOR cipher.

The resulting script will ask for the secret-key to decipher before execution.
Arguments will be passed to the original script.

## Usage
```
cat script.py | ./encyptopy.py <secret-key> >script.enc.py
```

## Example
Sample program which prints all arguments:
```
#!/usr/bin/env python3

import sys

class Example(object):
    def run(self):
        for arg in sys.argv:
            print(arg)
if __name__ == '__main__':
    Example().run()
```

Showing the output of sample.py
```
$ ./sample.py arg1 arg2 arg2
./sample.py
arg1
arg2
arg2
```

Ciphering sample.py with the key `123S0M3CR4ZyK3Y546` and running it again
```
$ cat sample.py | ./encryptopy.py 123S0M3CR4ZyK3Y546 > sample.enc.py
$ chmod +x sample.enc.py
$ ./sample.enc.py arg1 arg2 arg3
Enter passphrase: 123S0M3CR4ZyK3Y546
./sample.enc.py
arg1
arg2
arg3
$
```

## But why..?
I was pondering about entering an attack-defend CTF event where valuable
scripts should be protected from fellow competitors of the opposing team.

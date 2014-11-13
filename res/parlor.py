
import os
import ctypes
import subprocess
 
from sock import Sock
from libnum import n2s, s2n
from struct import pack, unpack
 
dll = ctypes.cdll.LoadLibrary("./fast.so")

def extend(data, hash, append, length=16):
    # when we know hash - we use hash_extender for more flexibility
    s = subprocess.check_output(["hash_extender", "-d", data, "-s", hash, "-a", append, "-l", str(length), "-f", "md5"])
    lines = s.splitlines()
    sig = lines[2].strip().split()[-1]
    s = lines[3].strip().split()[-1].decode("hex")
    return s, sig
 
 
p1 = "x\n"
app = "1\n"
 
f = Sock("54.197.195.247 4321", timeout=1000)
f.read_one()
f.send("1\n")
f.read_one()
f.send("100\n")
f.read_one()
f.send("2\n")
f.read_one()
f.send("0\n")
f.read_one()
f.send("3\n")
f.read_one()
f.send(p1)
n = int(f.read_until_re(r"generated (\d+),").group(1))
lowhash = n2s(n).rjust(16, "\x00").encode("hex")[7:]
print lowhash
 
ext1s, ext1sig = extend(p1, "a" * 32, app)
f.send("3\n")
f.read_until("round!")
f.send(ext1s)
n = int(f.read_until_re(r"generated (\d+),").group(1))
lowhash2 = n2s(n).rjust(16, "\x00").encode("hex")[7:]
print lowhash2
 
A, B, C, D = unpack(">4I", lowhash.rjust(32, "0").decode("hex"))
test_hash2 = lowhash2.rjust(32, "0")
 
A = dll.brute(A, B, C, D, test_hash2)
hash1 = pack(">4I", A, B, C, D).encode("hex")
 
 
cash = 100
for i in xrange(100000):
    r = os.urandom(8).encode("hex")
    fake, hash2 = extend(p1, hash1, r)
    num = int(hash2, 16)
    e = 0
    while num % 2 == 0:
        e += 1
        num >>= 1
 
    if e > 100:
        e = 100
 
    if e == 0:
        continue
 
    print i, e, "checking...", "cash", cash
 
    f.send("1\n")
    f.read_one()
    f.send(str(e) + "\n")
    f.read_one()
 
    f.send("2\n")
    f.read_one()
    f.send("%s\n" % cash)
    f.read_one()
 
    f.send("3\n")
    f.read_one()
    f.send(fake)
    print f.read_one()
 
    f.send("4\n")
    print "CASH?", f.read_one()
    if e > 2:
        cash *= 2
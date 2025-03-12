import hashlib

def sha1_for_largefile(filepath, blocksize=8192):
    sha_1 = hashlib.sha1()
    try:
        f = open(filepath, "rb")
    except IOError as e:
        print("file open error", e)
        return
    while True:
        buf = f.read(blocksize)
        if not buf:
            break
        sha_1.update(buf)
    return sha_1.hexdigest()

if __name__ == "__main__":
    print(sha1_for_largefile("shattered-1.pdf"))
    print(sha1_for_largefile("shattered-2.pdf"))
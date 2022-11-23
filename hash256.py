import hashlib as hash

# print("sha3_384, sha1, sha384, shake_256, sha224, sha256, shake_128, sha3_512, sha512_224, sha512, md5, sha3_256, blake2s, sha512_256, sm3, md5-sha1, sha3_224, blake2b")
hashcode = hash.sha256(input('write your phrase here:').encode('utf-8')).hexdigest()
print(f'hash: {hashcode}')

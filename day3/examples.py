# difference between encryption & hashing 
""" 
# Hashing

A one-way function: once data is hashed, you can’t get it back.
Used for verifying data — like checking passwords or file integrity.
Common algorithms: SHA-256, SHA-1, bcrypt.
Always produces a fixed-size output, regardless of input size.
Even a small change in input gives a completely different hash.

# Encryption

A two-way process: data is scrambled using a key and can be unscrambled (decrypted) with that key.
Used when you need to protect data but also read it later — like messages, files, credentials.
The encrypted output can vary in size depending on the input and encryption method.

"""

# import hashlib

# text = b"hello123"

# hashed = hashlib.sha256(text).hexdigest()

# print("Hashed:", hashed)

#-------------------------------------
""" 
bcrypt is designed to make attacks much harder.

bcrypt.gensalt() generates a random salt each time.
hashpw() returns the hashed version of the password.
Output is a byte string, not regular text.
"""
import bcrypt

# Original password (must be bytes)
password = b"my_secret_password"

# Generate a salted hash
hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

print("Hashed password using bcrypt:", hashed_password)


## Try to login 
login_password = b"my_secret_password"
# Compare with stored hash
if bcrypt.checkpw(login_password, hashed_password):
    print("Password is correct")
else:
    print("Password is incorrect")

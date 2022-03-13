from email import message
import hashlib

message= hashlib.sha256()
message.update(b'shayd')

print(message.hexdigest())
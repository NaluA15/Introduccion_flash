from email import message
import hashlib

message= hashlib.sha256()
message.update(b'nalu')

print(message.hexdigest())
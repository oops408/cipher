from Crypto.Util.number import bytes_to_long, long_to_bytes, getPrime, inverse

# Generate the public and private keys
p = 7929784484601571438556962301091075858855221082408119915984427404222889089508123170481994187868730450486555622247851839792346424851012282168291892181358521
q = 12702763305095394050797091920448801436034799490575134387288377684776621453859015314357141487880257024105303175708994671153726639639927719205169291350500497
N = p * q
totient = (p - 1) * (q - 1)
e = 88
d = inverse(e, totient)

# Define the message to be encrypted
message = b"Hello, world!"

# Convert the message to an integer using bytes_to_long
m = bytes_to_long(message)

# Encrypt the message using RSA
ciphertext = pow(m, e, N)

# Print the ciphertext
print(ciphertext)

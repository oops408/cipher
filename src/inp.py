from Crypto.Util.number import bytes_to_long, long_to_bytes, getPrime, inverse
 
p = 7929784484601571438556962301091075858855221082408119915984427404222889089508123170481994187868730450486555622247851839792346424851012282168291892181358521
q = 12702763305095394050797091920448801436034799490575134387288377684776621453859015314357141487880257024105303175708994671153726639639927719205169291350500497
N = p * q
totient = (p - 1) * (q - 1)
e = 88
d = inverse(e, totient)
 
ciphertext = 20105686147991941369013766839987314637794741418836048390207432144211428603343545341113483780787575674844374295850418357112562002976911845044695395223651780902249997312992203320108137212557982436701392702319743854706572541120465765715495541599418085021051751662008710898889028243528751455361486108662629587591
 
plaintext = pow(ciphertext, d, N)
plaintext = long_to_bytes(plaintext)
 
print(plaintext)

<<<<<<< HEAD
import sys

les = 'abcdefghlmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890ԱԲԳԴԵԶԷԸԹԺԻԼԽԾԿՀՁՂՃՄՅՆՇՈՉՊՋՌՍՎՏՐՑՈՒՓՔՕՖաբգդեզէըթժիլխծկհձղճմյնշոչփջռսվտրցուփքևօֆ,․/՛~#!$%^&*)( ><;:][}{'
file = open(sys.argv[1], 'r', newline='\n')
txt = file.read()
print(txt[:1900])

for ch in les:
=======
import sys

les = 'abcdefghlmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890ԱԲԳԴԵԶԷԸԹԺԻԼԽԾԿՀՁՂՃՄՅՆՇՈՉՊՋՌՍՎՏՐՑՈՒՓՔՕՖաբգդեզէըթժիլխծկհձղճմյնշոչփջռսվտրցուփքևօֆ,․/՛~#!$%^&*)( ><;:][}{'
file = open(sys.argv[1], 'r', newline='\n')
txt = file.read()
print(txt[:1900])

for ch in les:
>>>>>>> 013eb88b94a1b7b8b17f5fc86c31cf0de2c97b8f
    print("%s : %s" % (ch, txt.count(ch)))
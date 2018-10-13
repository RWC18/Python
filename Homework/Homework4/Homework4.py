import sys

les = 'abcdefghlmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890ԱԲԳԴԵԶԷԸԹԺԻԼԽԾԿՀՁՂՃՄՅՆՇՈՉՊՋՌՍՎՏՐՑՈՒՓՔՕՖաբգդեզէըթժիլխծկհձղճմյնշոչփջռսվտրցուփքևօֆ,․/՛~#!$%^&*)( ><;:][}{'
file = open(sys.argv[1], 'r', newline='\n')
txt = file.read()
print(txt[:1900])

for ch in les:
    print("%s : %s" % (ch, txt.count(ch)))
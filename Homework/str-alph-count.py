les = 'abcdefghlmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890ԱԲԳԴԵԶԷԸԹԺԻԼԽԾԿՀՁՂՃՄՅՆՇՈՉՊՋՌՍՎՏՐՑՈՒՓՔՕՖաբգդեզէըթժիլխծկհձղճմյնշոչփջռսվտրցուփքևօֆ,․/՛~#!$%^&*)( ><;:][}{'
st = str(input())

for ch in les:
    print("%s : %s" % (ch, st.count(ch)))
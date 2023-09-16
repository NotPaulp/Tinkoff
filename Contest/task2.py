n,k=map(int,input().split())
p=input()
symbols={}
for symbol in p:
    symbols[symbol]=symbols.get(symbol, 0)+1
symbols=sorted(symbols.items(),key=lambda x:x[1])
i=0
answer=len(symbols)
while k>0 and i<len(symbols):
    if k>=symbols[i][1]:
        k-=symbols[i][1]
        answer-=1
        i+=1
    else:
        break
print(answer)
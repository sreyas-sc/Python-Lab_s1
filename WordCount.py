text=input("Enter the Word: ");
wrdlist=text.split();
occurence_str='';
for x in wrdlist:
    _occ=0;
    for y in wrdlist:
        if x==y:
            _occ+=1;
    occurence_str+="Word: '"+str(x)+"' occurrence: "+str(_occ)+"\n";
print(occurence_str)
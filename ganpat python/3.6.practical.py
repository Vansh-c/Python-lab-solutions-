# Go to String below and if the length of a word is even print "even!".

st='I love doing python programming in spyder'

l = st.split(' ') 

for element in l:
    if(len(element)!=0):
        if(len(element)%2==0):
            print("even!") 

            
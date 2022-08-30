# framework={"name":"django","rating":4,"language":"python"}
# if "rating" in framework:
#     framework["framework"]+=1
# else:
#     framework["rating"]=1
#
# framework["architecture"]="mvt"
# print(framework)

# text="hello,hai,hello,hai,hello"
# words=text.split(",")
# word_count={}
#
# for w in words:
#     if w in word_count:
#         word_count[w]+=1
#     else:
#         word_count[w]=1
# print(word_count)

text="hello,hai,hello,hai,hello,hi,hlo,hi,hi,hi"
words=text.split(",")
word_count={}

for w in words:
    if w in word_count:
        word_count[w]+=1
    else:
        word_count[w]=1
print(word_count)
print(max(word_count,key=lambda k:word_count.get(k)))





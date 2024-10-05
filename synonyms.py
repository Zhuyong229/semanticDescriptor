'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Nov. 18, 2022.
'''

import math


def norm(vec):
    '''Return the norm of a vector stored as a dictionary, as 
    described in the handout for Project 3.
    '''
    
    sum_of_squares = 0.0  
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    
    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    #print(vec1,vec2)
    numerator = 0
    for k1 in vec1:
        for k2 in vec2:
            if k1 == k2:
                numerator += vec1[k1]*vec2[k2]
    
    denominator = norm(vec1) * norm(vec2)
    return float(numerator/denominator)
    
    

def build_semantic_descriptors(sentences):
    # put in all the keys
    dic = {}
    #for i in sentences:
        #for k in range (len(i)):
            #if i[k] not in dic:
                #dic[i[k]] == {}
    # count numbers
    #for w in dic:
        #for a in sentences:
            #if w in a:
                #for b in range (len(a)):
                    #if a[b] not in dic[i[k]] and a[b] != w:
                        #dic[i[k]][a[b]] = 0
                    #elif a[b] != w:
                        #dic[i[k]][a[b]] += 1
                        #break

    for a in sentences:
        for b in range(len(a)):
            if a[b] not in dic:
                dic[a[b]] = {}
            for c in range (b+1, len(a)):
                if a[c] not in dic:
                    dic[a[c]] = {}

                if a[c] in dic[a[b]]:
                    dic[a[b]][a[c]] += 1
                else:
                    dic[a[b]][a[c]] = 1
                if a[b] in dic[a[c]]:
                    dic[a[c]][a[b]] += 1
                else:
                    dic[a[c]][a[b]] = 1

    return dic


def build_semantic_descriptors_from_files(filenames):
    tot_dic = {}
    tot_sentences = []
    for file in filenames:
        with open(file, "r", encoding="utf-8") as sentences:
            sentences = sentences.read()
            sentences = sentences.replace("!",".").replace("?",".")
            sentences = sentences.replace("$"," ").replace("&"," ").replace("*"," ").replace("#"," ").replace("/"," ").replace("_"," ").replace(","," ").replace("-"," ").replace("--"," ").replace(":"," ").replace(";"," ").replace("\n"," ").replace("("," ").replace(")"," ").replace("{"," ").replace("}"," ").replace("|"," ").replace("<"," ").replace(">"," ")
            sentences = sentences.lower()
            sentences = sentences.split(".")
            sentences.remove(sentences[len(sentences)-1])
            for sentence in sentences:
                tot_sentences.append(sentence.split())
                
            
    tot_dic = build_semantic_descriptors(tot_sentences)
    #print(tot_sentences)
    return tot_dic

def similarity_fn(vec1,vec2):
    return cosine_similarity(vec1,vec2)

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    max_similarity = -1
    for w in range (len(choices)):
        if choices[w] in semantic_descriptors and word in semantic_descriptors:
            similarity = similarity_fn(semantic_descriptors[word],semantic_descriptors[choices[w]])
            #print(similarity)
            if similarity > max_similarity:
                max_similarity = similarity
                index = w
               
    if max_similarity == -1:
        return choices[0]
    else:
        return choices[index]

def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    correct_number = 0
    with open(filename,"r",encoding="utf-8") as lines:
        lines = lines.read()
        lines = lines.split("\n")
        for line in lines:
            l = line.split()
            choices = l[2:]
            if l[1] == most_similar_word(l[0], choices, semantic_descriptors, similarity_fn):
                #print(most_similar_word(line[0], line[2:], semantic_descriptors, similarity_fn))
                correct_number += 1
            #else:
                #print(most_similar_word(line[0], line[2:], semantic_descriptors, similarity_fn))
    return float((correct_number/len(lines))*100)

filenames=["D:/Golden Wind/python/synonyms/War&Peace.txt","D:/Golden Wind/python/synonyms/Swann'sWay.txt"]
semantic_descriptors = build_semantic_descriptors_from_files(filenames)
res = run_similarity_test("D:/Golden Wind/python/synonyms/test.txt", semantic_descriptors, similarity_fn)  
print(res)

#"D:/Golden Wind/python/synonyms/Swann'sWay.txt"
#"D:/Golden Wind/python/synonyms/War&Peace.txt"
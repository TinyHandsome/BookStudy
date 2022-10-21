def loadDataSet():
    postingList = [
        ['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
        ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
        ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
        ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
        ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
        ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']
    ]

    # 1 侮辱性文字，0 正常言论
    classVec = [0, 1, 0, 1, 0, 1]
    return postingList, classVec


def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        # 创建两个集合的并集，目的是为了获取 所有的数据集中涉及到的单词
        vocabSet = vocabSet | set(document)
    return list(vocabSet)


def setOfWords2Vec(vocabList, inputSet):
    # 创建一个其中所含元素都为0的向量
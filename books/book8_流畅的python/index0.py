"""创建一个从单词到其出现情况的映射"""

import sys
import re
from collections import defaultdict

WORD_RE = re.compile(r'\w+')

# index = {}
index = defaultdict(list)
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            
            ''' 这其实是一种很不好的实现，这样写只是为了证明论点
            occurrences = index.get(word, [])
            occurrences.append(location)
            index[word] = occurrences
            '''
            
            ''' 下面是好的实现，用到了setdefault函数
            index.setdefault(word, []).append(location)
            '''
            
            ''' 通过collections.defaultdict实现，取得key没有的时候，新建这个key，并赋予默认值'''
            index[word].append(location)
            
# 以字母顺序打印出结果
for word in sorted(index, key=str.upper):
    print(word, index[word])
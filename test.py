# 原文的断句有问题，比如：<div class="entry">Get me in ten minutes, Ray.<br><br>Boss.<br><br>- Bobby.<br>- Boss?<br><br>I'll have a pint<br>and a pickled egg.<br><br>Coming straight up.<br><br>If you wish to be<br>the king of the jungle,<br><br>it's not enough<br>to act like a king. 
# 我希望写入到md文件中的时候，可以按照一句话来分割，比如I'll have a pint and a pickled egg. 这是完整的一句话，不要从pint后面换行
import re

# 原始文本
text = '<div class="entry">Get me in ten minutes, Ray.<br><br>Boss.<br><br>- Bobby.<br>- Boss?<br><br>I\'ll have a pint<br>and a pickled egg.<br><br>Coming straight up.<br><br>If you wish to be<br>the king of the jungle,<br><br>it\'s not enough<br>to act like a king.'

# 去除 <br> 标签
text = re.sub(r'<br>', '', text)

# 使用正则表达式将文本按照句子分割
sentences = re.findall(r'[^.!?]+[.!?]', text)

# 写入到 Markdown 文件
with open('test.md', 'w') as file:
    for sentence in sentences:
        file.write(sentence.strip() + '\n\n')

# TODO： enough 后面没有加空格就直接拼接上了to; 可见处理的时候要加上空格
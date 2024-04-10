import requests
from bs4 import BeautifulSoup
import re

def get_movie_scripts(url):
    page = 1
    content = ""
    while True: 
        print(f"current page: {page}")
        page_url = f"{url}?page={page}"
        response = requests.get(page_url)
        html_content = response.text

        soup = BeautifulSoup(html_content, 'html.parser')

        # 使用BeautifulSoup选择器找到每个页面中的entry类别的div标签，提取内容
        movie_scripts = soup.find('div', class_='entry')
        if movie_scripts.text == "":
            print("scipt scapering is over")
            break

        content += movie_scripts.get_text(separator='\n\n')
        content += "\n\n---\n\n"

        page += 1
       # 清空已存在的Markdown文件
    with open('movie_scripts.md', 'w') as file:
        file.write('')

    # 将提取到的电影剧本信息一次性保存到Markdown文件
    with open('movie_scripts.md', 'a') as file:
        file.write(content)

# 调用获取电影剧本的函数
url = "https://www.taicishe.com/movie-the-gentlemen-2019"
get_movie_scripts(url)
print("done")
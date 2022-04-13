import urllib.request
from bs4 import BeautifulSoup

def getPageNum():
    print("크롤링 : 문서 수 = 페이지 수 x 10")
    print("최대 페이지 수 : ")
    max_page = int(input())
    return max_page

def getSearch():
    print("검색어 : ")
    search = input()
    search = "+".join(search.split())
    return search

def getURL(page, search):
    url = "https://scholar.google.com/scholar"
    get = "?start=" + str(10 * page)
    query = "&q=" + search + "&hl=ko&as_sdt=0,5"
    
    url = url + get + query 
    return url 

def crawl(url):
    header = {"User-Agent": "Mozilla/5.0"} # 크롤링 그냥 하면 막혀있어서 추가
    page = urllib.request.Request(url, headers=header)
    html = urllib.request.urlopen(page)
    soup = BeautifulSoup(html, 'html.parser')
    informations = soup.select('div.gs_ri')

    papers = []
    for info in informations:
        title = info.find('h3','gs_rt') # 제목
        sub_info = info.find('div','gs_fl') # 인용수 찾기용
        sub_info = sub_info.get_text()
        cnt = 0 # 인용수
        element = [title.get_text(), cnt]
        # 인용수 구하기
        for idx in range(len(sub_info)):
            if sub_info[idx] == '회':
                last = idx 
                start = idx  
                while True:
                    if sub_info[idx] == ' ':
                        start = idx + 1 
                        break
                    idx -= 1    
                element[1] = int(sub_info[start:last]) 
                break 
        papers.append(element)
    return papers

def sortByCitiation(papers):
    return sorted(papers, key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    
    max_page = getPageNum()
    search = getSearch()
    result = []

    for page in range(max_page):
        url = getURL(page,search)
        papers = crawl(url)
        for paper in papers:
            result.append(paper) 
            # 앗 잘못 짰다.... (crawl 함수)
            # 페이지 별로 말고 하나 씩 넣을 걸
            # 괜히 한 번 더 복사시켜야 하네....
            # 논문 비교할 게 몇 개 안 되니 일단 이렇게....

    print("===결과===")    
    result = sortByCitiation(result)
    for element in result:
        print(element)
    

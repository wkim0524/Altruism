####Cine 21 평론 게시판을 예시로 작성####

def crawl():  # crawl 함수 정의
    # 필요모듈
    import selenium
    from selenium import webdriver
    from bs4 import BeautifulSoup

    x = 0
    while x < 40:  # 조건문 시작. 필요에 따라 수정
        x = x + 1  # x 값 정의
        z = str(x)  # x 값 스트링으로 변환. 밑의 주소에 입력시 int 는 입력이 안되어 str로 변환

        # 텍스트 리스트 만들기
        texts = []

        html = 'http://www.cine21.com/news/list/?idx=6&p='  # 소스 페이지
        driver = webdriver.Chrome('/Users/gim-woncheol/chromedriver')  # 드라이버 실행. 크롬 사용. 다른 드라이버 사용 가능

        driver.get(html + z)  # html 과 z 를 조합한 주소로 크롬 실행

        # 상위 엘리먼트 객체 불러오기
        results = driver.find_elements_by_tag_name('li')  # li 태그가 붙은 부위 results 로 묶음

        links = []  # 새창에 띄울 링크 리스트 생성

        # li 객체에서 a 태그가 붙은 객체 중, href 를 포함하는 객체를 포함하기
        for i in range(18, 30):  # li 태그 객체중 19번 부터 31번 까지만 필요로 하기 떄문에 range 설정
            link = results[i].find_element_by_tag_name(
                "a")  # results, 즉 li 태그가 붙은 19~31 번 객체로 부터, a 태그가 붙은 위치 link 로 정의
            links.append(link.get_attribute("href"))  # a 태그 가 붙은 링크가 포함하고 있음 href 항목을 links 리스트에 저장

            # 새탭에 전부 출력
        for link in links:  # links 리스트의 모든 link 를
            driver.execute_script('window.open("' + link + '")')  # 새로운 창에서 실행

        driver.switch_to.window(driver.window_handles[1])  # 창 변경
        # 크롤링
        html = driver.page_source  # 창페이지 소스 긁어오기
        soup = BeautifulSoup(html, 'html.parser')  # 소스 파싱
        body = soup.select('p')  # 범위 셀렉트
        texts.append(body)  # 리스트에 추출 텍스트 저장

        ###
        driver.switch_to.window(driver.window_handles[2])  # 창 변경
        # 크롤링
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        body = soup.select('p')
        texts.append(body)

        ###
        driver.switch_to.window(driver.window_handles[3])  # 창 변경
        # 크롤링
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        body = soup.select('p')
        texts.append(body)

        ###
        driver.switch_to.window(driver.window_handles[4])  # 창 변경
        # 크롤링
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        body = soup.select('p')
        texts.append(body)

        ###
        driver.switch_to.window(driver.window_handles[5])  # 창 변경
        # 크롤링
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        body = soup.select('p')
        texts.append(body)

        ###
        driver.switch_to.window(driver.window_handles[6])  # 창 변경
        # 크롤링
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        body = soup.select('p')
        texts.append(body)

        ###
        driver.switch_to.window(driver.window_handles[7])  # 창 변경
        # 크롤링
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        body = soup.select('p')
        texts.append(body)

        ###
        driver.switch_to.window(driver.window_handles[9])  # 창 변경
        # 크롤링
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        body = soup.select('p')
        texts.append(body)

        ###
        driver.switch_to.window(driver.window_handles[10])  # 창 변경
        # 크롤링
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        body = soup.select('p')
        texts.append(body)

        ###
        driver.switch_to.window(driver.window_handles[11])  # 창 변경
        # 크롤링
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        body = soup.select('p')
        texts.append(body)

        ###
        driver.switch_to.window(driver.window_handles[12])  # 창 변경
        # 크롤링
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        body = soup.select('p')
        texts.append(body)

        driver.quit()  # 드라이버 종료

        if z is '0':  # 첫페이지 실행시
            f = open("testing123.txt", "w+")  # 파일생성 및 쓰기
            print(texts, file=f)  # texts 에 저장된 리스트 파일에 쓰기
        else:  # 첫페이지 후에 오픈되는 페이지
            f = open("testing123.txt", "a+")  # 기존 파일 열고 추가 하기
            print(texts, file=f)  # text 에 저장된 리스트 파일에 추가

        # while 문 조건 제한 부분. 필요에 따라 수정 가능
        if x < 5:
            continue
        if x > 6:
            break

crawl() #함수 실행
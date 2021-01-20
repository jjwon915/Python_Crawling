# Python_Crawling

1. 크롤링할 키워드와 Page 수를 입력하고 제출 버튼을 클릭하면 daum의 뉴스 기사 목록들을 page 수 만큼 크롤링해 result.html에서 출력한다. 또한 크롤링한 결과들을 엑셀파일 형태로 저장할 수 있다.

2. 크롤링할 키워드를 입력 후 Naver Shopping Crawling selenium을 클릭하면 네이버 쇼핑에서 입력된 상품의 목록의 제목, 사진들을 크롤링해오고, 백화점/홈쇼핑 탭의 상품의 목록의 제목, 사진들을 크롤링해온다.

[app.py]
- keyword와 page 수를 입력받아 daum에서 뉴스를 검색한 결과를 result.html에 출력한다.

- daum_list에 크롤링한 결과를 append하고 result.html에 daum_list를 result.html로 넘겨 출력한다.

- daum에서 검색하면 a 태그 안의 f_likn_b 클래스에 뉴스 기사의 제목이 담겨있다.

 - naver shopping 에서 입력된 단어로 검색해 상품의 이름과 이미지를 크롤링해 search_list와 search_list_src에 append해 shopping.html로 넘겨 shopping.html에서 크롤링된 결과를 이미지와 함께 출력한다.

- 크롤링하기 전 페이지가 모두 스크롤 된 후 하기 위한 코드를 추가했다.

- 강의의 내용과 다르게 naver shopping의 html 코드가 변경되어 바뀐 내용으로 코드를 수정했다. 상품의 이름들이 div태그로 감싸져 반복되는 구조를 가졌기 때문에 soup.select안의 내용을 저런식으로 써주었다. 또한 이미지의 src도 강의 내용의 코드에는 class이름이 써있지만 class가 없어졌기 때문에 i.find("img")["src"]로 변경해주었다. 

- 전체 탭에서 크롤링 후 백화점/홈쇼핑 탭에서도 마찬가지로 크롤링 하기 위해 백화점/홈쇼핑 탭이 자동클릭되게 했다. 백화점/홈쇼핑 탭도 강의 내용과 달리 naver shopping의 html 코드가 변경되어 find_element_by_css_selector를 사용하여 써주었다. 

[index.html]
- 실행했을 때  127.0.0.1:5000에 출력되는 html 코드.

- 부트스트랩의 코드를 활용했고 크롤링할 키워드와 페이지 수를 입력할 수 있다. 

[result.html과 shopping.html]
- result.html에서는 daum 뉴스에서 크롤링된 결과를 출력하고, 크롤링한 결과가 저장된 엑셀 파일을 저장할 수 있다. 

- shopping.html도 비슷한 코드를 가지고 있으며 이미지 파일과 함께 출력하기 위해 for 문 안에 <li><img src={{ search_list_src[i] }}></li> 도 함께 작성해주었다. 

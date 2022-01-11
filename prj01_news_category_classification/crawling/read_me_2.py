# news_category_classification_01_2_crawling.py 에서 culture / Economic / IT / Politics / Social / World 6개에 있는 뉴스제목,헤드라인기사를 크클링 해와서
# team_crawling 폴더에 모두 저장했다
# news_category_classification_01_3_concat.py 에서 team_crawling에 저장한 모든 csv파일을 concat 했다.
# news_category_classification_02_preprocessing.py 에서 crawling/stopwords.csv 파일을 이용하여 불용어를 제거하였다.
# news_category_classification_03_learning.py에서 모델링을 하였다.
# news_category_classification_04_model_predict.py 위에서 만들어진 모델로 새로운 기사를 예측시켰다.
# 새로운 기사를 예측시키는 크롤링코드는 news_category_classification_01_1_crawling.py 이다
# crawling/naver_headline_news20220105.csv 으로 22년1월5일 당일, 6개의 카테고리 당일 기사를 모두 각각 예측시켜보았다.
# 예측은 새로운 모델링 환경에서 하고
# 예측 결과는 이러이러하다
# 사용한 환경은 requirements에 따로 저장하여두었다.
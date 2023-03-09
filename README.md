## JjinddaCheck - 찐따 구별 애플리케이션 개발계획서 (예시)

2023년 3월 4일 작성
Bill Jebs

### <개발취지>
1. 익명성이 보장되는 인터넷에서 찐따들의 무분별한 무지성 댓글들로 인해 SNS환경이 매우 불순함
2. 사회성이 결여된 사람들의 이용량이 상대적으로 많기에 찐따 육성이 활발하고 비례적으로 악플로 인한 피해자가 만연한 실정임
3. 이들이 결국 노동, 출산율 저하의 원인이 되고 사회와 더욱 격리되게 되는 현상 발생
4. 정부에서 실행하는 노동활동 지원 프로그램 등, 간접적으로 그러한 찐따활동을 줄이기에는 역부족 -> 따라서 직접적으로 찐따들에게 본인이 찐따라는 강한 충격을 주게 하여 스스로를 깨닫게 하고 키보드에서 손을 떼도록 하기 위함

### <기대효과>
1. 인터넷 환경 개선 
2. 무직자들의 노동 촉진 ~~혹시 일하는 사람중에 최창민씨 계시나요~~
3. 븅신들의 깨달음 ~~빙신같은 lap puddle~~

### <개발안>
1. 빅데이터 기반 A.I.(인공지능) 시스템 구축
            - SNS, 뉴스기사, 온라인 커뮤니티 사이트 등의 인터넷 댓글 대량수집 후 입력
            - 좋은 반응을 얻은 댓글과 그렇지 않은 댓글 두 가지로 분류(추후 필요 카테고리 추가)
            - AI 반복학습
            - 찐따의 무지성댓글에 대한 반박자료로써 사용

2. 공유기능 탑재
            - 분석결과를 다양한 플랫폼으로 쉽고 빠르게 공유
            - 온라인 댓글 논쟁의 흐름이 깨지지 않도록 자연스럽게 녹아드는 것이 가능
            - 해당 논쟁에 대한 타사이트로의 공유 증가 -> 찐따의 반박 원천봉쇄와 기권유도

### <인공지능 학습>
1. 데이터 주입 기준 
    - 0점: 찐따 (김도건, 최유백, 서종원, 이동훈)
    - 0.5점: 평민 (안성현, 최부건, 김학일)
    - 1점: 인싸 (김진성, 김소혜, 김은수, 서동연)
2. 인공지능 평가 기준
    - 문맥에 따라 인싸가 썻는지 찐따가 쓴 단어인지 확률 계산 -> 평균값 계산
    - 인지하지 못하는 단어가 나왔을때 찐따 단어 (0점) 로 계산
## Tech Stack
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![KakaoTalk](https://img.shields.io/badge/kakaotalk-ffcd00.svg?style=for-the-badge&logo=kakaotalk&logoColor=000000)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)

### <홍보안>
1. 인스타그램 릴스, 유튜브 쇼츠 등의 비교적 쉽게 노출될 수 있는 플랫폼으로 바이럴 마케팅 시전
2. 공유 多
3. 빅데이터의 신뢰성으로 인한 이용량 증가 -> 반절대적 온라인 대화수단으로 급부상 가능성 ⤴

### <예상문제점>
1. 개인의견피력의 자유를 저해한다는 점에서 논란 가능성
            - 자유에는 책임이 따른다는 말로 반박가능
            - 어차피 익명성은 보장되기에 개인신상이 털릴 위험 x
2. 데이터수집력의 한계
            - 개발자의 역량에 달림 ~~ㅈㄴ 넣으면돼 이새기야~~

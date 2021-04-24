## 알고리즘 연습장

### git 초기 업로드 방법

- git init 
- git remote add origin https://github.com/wonpaka/Algorithm.git
  - 원격저장소를 연결 한다는 의미이다.
- git remote -v
- git add .
- git commit -m "first commit"
  - 메시지와 함께 commit을 진행하겠다는 말

####    ( 만약 여기서 Author identity unknown 이 나온다면, )

- git config --global user.email "you@example.com"
- git config --global user.name "Your Name"

- git commit -m "first commit"
- git push -u origin main



### git 추가 업로드 방법

- git add .
- git commit -m "second commit"
- git push -u origin main



### 게시된 파일 원격으로 내려받는법

- git clone https://github.com/wonpaka/Algorithm.git
- git pull origin master


### 다음과 같은 에러 발생 시 
- fatal: not a git repository (or any of the parent directories): .git
  - 현재 폴더에 git에 대한 정보를 담은 파일이 없기 때문에 발생하는 에러.
  - 업로드시 위의 문제가 발생하면, $ git init 수행후 다시 $ git remote add 명령어 실행 
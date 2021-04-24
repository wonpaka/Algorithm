## 알고리즘 연습장

### git 초기 업로드 방법

- git init 
- git remote add origin https://github.com/wonpaka/Algorithm.git
- git remote -v
- git add .
- git commit -m "first commit"

##### 만약 여기서 Author identity unknown 이 나온다면,

- git config --global user.email "you@example.com"
- git config --global user.name "Your Name"

- git commit -m "first commit"
- git push -u origin main

### git 추가 업로드 방법

- git add .
- git commit -m "second commit"
- git push -u origin main
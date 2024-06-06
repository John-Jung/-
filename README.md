<div align="center">
  <h1>보안 주제 기반 학술 사이트 Security arXiv</h1>
  
  <h3>"SK 쉴더스 루키스에서 보안 공부를 하는 루키들을 위한!"</h3>
  

</div>
</br>
</br>

# 목차

1. [프로젝트 소개](#프로젝트-소개)
2. [개발 기간](#개발-기간)
3. [팀 멤버](#팀-멤버)
4. [주요기능 소개](#주요기능-소개)
   - [자기소개서 가이드](#자기소개서-가이드)
   - [자기소개서 첨삭](#자기소개서-첨삭)
   - [글 리스트 조회](#글-리스트-조회)
   - [상세 페이지 기능](#상세-페이지-기능)
   - [마이페이지](#마이페이지)
   - [어드민 유저관리](#어드민-유저관리)
   - [어드민 유저통계](#어드민-유저통계)
   - [랜딩페이지](#랜딩페이지)
5. [프로젝트 아키텍처](#프로젝트-아키텍처)
6. [개발 환경](#개발-환경)
7. [레포지토리](#레포지토리)
8. [트러블 슈팅 & 기술적 경험](#트러블-슈팅--기술적-경험)
   - [김상휘 AI](#김상휘)
   - [박민준 FE](#박민준)
   - [신아진 BE](#신아진)
   - [박연경 BE](#박연경)
   - [안은비 BE](#안은비)


## 💻프로젝트 소개

<p>SK 쉴더스 루키즈 19기 1차 모듈프로젝트입니다.</p>
<p>1달동안 배운 파이썬, Django, 애플리케이션 보안, 시스템/네트워크 보안 기술, 클라우드 보안 기술과정을 적용</p>
<p>SK 쉴더스취약점점검보고서 클라우드 보안 가이드, KISA 파이썬 시큐어코딩 가이드를 반영하여 개발</p>


## ⏲개발 기간

2024.04.11 - 2024.04.24

## 👪팀 멤버


|    정성욱   |    김현진   |    서미란   |    정연서    |    홍준혁    |
|:------------:|:------------:|:------------:|:------------:|:------------:|
| 팀장 / Backend / 취약점 진단 | 팀원 / AWS 구축 / 배 | 팀원 / Backend / 취약점 진단 | 팀원 / AWS 구축 /Frontend | 팀원 / Frontend / 취약점 진단 |


## 📷주요기능 소개

### [메인 페이지]
![SK쉴더스 루키즈 8조 프로젝트 수행결과보고서_page-0022](https://github.com/John-Jung/security_arxiv/assets/45717075/64458fa0-9382-4242-aa5c-0335a82bf266)

### [로그인 페이지]
![SK쉴더스 루키즈 8조 프로젝트 수행결과보고서_page-0023](https://github.com/John-Jung/security_arxiv/assets/45717075/92a5a9a7-6fd5-4f5c-ba3b-28c29ff63ed9)

### [메뉴바]
![SK쉴더스 루키즈 8조 프로젝트 수행결과보고서_page-0024](https://github.com/John-Jung/security_arxiv/assets/45717075/4d9ff57d-aaf0-40a0-9d7a-376ab6416b4b)

### [게시판 목록]
![SK쉴더스 루키즈 8조 프로젝트 수행결과보고서_page-0025](https://github.com/John-Jung/security_arxiv/assets/45717075/d8b0b2ad-46bf-4101-8600-6d5b5ef75cb0)

### [게시판 생성]
![SK쉴더스 루키즈 8조 프로젝트 수행결과보고서_page-0026](https://github.com/John-Jung/security_arxiv/assets/45717075/d8ffe88e-baf2-4b9d-be55-7b398a071446)

### [게시판 상세 1]
![SK쉴더스 루키즈 8조 프로젝트 수행결과보고서_page-0027](https://github.com/John-Jung/security_arxiv/assets/45717075/6d182076-da47-410e-b896-2e285506e3c5)

### [게시판 상세 2]
![SK쉴더스 루키즈 8조 프로젝트 수행결과보고서_page-0028](https://github.com/John-Jung/security_arxiv/assets/45717075/c93fb0e6-0858-4f29-92e7-a90361e51464)

### [게시판 수정]
![SK쉴더스 루키즈 8조 프로젝트 수행결과보고서_page-0029](https://github.com/John-Jung/security_arxiv/assets/45717075/979f9887-21c5-415b-a75b-971358242393)

### [내 정보]
![SK쉴더스 루키즈 8조 프로젝트 수행결과보고서_page-0030](https://github.com/John-Jung/security_arxiv/assets/45717075/bbb0289e-9f26-4848-8172-09a6ff718f8e)

### [내 정보 수정]
![SK쉴더스 루키즈 8조 프로젝트 수행결과보고서_page-0031](https://github.com/John-Jung/security_arxiv/assets/45717075/dde2ca37-dc9a-496e-9fa7-9b1dbc8c0d24)


### [비밀번호 수정]
![SK쉴더스 루키즈 8조 프로젝트 수행결과보고서_page-0032](https://github.com/John-Jung/security_arxiv/assets/45717075/2e51b870-36a4-4138-a896-9cefd88ea6c6)



## 🏛프로젝트 아키텍처
  ![reditor_architecture2](https://github.com/MinjoonHK/resumeEditorFrontend/assets/108560916/9e4adc18-e1b2-46b6-b1a2-1b0b7735ff50)

## ⚙개발 환경

<ul>
  <li>Front-end: React.js@18.2.0, TypeScript, Redux Toolkit@9.1.0, Antd</li>
  <li>Back-end: Spring Boot, Spring Security, Hibernate</li>
  <li>AI: ChatGPT API, Qdrant, Flask</li>
  <li>Env: Node.js@v18.17.0, JAVA 17</li>
  <li>Build: Vite, Gradle</li>
  <li>IDE: VScode, IntelliJ</li>
  <li>DB: MySQL</li>
  <li>CI/CD: Github Actions</li>
  <li>Deploy: Vercel, CloudType</li>
  <li>Collaboration: Github, Slack, Notion, Swagger@2.0.2, Figjam, Kakao Oven </li>
</ul>


## 🏠레포지토리

<a href="https://github.com/MinjoonHK/resumeEditorFrontend">프론트엔드 레포지토리</a><br/>
<a href="https://github.com/JavaBackEnd21st/resumeEditorBackend">백엔드 레포지토리</a><br/>
<a href="https://github.com/JavaBackEnd21st/resume_gpt_qdrant">AI 레포지토리</a><br/>

## 🛠트러블 슈팅 & 기술적 경험

### 김상휘


### 박민준
<ul>
  
  <li><a href="https://github.com/MinjoonHK/resumeEditorFrontend/wiki/FE-%E2%80%90-UX-%EA%B0%9C%EC%84%A0">FE-UX개선</a></li>
  <li><a href="https://github.com/MinjoonHK/resumeEditorFrontend/wiki/FE-%E2%80%90-%EC%84%B1%EB%8A%A5-%EC%B5%9C%EC%A0%81%ED%99%94%EC%97%90-%EB%8C%80%ED%95%B4">FE-성능 최적화</li>
</ul>

### 신아진


### 박연경


### 안은비

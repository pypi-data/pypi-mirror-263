# pollux-llm
pollux-llm library


### PyPI에 배포하기 ###
**참고문헌**

[Publishing package distribution releases using GitHub Actions CI/CD workflows](https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/)

[Python 빌드 및 테스트 ](https://docs.github.com/ko/enterprise-cloud@latest/actions/automating-builds-and-tests/building-and-testing-python)

다음의 명령어를 이용하면 Build와 동시에 PyPI에 패키지가 배포됩니다.
|명령|명령문|설명|
|---|---|---|
|local Tag 추가|git tag 0.0.1|local의 git tag를 0.0.1 버전으로 추가|
|local Tag 삭제|git tag -d 0.0.1|local git tag 0.0.1 버전을 삭제|
|Remote Tag 추가|git push origin 0.0.1|remote의 git tag를 0.0.1로 추가|
|Remote Tag 삭제|git push --delete orgin 0.0.1|remote git tag 0.0.1 버전을 삭제|
 
```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```
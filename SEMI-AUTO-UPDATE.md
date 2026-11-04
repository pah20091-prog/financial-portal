# 방식 B: 통합 에이전트 반자동 업데이트

1. 포털에서 `자산 뉴스 → 통합 에이전트 업데이트`로 이동합니다.
2. `요청 JSON 다운로드`를 누릅니다.
3. `통합 요청문 복사` 후 `Copilot Chat 열기`를 누릅니다.
4. Copilot Chat에 요청문을 붙여넣고 `asset-news-update-request.json`을 첨부합니다.
5. 생성된 `asset-news.json`을 다운로드합니다.
6. 포털에서 `검증 결과 가져오기`를 눌러 파일을 선택합니다.
7. 검증을 통과하면 GitHub 게시용 `asset-news.json`이 다시 다운로드됩니다.
8. 해당 파일로 프로젝트의 `data/asset-news.json`을 교체합니다.
9. GitHub Desktop에서 Commit to main, Push origin을 누릅니다.
10. GitHub Actions 검사가 통과하면 GitHub Pages가 자동 배포됩니다.

GitHub Pages 설정의 Source는 `GitHub Actions`로 변경합니다.

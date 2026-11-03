# 오류 점검 결과

점검일: 2026-11-03

## 통과
- 전체 인라인 JavaScript 9개 블록 구문 검사 통과
- HTML ID 338개 중 중복 ID 없음
- JavaScript의 정적 DOM ID 참조 누락 없음
- 메뉴 showPage 대상 모두 존재
- 이미지 alt 누락 없음
- ZIP 무결성 검사 통과

## 수정
- 자산 뉴스 화면이 요청하는 `data/asset-news.json`이 기존 배포 ZIP에 누락되어 있었음
- 빈 상태에서도 정상 로드되는 초기 JSON 파일을 `data/asset-news.json`에 추가함

## 확인이 필요한 제한
- Excel 가져오기는 외부 CDN의 SheetJS에 의존함
- PDF 가져오기는 외부 CDN의 PDF.js에 의존함
- Scotiabank 카드 이미지는 외부 URL에 의존하며, 실패 시 앱의 대체 UI가 사용되어야 함
- 데이터는 브라우저 LocalStorage에 저장되므로 PC와 모바일 간 자동 동기화는 지원하지 않음
- 로컬 `file://` 실행에서는 브라우저 보안 정책 때문에 JSON fetch가 제한될 수 있으므로 전체 기능 검사는 GitHub Pages 주소에서 권장함

## 추가 수정: 자산 뉴스 표시
- 기존 초기 JSON은 뉴스 항목이 0건이어서 실제 뉴스 카드가 표시되지 않는 것이 정상 동작이었음
- JSON 로드 실패 시 화면 전체가 오류 상태가 되지 않도록 내장 빈 상태 fallback 추가
- 자산 홈 하단에 `자산 뉴스 열기` 바로가기 카드 추가
- JSON 캐시 버전을 1.1로 올려 이전 실패 응답 캐시 영향을 줄임
- 실제 뉴스가 표시되려면 `data/asset-news.json`의 `items`에 검증 완료 항목이 있어야 함

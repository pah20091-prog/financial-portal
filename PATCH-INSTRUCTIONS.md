# 리워드 이미지 흰색 표시 핫픽스

## 원인
기존 구현이 작은 Google favicon을 카드 전체 `cover` 배경으로 확대한 탓에 흰색 또는 빈 이미지처럼 보였습니다.

## 적용
1. `assets/reward-program-branding.css`와 `assets/reward-program-branding.js`를 기존 프로젝트의 `assets` 폴더에 넣습니다.
2. `index.html`의 `</head>` 바로 앞에 다음 줄을 추가합니다.

```html
<link rel="stylesheet" href="assets/reward-program-branding.css?v=1">
```

3. `index.html`의 `</body>` 바로 앞에 다음 줄을 추가합니다.

```html
<script src="assets/reward-program-branding.js?v=1"></script>
```

4. GitHub Desktop에서 Commit 후 Push합니다.

핫픽스는 기존 멤버십 v3 파일을 삭제하거나 덮어쓰지 않습니다.

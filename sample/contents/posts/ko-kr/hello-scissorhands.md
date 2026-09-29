---
title: 안녕하세요, ScissorHands
description: Markdown에서 스타터 Razor 테마를 거쳐 렌더링된 예제 글입니다.
slug: hello-scissorhands
hero_image: /images/hello-world.png
published: 2026-09-11
tags:
  - dotnet
  - static-site
---

이 페이지는 전체 생성 과정을 보여 줍니다.

1. YAML frontmatter를 불러와 유효성을 검사합니다.
2. Markdown을 HTML로 변환합니다.
3. 스타터 Razor 테마가 최종 정적 페이지를 렌더링합니다.
4. 태그 페이지와 내비게이션 링크를 자동으로 생성합니다.

```csharp
var app = new ScissorHandsApplicationBuilder(args).Build();
await app.RunAsync();
```

페이지 탐색 예제는 [테마 안내](theme-guide)에서 살펴보고, 더 긴 스타일 예제는
[Markdown 주제](ko-kr/tags/markdown)에서 찾아보세요.

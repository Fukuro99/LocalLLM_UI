# LocalLLM_UI

FastAPI + HTMX + SQLModel の最小構成サンプルです。フォーム送信やボタン操作でサーバーが返す HTML 部分を差し替えることで、シンプルなメモ一覧を実装しています。

## セットアップ

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### OpenAI API キー

AI によるメモ案生成を有効にするため、[OpenAI API キー](https://platform.openai.com/)を取得し、環境変数 `OPENAI_API_KEY` に設定してください。

```bash
export OPENAI_API_KEY="sk-..."
```

## 起動

```bash
uvicorn app.main:app --reload
```

- ブラウザで http://127.0.0.1:8000 にアクセスします。
- HTMX の `hx-post` / `hx-delete` がリスト部分を更新するため、ページ全体のリロード無しで完結します。

## 構成

- `app/main.py` : FastAPI エントリーポイント。ページレンダリングと HTMX 部分更新用エンドポイントを提供。
- `app/db.py` : SQLite / SQLModel 初期化とセッション依存性。
- `app/models.py` : `Note` モデル定義。
- `app/settings.py` : 環境変数から OpenAI API キーを読み込み、存在チェックを実施。
- `app/openai_service.py` : OpenAI クライアントの初期化とメモ案生成ヘルパー。
- `app/crud.py` : 一覧取得・作成・状態切替・削除の CRUD 処理。
- `templates/` : Jinja2 テンプレート。`pages/` がページ全体、`partials/` が HTMX で差し替える断片。
- `static/` : 静的ファイル用（必要に応じて配置）。

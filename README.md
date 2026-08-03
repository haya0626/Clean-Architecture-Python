<img src="./pinkguy.jpg" width="800" height="250">

# Clean-Architecture-Python

Python と FastAPI を使用し、Clean Architecture に基づいた Web API を構築するためのプロジェクトです。

本プロジェクトでは、業務アプリケーションを想定し、保守性・テスト容易性・変更への強さを意識した設計と実装を行います。

## 目的

以下の内容を実践的に学ぶことを目的としています。

- Python を使用した Web API 開発
- FastAPI によるエンドポイント実装
- Clean Architecture を用いた責務分離
- 型安全を意識した実装
- 単体テスト・結合テストの作成
- Linter・Formatter によるコード品質の統一
- 環境変数を利用した設定管理

## 技術スタック

| 分類                | 使用技術                        |
| ------------------- | ------------------------------- |
| Language            | Python 3.13                     |
| Package Manager     | uv                              |
| Web Framework       | FastAPI                         |
| ASGI Server         | Uvicorn                         |
| Settings            | pydantic-settings               |
| Testing             | pytest / pytest-asyncio / httpx |
| Linter / Formatter  | Ruff                            |
| Static Type Checker | mypy                            |

## 各ツールの役割

| ツール              | 用途                                   |
| ------------------- | -------------------------------------- |
| `uv`                | Python、仮想環境、依存ライブラリの管理 |
| `FastAPI`           | Web API の実装                         |
| `Uvicorn`           | FastAPI アプリケーションの起動         |
| `pydantic-settings` | 環境変数や設定値の管理                 |
| `pytest`            | テストの実行                           |
| `pytest-asyncio`    | 非同期処理のテスト                     |
| `httpx`             | API の HTTP テスト                     |
| `Ruff`              | Lint、import 整理、コードフォーマット  |
| `mypy`              | 静的型チェック                         |

## 前提環境

以下が利用できることを前提とします。

- Git
- Visual Studio Code
- PowerShell
- uv

uv がインストールされていない場合は、PowerShell で以下を実行します。

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

インストール後、PowerShell または Visual Studio Code を再起動してください。

確認コマンド：

```powershell
uv --version
```

## セットアップ

### 1. リポジトリを clone

```powershell
git clone https://github.com/haya0626/Clean-Architecture-Python.git
cd CleanArchitecture-Python
```

### 2. Python と依存ライブラリを同期

```powershell
uv sync
```

`uv sync` により、以下が自動的に行われます。

- 使用する Python バージョンの確認
- 仮想環境 `.venv` の作成
- 依存ライブラリのインストール
- `uv.lock` に基づくバージョンの同期

Python のバージョンを確認します。

```powershell
uv run python --version
```

## アプリケーションの起動

以下のコマンドで開発サーバーを起動します。

```powershell
uv run uvicorn clean_architecture_python.main:app --reload
```

起動後、以下へアクセスします。

| URL                     | 用途 |
| ----------------------- | ---- |
| `http://127.0.0.1:8000` | API  |

`--reload` を指定しているため、ソースコードを変更すると開発サーバーが自動的に再起動します。

## 開発用コマンド

### テスト

```powershell
uv run pytest
```

詳細を表示する場合：

```powershell
uv run pytest -v
```

特定のテストファイルだけ実行する場合：

```powershell
uv run pytest tests/test_sample.py
```

### Lint

```powershell
uv run ruff check .
```

自動修正可能な問題を修正する場合：

```powershell
uv run ruff check . --fix
```

### Format

```powershell
uv run ruff format .
```

フォーマット差分がないことだけ確認する場合：

```powershell
uv run ruff format --check .
```

### 型チェック

```powershell
uv run mypy
```

## 開発時の確認手順

コード変更後は、以下の順番で確認します。

```powershell
uv run ruff check .
uv run ruff format --check .
uv run mypy
uv run pytest
```

各コマンドの役割は以下です。

| コマンド              | 確認内容                   |
| --------------------- | -------------------------- |
| `ruff check`          | コード上の問題やルール違反 |
| `ruff format --check` | フォーマット差分           |
| `mypy`                | 型の不整合                 |
| `pytest`              | 実装した処理の動作         |

すべて成功した状態でコミットすることを基本とします。

## 設定ファイル

| ファイル          | 用途                                       |
| ----------------- | ------------------------------------------ |
| `pyproject.toml`  | プロジェクト情報、依存関係、各種ツール設定 |
| `uv.lock`         | 使用するライブラリのバージョン固定         |
| `.python-version` | 使用する Python バージョン                 |
| `.gitignore`      | Git 管理対象外ファイルの定義               |

## 作成するシステム

商品検索 API を作成します。

イメージ

```text
検索ボタン押下
    ↓
GET /api/products
    ↓
商品を検索
    ↓
業務ルールを判定
    ↓
検索結果を返却
```

### 検索条件

- 商品コード
- 商品名
- カテゴリ
- 販売状況
- 在庫ありのみ

検索条件はすべて任意とし、複数指定された場合は、すべての条件を満たす商品を検索します。

## 業務ルール

- 論理削除された商品は表示しない
- 商品名は部分一致で検索する
- 検索結果が 0 件の場合は空の一覧を返す
- 販売中かつ在庫が 1 個以上の商品を購入可能とする
- 販売停止中や販売期間外の商品は、在庫があっても購入不可とする

## Clean Architecture の責務

### ■ Presentation 層

- GET リクエストを受け取る
- 入力値を検証する
- Application 層を呼び出す
- JSON レスポンスを返す

### ■ Application 層

- 商品検索の処理手順を管理する
- Repository を呼び出す
- 検索結果を Presentation 層へ返す

### ■ Domain 層

- 商品や金額、販売状況を表現する
- 商品が購入可能か判定する
- 業務ルールを管理する

### ■ Infrastructure 層

- 商品を検索する
- モックデータを Domain オブジェクトへ変換する

業務ルールは `Domain 層`、処理の流れは `Application 層`、HTTP 通信は `Presentation` 層、DB 操作は `Infrastructure` 層に分けます。

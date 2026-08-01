from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    name: str    
    host: str = "127.0.0.1"
    port: int = Field(default=8000)
    reload: bool = True

    model_config = SettingsConfigDict(
        env_prefix="APP_",
        env_file=".env",
        env_file_encoding="utf-8",
        # Settingsクラスに定義していない項目が.envにあっても、エラーにせず無視する
        # 余分な設定をエラーにしたい場合は「forbid」にする
        extra="ignore",
    )

# lru_cache : 関数の実行結果を保存して再利用するためのデコレーター
@lru_cache
def get_settings() -> Settings:
    """設定の読み込み結果をプロセス内で再利用する。"""
    return Settings()

from pathlib import Path
import os
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# 本番では環境変数に逃がすのが推奨ですが、NeoGenesis方式に合わせて直書き
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")

# NeoGenesis と同様、まずは開発しやすさ優先
DEBUG = True

# Render のドメインは必要に応じて追加してください
ALLOWED_HOSTS = ["127.0.0.1", "localhost", ".onrender.com"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "core",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # NeoGenesis に合わせて WhiteNoise 等は入れない
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

"""
# ===== Database (NeoGenesis方式) =====
DATABASE_URL = os.environ.get("DATABASE_URL")

if DATABASE_URL:
    # ← ここでだけ読み込めば、ローカルSQLiteのとき依存不要
    import dj_database_url
    DATABASES = {
        "default": dj_database_url.parse(
            DATABASE_URL,
            conn_max_age=600,
            ssl_require=True,  # Render等の本番でTLS必須ならTrue
        )
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
"""

# ===== Password validation =====
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ===== i18n / tz =====
LANGUAGE_CODE = "ja"
TIME_ZONE = "Asia/Tokyo"
USE_I18N = True
USE_TZ = True

# ===== Static files =====
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"     # ← collectstaticの出力先
STATICFILES_DIRS = [BASE_DIR / "static"]  # NeoGenesis と同じ運用
# （必要になったら STATIC_ROOT を追加して collectstatic 運用に切り替え）

# 本番での圧縮・キャッシュ有効化（必須ではないが推奨）
if not DEBUG:
    STORAGES = {
        "staticfiles": {
            "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"
        }
    }

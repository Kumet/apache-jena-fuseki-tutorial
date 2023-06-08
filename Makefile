default: | help

DC = docker-compose
SITE_NAME = app

build:  ## コンテナをビルド
	@$(DC) build

up:  ## コンテナ立ち上げ
	@$(DC) up

down:  ## コンテナを停止し削除
	@$(DC) down

shell:  ## コンテナ内のシェルに入る
	@$(DC) exec $(SITE_NAME) bash

test:  ## テストを実行
	@$(DC) run --rm $(SITE_NAME) pytest

help:  ## Show all of tasks
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1,$$2}'


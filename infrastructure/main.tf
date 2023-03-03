terraform {
  required_providers {
    heroku = {
      source  = "heroku/heroku"
      version = "5.1.2"
    }
  }
}

provider "heroku" {
  api_key = var.heroku_token
}

resource "heroku_app" "app" {
  name   = "grantadams-devnote"
  region = "eu"
  buildpacks = [
    "https://github.com/LaunchPadLab/heroku-buildpack-monorepo.git",
    "heroku/python",
  ]
}

resource "random_password" "key" {
  length   = 32
  special  = false
}

resource "heroku_config" "common" {
  vars = {
    DJANGO_SETTINGS_MODULE = "api.settings.prod"
    APP_BASE               = "api"
  }
  sensitive_vars = {
    SECRET_KEY             = random_password.key.result
  }
}

resource "heroku_app_config_association" "config-association" {
  app_id         = heroku_app.app.id
  vars           = heroku_config.common.vars
  sensitive_vars = heroku_config.common.sensitive_vars
}

resource "heroku_formation" "web-formation" {
  count    = var.web-dynos > 0 ? 1 : 0
  app_id   = heroku_app.app.id
  type     = "web"
  quantity = var.web-dynos
  size     = "eco"
}

resource "heroku_addon" "database" {
  app_id  = heroku_app.app.id
  plan    = "heroku-postgresql:mini"
}

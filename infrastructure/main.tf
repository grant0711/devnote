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

resource "heroku_config" "common" {
  vars = {
    DJANGO_SETTINGS_MODULE = "api.settings.prod"
    APP_BASE               = "api"
  }
}

resource "heroku_app_config_association" "config-association" {
  app_id = heroku_app.app.id
  vars           = heroku_config.common.vars
}

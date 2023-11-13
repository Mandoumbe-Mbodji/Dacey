provider "heroku" {
  # Configuration du fournisseur Heroku
}

resource "heroku_app" "app" {
  name   = "assurema"
  region = "us"
}

resource "heroku_build" "build" {
  app = heroku_app.app.name

  buildpacks = [
    "heroku/python",
  ]

  source = "."
}

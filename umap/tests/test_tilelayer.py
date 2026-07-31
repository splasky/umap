import pytest

from .base import TileLayerFactory

pytestmark = pytest.mark.django_db


def test_tilelayer_json():
    tilelayer = TileLayerFactory(
        attribution="Attribution",
        maxZoom=19,
        minZoom=0,
        name="Name",
        rank=1,
        tms=True,
        url_template="http://{s}.x.fr/{z}/{x}/{y}",
    )
    assert tilelayer.json == {
        "attribution": "Attribution",
        "id": tilelayer.id,
        "layer_type": "raster",
        "maxZoom": 19,
        "minZoom": 0,
        "name": "Name",
        "rank": 1,
        "style_url": "",
        "tms": True,
        "url_template": "http://{s}.x.fr/{z}/{x}/{y}",
    }


def test_maplibre_tilelayer_json():
    tilelayer = TileLayerFactory(
        attribution="Attribution",
        layer_type="maplibre",
        name="Martin",
        rank=0,
        style_url="https://tiles.example.com/styles/osm/style.json",
        url_template="",
    )
    assert tilelayer.json["layer_type"] == "maplibre"
    assert tilelayer.json["style_url"] == "https://tiles.example.com/styles/osm/style.json"
    assert tilelayer.json["url_template"] == ""

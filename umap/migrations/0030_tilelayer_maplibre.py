from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("umap", "0029_datalayer_parent"),
    ]

    operations = [
        migrations.AddField(
            model_name="tilelayer",
            name="layer_type",
            field=models.CharField(
                choices=[("raster", "Raster"), ("maplibre", "MapLibre")],
                default="raster",
                help_text="Renderer used for this tile layer.",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="tilelayer",
            name="url_template",
            field=models.CharField(
                blank=True,
                default="",
                help_text="URL template using OSM tile format",
                max_length=400,
            ),
        ),
        migrations.AddField(
            model_name="tilelayer",
            name="style_url",
            field=models.URLField(
                blank=True,
                default="",
                help_text="MapLibre style JSON URL.",
            ),
        ),
    ]

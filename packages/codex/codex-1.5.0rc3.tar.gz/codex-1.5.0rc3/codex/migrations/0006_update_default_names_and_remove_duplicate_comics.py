"""Generated by Django 3.2.9 on 2021-11-04 03:03."""

from types import MappingProxyType

from django.db import migrations
from django.db.models.functions import Now

MODEL_NAMES = MappingProxyType(
    {
        "Series": "Default Series",
        "Imprint": "Main Imprint",
        "Publisher": "No Publisher",
    }
)
NEW_DEFAULT_NAME = ""
UPDATE_FIELDS = ("stat", "updated_at")


def update_default_names(apps, _schema_editor):
    """Prepare for removing the is_default field."""
    for model_name, default_name in MODEL_NAMES.items():
        model = apps.get_model("codex", model_name)
        model.objects.filter(name=NEW_DEFAULT_NAME, is_default=False).update(
            name="UNKNOWN", updated_at=Now()
        )
        model.objects.filter(name=default_name, is_default=True).update(
            name=NEW_DEFAULT_NAME, updated_at=Now()
        )


def remove_duplicate_comics(apps, _schema_editor):
    """Remove duplicate comics in preparation for looser unique constraints."""
    model = apps.get_model("codex", "Comic")
    comics = model.objects.only("pk", "library__id", "path", "updated_at")
    unique = {}
    update_comics = {}
    delete_comics = set()
    now = Now()
    for comic in comics:
        dupe_id = (comic.library_id, comic.path)
        update_comic = unique.get(dupe_id)
        if update_comic:
            if update_comic.pk not in update_comics:
                update_comic.stat = None
                update_comic.updated_at = now
                update_comics[update_comic.pk] = update_comic
            delete_comics.add(comic.pk)
        else:
            unique[dupe_id] = comic

    if not delete_comics and not update_comics:
        return
    print()
    if delete_comics:
        print(f"Deleting {len(delete_comics)} duplicate comics from database.")
        model.objects.filter(pk__in=delete_comics).delete()
    if update_comics:
        print(f"Marking {len(update_comics)} comics to be updated by the next poll.")
        model.objects.bulk_update(update_comics.values(), fields=UPDATE_FIELDS)


class Migration(migrations.Migration):
    """Change default names to ''."""

    dependencies = [
        ("codex", "0005_auto_20200918_0146"),
    ]

    operations = [
        migrations.RunPython(update_default_names),
        migrations.RunPython(remove_duplicate_comics),
    ]

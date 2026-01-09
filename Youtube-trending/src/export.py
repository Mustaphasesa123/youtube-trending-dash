import csv
import json
from datetime import datetime


def export_video_json(video: dict, filepath: str) -> None:
    payload = dict(video)
    payload["_exported_at"] = datetime.utcnow().isoformat() + "Z"
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)


def export_top10_csv(videos: list[dict], filepath: str) -> None:
    fields = ["video_id", "title", "channel_title", "category_id", "views", "likes", "comment_count"]
    with open(filepath, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for v in videos:
            writer.writerow({k: v.get(k, "") for k in fields})
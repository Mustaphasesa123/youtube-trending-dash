from collections import Counter
from typing import Optional


def total_videos(data: list[dict]) -> int:
    return len(data)


def total_channels(data: list[dict]) -> int:
    return len({row.get("channel_title") for row in data if row.get("channel_title")})


def category_counts(data: list[dict]) -> dict[int, int]:
    c = Counter()
    for row in data:
        c[row.get("category_id", 0)] += 1
    return dict(c)


def find_video(
    data: list[dict],
    *,
    video_id: Optional[str] = None,
    title_query: Optional[str] = None
) -> Optional[dict]:
    """Find video by exact id or title substring (case-insensitive)."""
    if video_id:
        target = video_id.strip()
        for row in data:
            if row.get("video_id") == target:
                return row

    if title_query:
        q = title_query.strip().lower()
        for row in data:
            if q and q in (row.get("title") or "").lower():
                return row

    return None


def top_10_by_metric(data: list[dict], metric: str) -> list[dict]:
    if metric not in {"views", "likes", "comment_count"}:
        raise ValueError("Metric must be: views, likes, comment_count")

    return sorted(data, key=lambda r: int(r.get(metric, 0)), reverse=True)[:10]
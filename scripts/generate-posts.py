import json
import re
import hashlib
from pathlib import Path
from datetime import date, datetime

POSTS_DIR = Path("posts")
OUTPUT_FILE = Path("posts.json")


def parse_front_matter(text, file_path):
    match = re.match(
        r"\A\s*---\s*\r?\n(.*?)\r?\n---\s*(?:\r?\n|$)",
        text,
        re.DOTALL
    )

    if not match:
        raise ValueError(f"Missing front matter: {file_path}")

    import yaml
    data = yaml.safe_load(match.group(1)) or {}
    body = text[match.end():].strip()

    if not isinstance(data, dict):
        raise ValueError(f"Invalid front matter: {file_path}")

    return data, body


def normalize_date(value):
    if isinstance(value, (date, datetime)):
        return value.isoformat()[:10]

    if value is None:
        return ""

    return str(value)


def make_excerpt(value, body, limit=160):
    if value:
        return str(value).strip()

    plain_text = re.sub(r"```.*?```", " ", body, flags=re.DOTALL)
    plain_text = re.sub(r"!\[.*?\]\(.*?\)", " ", plain_text)
    plain_text = re.sub(r"\[([^\]]+)\]\(.*?\)", r"\1", plain_text)
    plain_text = re.sub(r"[#>*_`~]", " ", plain_text)
    plain_text = re.sub(r"\s+", " ", plain_text).strip()

    if len(plain_text) > limit:
        return plain_text[:limit].rstrip() + "..."

    return plain_text


def main():
    posts = []

    if POSTS_DIR.exists():
        files = sorted(POSTS_DIR.rglob("*.md"))

        for file_path in files:
            content = file_path.read_bytes()
            text = content.decode("utf-8")
            
            sha = hashlib.sha1(
                b"blob " + str(len(content)).encode() + b"\0" + content
            ).hexdigest()
            
            metadata, body = parse_front_matter(text, file_path)

            title = metadata.get("title")
            slug = metadata.get("slug")
            published_date = metadata.get("date")

            if not title or not slug or not published_date:
                raise ValueError(
                    f"Missing title, slug, or date in {file_path}"
                )

            posts.append({
                "title": str(title).strip(),
                "slug": str(slug).strip(),
                "date": normalize_date(published_date),
                "cover": metadata.get("cover") or "",
                "excerpt": make_excerpt(
                    metadata.get("excerpt"), body
                ),
                "path": file_path.as_posix(),
                "sha": sha
            })

    posts.sort(
        key=lambda post: (post["date"], post["slug"]),
        reverse=True
    )

    OUTPUT_FILE.write_text(
        json.dumps(posts, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8"
    )

    print(f"Generated {OUTPUT_FILE} with {len(posts)} posts.")


if __name__ == "__main__":
    main()
  

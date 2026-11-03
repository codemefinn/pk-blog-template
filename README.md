# Carrd Blog Template

## 1. Add a Post

1. Open the `posts/` folder in your GitHub repository.

   **Tip:** The folder already contains a sample post. To use it as a starting point, click the pencil icon to edit it, replace the sample content with your own, and click **Commit changes** to save.

2. To create a new post instead, click **Add file → Create new file**.

3. Name your file after your post title using lowercase letters and hyphens, such as `my-first-post.md`. **The `.md` extension is required.**

4. Copy the following template into your file and replace the example values with your own:

  ### Required Fields

```yaml
---
title: "My First Post"
slug: "my-first-post"
date: "2026-10-27"
---

Write your article here.
```

- `title`: Your post title.
- `slug`: A unique name used in the post URL. Each post must have a different slug.
- `date`: The post date in `YYYY-MM-DD` format. This does not schedule publication.

### Optional Fields

```yaml
cover: "https://example.com/cover.jpg"
excerpt: "A short introduction to my post."
author: "John Doe"
author_url: "https://example.com"
icon: "https://example.com/avatar.jpg"
```

- `cover`: Cover image URL. Optional; omit if not needed.
- `excerpt`: Short summary shown in the post list. Optional; an excerpt is generated automatically if omitted.
- `author`: Author's name. Optional; defaults to your GitHub profile name or username. Set to `null` to hide or enter a custom name to override.
- `author_url`: URL linked to the author name. Optional; defaults to your GitHub website or profile URL. Set to `null` to hide or enter a custom URL to override.
- `icon`: Author avatar or icon. Optional; defaults to your GitHub profile avatar. Set to `null` to hide or enter a custom image URL or emoji to override.

5. Click **Commit changes** to save your post. It may take a few minutes for your post to appear on your Carrd website.

## 2. Deleting a Post

1. Open the `.md` file you want to delete in the `posts/` folder.
2. Click the three-dot menu (`...`) in the top-right corner and select **Delete file**.
3. Click the green **Commit changes** button to confirm.
   
## 3. Supported Formatting

All Carrd-supported text and link syntax is supported.

**Note:** `clipboard:` and `spoiler:` only work if the corresponding elements already exist on your Carrd page.

### Headings

Use `#` to `####` at the beginning of a line to create headings of different levels.

```markdown
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
```

### Images

Use standard Markdown image syntax:

```markdown
![Image description](https://example.com/image.jpg)
```

You can optionally add `{}` to control image width, round and alignment. These settings are not required.

```markdown
![Image](https://example.com/image.jpg){width=50%}
![Image](https://example.com/image.jpg){align=center}
![Image](https://example.com/image.jpg){round=12px}
![Image](https://example.com/image.jpg){width=80% round=50% align=center}
```

### Line Breaks

Line breaks(Enter) work normally on your Carrd website. However, they may not appear in GitHub's preview when you press Enter. If the preview looks different from what you expected, try adding two spaces at the end of a line before pressing Enter. This is optional and only affects the GitHub preview.

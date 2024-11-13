"""Get most popular projects for test."""

import json
import requests


def most_starred_projects(top: int) -> list[dict]:
    """Get job textual log data from API.

    Returns
    -------
        (str | None): Log data textual content. None if no logs available (e.g., for canceled jobs).
    """
    url = "https://gitlab.com/api/v4/projects"
    params = {"order_by": "star_count", "sort": "desc"}
    response = requests.get(url, params)  # noqa
    projects = [
        {"id": p["id"], "name": p["name"], "star_count": p["star_count"]}
        for p in response.json()
    ]
    return projects[:top]


if __name__ == "__main__":
    projects = most_starred_projects(top=15)
    with open("tests/most_starred_projects.json", mode="w", encoding="utf-8") as f:
        json.dump(projects, f, indent=2)

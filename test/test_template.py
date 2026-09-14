import json
from html.parser import HTMLParser
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from urllib.parse import quote, unquote, urljoin, urlparse


REPOSITORY = Path(__file__).resolve().parents[1]
SHARED_TAG = "C# & .NET"
SHARED_TAG_URL = "tags/" + quote(SHARED_TAG.lower(), safe="")


class RenderedPage(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.html = path.read_text(encoding="utf-8")
        self.links = []
        self.assets = []
        self.base = None
        self.navigation = None
        self.link = None
        self.feed(self.html)

    def handle_starttag(self, tag, attributes):
        attributes = dict(attributes)
        if tag == "nav":
            self.navigation = attributes.get("aria-label")
        elif tag == "base":
            self.base = attributes["href"]
        elif tag in ("link", "script"):
            url = attributes.get("href") or attributes.get("src")
            if url:
                self.assets.append(url)
        elif tag == "a":
            self.link = dict(attributes, navigation=self.navigation, text="")
            self.links.append(self.link)

    def handle_endtag(self, tag):
        if tag == "nav":
            self.navigation = None
        elif tag == "a":
            self.link = None

    def handle_data(self, data):
        if self.link is not None:
            self.link["text"] += data

    def navigation_links(self, label):
        return [link for link in self.links if link["navigation"] == label]


class TemplateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temporary = tempfile.TemporaryDirectory(prefix="scissorhands-template-")
        cls.addClassCleanup(cls.temporary.cleanup)
        cls.root = Path(cls.temporary.name)
        ignore = shutil.ignore_patterns("bin", "obj", "themes", "dist", "preview")
        for directory in ("src", "sample"):
            shutil.copytree(REPOSITORY / directory, cls.root / directory, ignore=ignore)
        for name in (
            "Directory.Build.props",
            "Directory.Packages.props",
            "global.json",
        ):
            shutil.copy2(REPOSITORY / name, cls.root / name)
        solutions = list(REPOSITORY.glob("*.slnx"))
        if len(solutions) != 1:
            raise AssertionError("Expected exactly one solution in the repository root.")
        solution = cls.root / solutions[0].name
        shutil.copy2(solutions[0], solution)

        cls.sample = cls.root / "sample"
        # Compile the same template files into the sample without requiring symlink privileges.
        shutil.copytree(cls.root / "src", cls.sample / "themes" / "theme-template")
        cls.settings_path = cls.sample / "appsettings.json"
        settings = json.loads(cls.settings_path.read_text(encoding="utf-8-sig"))
        settings["Site"].update(
            Theme="theme-template",
            BaseUrl="/docs/",
            Locale="en-US",
            UseLocaleInUrl=False,
        )
        cls.settings_path.write_text(json.dumps(settings), encoding="utf-8")

        cls.write_content("pages/guide/index.md", title="Guide", show_in_navigation=True)
        cls.write_content(
            "pages/guide/01-first.md",
            title="Z first <lesson> & notes",
            slug="guide/first step",
            show_in_navigation=True,
            tags=[SHARED_TAG],
        )
        cls.write_content(
            "pages/guide/02-second.md",
            title="A second lesson",
            slug="guide/missing-parent/second",
            show_in_navigation=True,
        )
        cls.write_content(
            "pages/hidden/index.md", title="Hidden section", show_in_navigation=False
        )
        cls.write_content(
            "pages/hidden/child.md",
            title="Suppressed child",
            show_in_navigation=True,
        )
        cls.write_content(
            "pages/draft.md", title="Draft page", show_in_navigation=True, draft=True
        )
        cls.write_content(
            "pages/zz-last.md", title="Last page", slug="finish", show_in_navigation=True
        )
        cls.write_content(
            "posts/url-test.md",
            title="Shared tag post",
            slug="post with space",
            published="2026-01-01",
            tags=[SHARED_TAG],
            show_in_navigation=True,
        )

        cls.run_dotnet("build", str(solution), "--verbosity", "quiet")
        cls.generate()
        cls.output = cls.sample / "dist"
        cls.pages = {
            str(path.relative_to(cls.output)): RenderedPage(path)
            for path in cls.output.rglob("*.html")
            if "themes" not in path.relative_to(cls.output).parts
        }

        settings["Site"]["UseLocaleInUrl"] = True
        cls.settings_path.write_text(json.dumps(settings), encoding="utf-8")
        cls.generate()
        cls.localized = RenderedPage(cls.output / "en-us" / "about" / "index.html")

    @classmethod
    def write_content(cls, relative_path, **metadata):
        path = cls.sample / "contents" / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        # JSON scalar and array syntax is also valid YAML frontmatter.
        fields = "\n".join(f"{key}: {json.dumps(value)}" for key, value in metadata.items())
        path.write_text(f"---\n{fields}\n---\n\nFixture body.\n", encoding="utf-8")

    @classmethod
    def run_dotnet(cls, *arguments):
        result = subprocess.run(
            ["dotnet", *arguments],
            cwd=cls.sample,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=180,
        )
        if result.returncode:
            raise AssertionError(result.stdout + result.stderr)

    @classmethod
    def generate(cls):
        cls.run_dotnet("run", "--no-launch-profile", "--no-build", "--", "--build")

    def page(self, route):
        return self.pages[str(Path(route) / "index.html")]

    def test_navigation_on_every_view_preserves_engine_order(self):
        expected = [
            ".",
            "about",
            "guide",
            "guide/first%20step",
            "guide/missing-parent/second",
            "finish",
            "tags",
        ]
        for path, page in self.pages.items():
            with self.subTest(path=path):
                links = page.navigation_links("Primary navigation")
                self.assertEqual(expected, [link["href"] for link in links])
                self.assertIn('<span class="navigation-label">Missing Parent</span>', page.html)
                self.assertIn('class="navigation-children"', page.html)
                self.assertNotIn('<a href="guide/missing-parent">', page.html)

    def test_page_navigation_flows_through_layout(self):
        routes = ("about", "guide", "guide/first step", "guide/missing-parent/second", "finish")
        for index, route in enumerate(routes):
            links = self.page(route).navigation_links("Page navigation")
            expected = {}
            if index:
                expected["prev"] = quote(routes[index - 1], safe="/")
            if index + 1 < len(routes):
                expected["next"] = quote(routes[index + 1], safe="/")
            with self.subTest(route=route):
                self.assertEqual(expected, {link["rel"]: link["href"] for link in links})
                self.assertTrue(all(link.get("tabindex") == "0" for link in links))

        for route in ("hidden", "hidden/child"):
            self.assertEqual([], self.page(route).navigation_links("Page navigation"))
        for path, page in self.pages.items():
            if path == "index.html" or path == "404.html" or path.startswith("tags"):
                self.assertEqual([], page.navigation_links("Page navigation"))

    def test_directory_index_and_encoded_titles(self):
        self.assertIn(str(Path("guide") / "index.html"), self.pages)
        self.assertNotIn(str(Path("guide") / "index" / "index.html"), self.pages)
        primary = self.page("guide").navigation_links("Primary navigation")
        title = next(link["text"].strip() for link in primary if link["href"] == "guide/first%20step")
        self.assertEqual("Z first <lesson> & notes", title)
        self.assertNotIn("<lesson>", self.page("guide").html)

    def test_tags_render_posts_and_pages_with_shared_urls(self):
        tag_index = self.page("tags")
        card_urls = [link["href"] for link in tag_index.links if link.get("class") == "tag-card"]
        for url in ("tags/dotnet", "tags/sample", "tags/static-site", SHARED_TAG_URL):
            self.assertIn(url, card_urls)
        # Tag output directories use the escaped tag segment.
        tagged = self.page(SHARED_TAG_URL)
        self.assertIn("<h2>Posts</h2>", tagged.html)
        self.assertIn("<h2>Pages</h2>", tagged.html)
        self.assertIn('href="guide/first%20step"', tagged.html)
        self.assertIn("Shared tag post", tagged.html)
        for page in (tagged, self.page("")):
            post_link = next(link for link in page.links if link["text"].strip() == "Shared tag post")
            self.assertTrue(post_link["href"].endswith("post%20with%20space"))
        for route in ("", "guide/first step"):
            self.assertIn(SHARED_TAG_URL, [link["href"] for link in self.page(route).links])
        post = next(page for page in self.pages.values() if "<h1>Shared tag post</h1>" in page.html)
        self.assertIn(SHARED_TAG_URL, [link["href"] for link in post.links])
        self.assertIn("Hello, ScissorHands", self.page("tags/dotnet").html)
        self.assertIn("About the sample", self.page("tags/sample").html)

    def test_localized_navigation_is_not_reescaped(self):
        nav = self.localized.navigation_links("Primary navigation")
        expected = "en-us/guide/first%20step"
        self.assertIn(expected, [link["href"] for link in nav])
        self.assertNotIn("%2520", self.localized.html)
        pager = self.localized.navigation_links("Page navigation")
        self.assertEqual(["en-us/guide"], [link["href"] for link in pager])
        self.assertEqual(
            "https://example.test/docs/" + expected,
            urljoin("https://example.test/docs/", expected),
        )
        self.assertTrue((self.output / unquote(expected) / "index.html").exists())

    def test_assets_and_links_stay_base_relative(self):
        for path, page in self.pages.items():
            with self.subTest(path=path):
                self.assertEqual("/docs/", page.base)
                for url in page.assets + [link["href"] for link in page.links]:
                    self.assertFalse(url.startswith("/"), url)
                    self.assertFalse(urlparse(url).scheme, url)
                self.assertIn("themes/theme-template/assets/css/theme.css", page.assets)
                self.assertIn("themes/theme-template/assets/js/theme.js", page.assets)


if __name__ == "__main__":
    unittest.main()

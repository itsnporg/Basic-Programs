import argparse
import os
import urllib.request
from urllib.request import urlretrieve

import cssutils
from bs4 import BeautifulSoup
from rich import print
from rich.console import Console

# create take url input from command line
parser = argparse.ArgumentParser(description="Clone a website or page")
parser.add_argument(
    "--url",
    help="Base URL of the website",
    required=True,
    type=str,
)
# parsing url from commands
args = parser.parse_args()
baseurl = args.url


console = Console()


print("[bold green]Script to clone webpage[/bold green]")


# directory = ""
def scrape_page(baseurl):
    """
    Scrape the page and return the html
    """
    opener = urllib.request.build_opener()
    opener.addheaders = [
        (
            "User-Agent",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        ),
        ("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"),
        ("Connection", "keep-alive"),
    ]
    urllib.request.install_opener(opener)
    html = urllib.request.urlopen(baseurl).read()
    return html


with console.status(status="Cloning Webpage") as status:

    try:
        soup = BeautifulSoup(scrape_page(baseurl=baseurl), "html.parser")
        formatted_soup = soup.prettify(formatter="html")
        console.print("[bold green] Initializing Index File")
        with open("index.html", "w") as f:
            f.write(formatted_soup)
        a = soup.find_all("img")
        for i in range(len(a)):
            try:
                if a[i].get("data-src"):
                    directory = a[i]["data-src"]
                elif a[i].get("src"):
                    directory = a[i]["src"]
                else:
                    continue
                console.print(f"Downloading img {str(directory)}")
                if "data:image" in directory:
                    console.print(f"[bold yellow]skipped {directory}")
                    continue
                if not os.path.exists(os.path.dirname(directory)):
                    console.print("[bold green] Creating Assets Directory")
                    os.makedirs(os.path.dirname(directory))
                testfile, headers = urlretrieve(baseurl + directory, directory)
            except Exception:
                pass
        console.print("[bold green] Downloaded all the images")

        # cloning all css files
        console.print("[bold green] Creating all the CSS files")
        a = soup.find_all("link")
        for i in range(len(a)):
            try:
                directory = a[i]["href"]
                if ".css" not in directory:
                    console.print(f"[bold yellow]skipped {directory}")
                    continue
                if "http" in directory or "https" in directory:
                    console.print(f"[bold yellow]skipped {directory}")
                    continue
                console.print(f"Downloading CSS {directory}")
                if "/" not in directory:
                    console.print(f"\tNo directory Found. Saving files {directory}")
                elif not os.path.exists(os.path.dirname(directory)):
                    console.print("[bold green] Creating directory")
                    os.makedirs(os.path.dirname(directory))
                testfile, headers = urlretrieve(baseurl + directory, directory)
                urls = list(cssutils.getUrls(cssutils.parseFile(directory)))
                if "fontawesome" in directory:
                    continue
                if len(urls) != 0:
                    for link in urls:
                        try:
                            if (
                                "http" in directory
                                or "https" in link
                                or "data:image/" in link
                            ):
                                console.print(f"[bold yellow]Skipped {link}")
                                continue
                            while "../" in link:
                                if "assets" in link:
                                    link = link[3:]
                                else:
                                    link = "assets/" + link[3:]
                            console.print(f"Downloading CSS-Image {str(link)}")
                            if "/" not in link:
                                console.print(f"No directory Found {link}")
                            elif not os.path.exists(os.path.dirname(link)):
                                console.print("[bold green] Creating directory")
                                os.makedirs(os.path.dirname(link))
                            testfile, headers = urlretrieve(baseurl + link, link)
                        except Exception:
                            pass
            except Exception:
                pass
        console.print("[bold green] Downloaded and Created All the CSS files")
        console.print("[bold green] Downloading all the  JS files")

        """
        scrape all the JS files
        """
        a = soup.find_all("script")
        for i in range(len(a)):
            try:
                if a[i].get("src"):
                    directory = a[i]["src"]
                else:
                    continue
                if "http" in directory or "https" in directory:
                    console.print(f"[bold yellow]skipped {directory}")
                    continue
                console.print(f"Downloading JS Files {directory}")
                if not os.path.exists(os.path.dirname(directory)):
                    console.print("[bold green] Creating directory")
                    os.makedirs(os.path.dirname(directory))
                testfile, headers = urlretrieve(baseurl + directory, directory)
            except Exception:
                pass

        console.print("[bold green] Downloaded all the JS files")
        console.print("[bold yellow] Cloned page and saved in root directory")
    except Exception:
        pass

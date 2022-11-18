import asyncio
import os
import sys

from pyppeteer import launch
from tqdm import tqdm


async def main():

    # create browser instance
    browser = await launch()

    # get filename
    twitter_handle = sys.argv[1]
    start, end = sys.argv[2].split("-")
    start, end = int(start), int(end)
    filename = os.path.join("urims", f"{twitter_handle}.txt")

    # get list of all URI-Ms from file
    with open(filename, "r") as infile:
        urims = list(infile.readlines())

    # crawl URI-Ms from start index to end index
    for i in tqdm(range(start - 1, end)):

        urim = urims[i].strip()

        # dereference as HTML
        page = await browser.newPage()

        # load webpage (retry 3x and mark as fail)
        for _ in range(3):
            try:
                await page.goto(urim, timeout=60e3)
                break
            except:
                await asyncio.sleep(60)
        else:
            # max retries exceeded, skip
            continue

        # save html
        try:
            html = await page.content()
        except:
            html = ""

        with open(f"html/{twitter_handle}-{i+1}.html", "w") as outfile:
            outfile.write(html)
            outfile.flush()

        try:
            await page.screenshot(
                {"path": f"screenshots/{twitter_handle}-{i+1}.png", "fullPage": True}
            )
        except:
            pass

        await page.close()

    await browser.close()


if __name__ == "__main__":

    # create event loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # run function on loop
    asyncio.get_event_loop().run_until_complete(main())

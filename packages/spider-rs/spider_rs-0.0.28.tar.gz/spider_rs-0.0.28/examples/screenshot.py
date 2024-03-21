import asyncio

from spider_rs import Website

async def main():
    website = (
        Website("https://choosealicense.com", False)
        .with_user_agent("BotBot")
        .with_headers({"authorization": "Something "})
        .with_screenshot({
            "params": {
                "cdp_params": None,
                "full_page": True,
                "omit_background": False
            },
            "bytes": False,
            "save": True,
            "output_dir": None
        })
    )
    website.crawl()
    print(website.get_links())


asyncio.run(main())

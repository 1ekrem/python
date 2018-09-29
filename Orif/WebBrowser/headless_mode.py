import asyncio # Python synchronization library.
from pyppeteer import launch

#Headless mode is that the app runs in the background so it is not visible to user.
#It is useful for Selenium user bc sometimes it may take minutes to run 1 

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://google.com')

    await page.keyboard.type('Hello, World!\n')

    input = await page.querySelector("#tsf > div:nth-child(2) > div > div.RNNXgb > div > div.a4bIc > input")
    value = await page.evaluate('(input) => input.value', input)
    print(value)

    await page.screenshot({'path': 'google.png'})

    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
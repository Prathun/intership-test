import asyncio
from playwright.async_api import async_playwright

async def main():
    url = "https://www.flipkart.com/search?q=mobile+phones+under+60000"
    max_pages = 5

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        for i in range(1, max_pages + 1):
            print(f"\n--- Page {i} ---")

            await page.goto(url, timeout=60000)

            # Close login popup if it appears
            try:
                await page.click("button._2KpZ6l._2doB4z", timeout=5000)
                print("Popup closed.")
            except:
                print("No popup to close.")

            # Wait for product titles to load
            try:
                await page.wait_for_selector("div.KzDlHZ", timeout=10000)
            except:
                print("Product titles not found.")
                await save_debug_html(page, i)
                continue

            # Get product titles and prices
            titles = await page.locator("div.KzDlHZ").all_text_contents()
            prices = await page.locator("div.Nx9bqj._4b5DiR").all_text_contents()

            if not titles or not prices:
                print("Titles or prices not found. Saving page for debug...")
                await save_debug_html(page, i)
                continue

            for title, price in zip(titles, prices):
                print(f"{title} - {price}")

            # Try to go to next page if exists
            try:
                await page.click("a._1LKTO3", timeout=5000)
                url = page.url  # update URL to new page
            except:
                print("No next page link found.")
                break

        await browser.close()

async def save_debug_html(page, page_number):
    html_content = await page.content()
    with open(f"debug_page_{page_number}.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Saved debug_page_{page_number}.html — inspect this to update selectors.")

if __name__ == "__main__":
    asyncio.run(main())

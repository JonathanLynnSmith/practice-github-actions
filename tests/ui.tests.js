const puppeteer = require("puppeteer");

test("Page loads and displays correct text", async () => {
    const browser = await puppeteer.launch({
        headless: 'new', // Set to 'new' to opt in to the new headless mode
      });    const page = await browser.newPage();
    await page.goto("file://" + __dirname + "/../src/index.html"); // Local file load

    const text = await page.$eval("#message", el => el.textContent);
    expect(text).toBe("Hello, GitHub Actions!");

    await browser.close();
});


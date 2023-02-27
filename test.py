from playwright.sync_api import sync_playwright

url = 'http://r.srvtrck.com/v1/redirect?type=link&id=42f4ebadd19f405fb1a72ca74f56fa6a&site_id=b2d0921615ab4f9197a4594787c864d9&ad_zi=YieldShare&ad_t=advertiser'
def log_request(intercepted_request):
    print("a request was made:", intercepted_request)

def run(playwright):
    webkit = playwright.webkit
    browser = webkit.launch()
    context = browser.new_context()
    page = context.new_page()
    page.on("request", log_request)
    page.goto(url)
    page.wait_for_load_state(state="load", timeout=1)
    browser.close()

with sync_playwright() as playwright:
    run(playwright)


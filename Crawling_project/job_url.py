from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = webdriver.Chrome()

job_links = [
    "https://www.saramin.co.kr/zf_user/jobs/relay/view?view_type=list&rec_idx=52898615&t_ref=jobcategory_recruit&t_ref_content=general#seq=0"
]

results = []

for link in job_links:
    driver.get(link)
    time.sleep(5)

    iframes = driver.find_elements(By.TAG_NAME, "iframe")
    if len(iframes) > 0:
        driver.switch_to.frame(iframes[0])

    body = driver.find_element(By.TAG_NAME, "body")
    text = body.text

    results.append({
        "url": link,
        "description": text
    })

    driver.switch_to.default_content()

driver.quit()

df = pd.DataFrame(results)
df.to_csv("saramin_7.csv", index=False, encoding="utf-8-sig")
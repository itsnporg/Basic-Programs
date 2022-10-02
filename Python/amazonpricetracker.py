from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
import os


# product data #
URL = "https://www.amazon.com/Instant-Pot-Plus-Programmable-Sterilizer/dp/B075CWJ3T8"
HEADER = {
    "Accept-Language": "en-GB,en;q=0.9,ar-AE;q=0.8,ar;q=0.7,en-US;q=0.6",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/97.0.4692.99 Safari/537.36",
}

res = requests.get(URL, headers=HEADER)
dump = res.text


# price info#
soup = BeautifulSoup(dump, "lxml")

product_title_mask = soup.find("span", id="productTitle").getText().split(",")
product_title = product_title_mask[0].lstrip()

mask = soup.find("span", class_="apexPriceToPay")
price = mask.find("span", class_="a-offscreen").getText().strip("$")


# smtp #
username = os.environ.get("gmail_username")
password = os.environ.get("gmail_password")

s = smtplib.SMTP(host="smtp.gmail.com", port=587)
s.starttls()
s.login(username, password)

message = f"""\
Subject: Low Price Alert -- ${price} for {product_title}

{product_title}'s price is dropped to ${price}.

Click below to buy now:
{URL}

"""

# price stats #
if float(price) <= 100:
    try:
        s.sendmail(username, username, message) 
        print("Successfully sent email")
    except smtplib.SMTPException:
        print("Error: unable to send email")
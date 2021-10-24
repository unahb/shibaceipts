## Inspiration:
As poor college students who carpool and split groceries, we have to manually read receipts, input the items purchased into a table, and calculate how much each of us has to pay. It is very time-consuming and as expected, quite boring. To end this long and tedious process, we decided to stay up all night (twice!) and make a receipt scanner using OCR; it reads, extracts, and saves the grocery items data. Since it's no fun to simply scan receipts, we decided to gamify it! We have hand-drawn generative art in the form of cute Shiba Inus of different rarities that you can collect, thus giving this project the name Shibaceipts.

## What it does:
After shopping at your favorite store, you can take a picture of your receipt or upload an old receipt to the Shibaceipt app. The OCR automatically detects, separates, and saves item names, item costs, and the total. This total is then used to generate your very own shibaceipts NFT, out of 6000+ possibilities. This NFT is saved to your Shibaceipt account and can be seen by others and sold. Through the marketplace, you are able to purchase other users' for-sale Shibas. On your account, you should be able to view your past receipts, the items purchased and their costs, and the Shibaceipts you own. The total amount of the receipt influences the rarity of the minted Shiba, with higher spending resulting in rarer traits. 

## How we built it:
We used a React-Native, Javascript frontend with a Python flask backend. The OCR parsing logic workflow is through Amazon (AWS) Textract. Shibas are generated via the receipt amount and with random weighted traits, and the accessories are combined with the shibas with the help of Pillow.

## Challenges we ran into:
We wanted to categorize the data based on the item purchased. For instance, "red gala apple" would be a fruit, "Dove moisturizer" would be a personal hygiene product, and so forth. We intended to generate shibaceipts based on the amount of products of each type created but this is a huge problem being researched for the past few years and is probably not possible to be solved in 36 hours.

## Accomplishments that we're proud of:
6000+ Shibaceipts to collect
All of the art is hand-drawn
User-friendly, cross-platform application 
Quick and precise OCR

## What's next for Shibaceipts:
We plan to introduce custom accessories for receipts that belong to particular stores, allowing for brand integration and sponsorship opportunities. 
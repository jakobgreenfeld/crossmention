# CrossMention

[CrossMention](https://crossmention.com/) is a mention exchange for B2B companies. Members mention and link each other in their own content and are paid in credits priced by domain rating.

This repository holds the public credit table and a small reference function for it.

## Credit table

A mention you place earns your site's band. A mention you receive costs the other site's band.

| Domain rating | Credits per mention |
|---|---|
| 0-19 | 1 |
| 20-39 | 2 |
| 40-59 | 4 |
| 60-79 | 8 |
| 80-100 | 15 |

Ratings are Ahrefs Domain Rating, refreshed monthly. Credits cannot be bought, sold or cashed out.

- `credit-tiers.json`: the table as data
- `credits.py`: `credits_for(dr)` returns the credits for a rating

## Links

- Site: https://crossmention.com/
- Pricing: https://crossmention.com/pricing
- Company facts: https://crossmention.com/company
- Contact: hello@crossmention.com

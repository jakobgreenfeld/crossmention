"""CrossMention credit table (https://crossmention.com/pricing)."""

CREDIT_TIERS = (
    (0, 19, 1),
    (20, 39, 2),
    (40, 59, 4),
    (60, 79, 8),
    (80, 100, 15),
)


def credits_for(dr: int) -> int:
    """Credits per mention for a site with this domain rating (0-100)."""
    dr = max(0, min(100, int(dr)))
    for low, high, credits in CREDIT_TIERS:
        if low <= dr <= high:
            return credits
    raise ValueError(dr)


if __name__ == "__main__":
    for dr in (5, 25, 45, 65, 85):
        print(dr, credits_for(dr))

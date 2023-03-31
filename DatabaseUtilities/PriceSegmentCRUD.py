from DatabaseUtilities.DBConnect import Session
from DatabaseUtilities.DBConnect import PriceSegment


class PriceSegmentCRUD:
    @staticmethod
    def get_price_segments():
        with Session() as db:
            prices = db.query(PriceSegment).all()
            return prices


prices = PriceSegmentCRUD.get_price_segments()
for p in prices:
    print(f"{p.id}.{p.bottom_line}  - {p.top_line}")
from DatabaseUtilities.DBConnect import Session
from DatabaseUtilities.DBConnect import PriceSegment


class PriceSegmentCrud:
    @staticmethod
    def get_price_segments():
        with Session() as db:
            prices = db.query(PriceSegment).all()
            return prices

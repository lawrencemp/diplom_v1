from Utilities.DBConnect import Session
from Utilities.DBConnect import PriceSegment


class PriceSegmentCRUD:
    @staticmethod
    def get_price_segments():
        with Session as db:
            return db.query(PriceSegment).all()



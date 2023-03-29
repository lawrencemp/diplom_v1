from Utilities.DBConnect import Session
from Utilities.DBConnect import TopLaptop
from typing import List


class TopLaptopCRUD:
    @staticmethod
    def write_new_top(laptops:List[TopLaptop]):
        with Session as db:
            old_laptops = db.query(TopLaptop).all()
            for old_laptop in old_laptops:
                for new_laptop in laptops:
                    if old_laptop.price_segment_id == new_laptop.price_segment_id:
                        old_laptop.link = new_laptop.link
            db.commit()

    @staticmethod
    def get_top(price_id):
        with Session as db:
            return db.query(TopLaptop).filter(TopLaptop.price_segment_id == price_id).first()

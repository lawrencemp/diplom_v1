from DatabaseUtilities.DBConnect import Session
from DatabaseUtilities.DBConnect import TopLaptop
from typing import List
from LaptopUtilities.NotebookSpecs import NotebookSpecs


class TopLaptopCrud:
    @staticmethod
    def write_new_top(laptops: List[TopLaptop]):
        with Session() as db:
            old_laptops = db.query(TopLaptop).all()
            for old_laptop in old_laptops:
                for new_laptop in laptops:
                    if old_laptop.price_segment_id == new_laptop.price_segment_id:
                        old_laptop.link = new_laptop.link
            db.commit()

    @staticmethod
    def write_top_with_price_segment(best_laptop: NotebookSpecs, price_segment: int):
        best_laptop.__str__()
        print(price_segment)
        with Session() as db:
            old_top = db.query(TopLaptop).filter(TopLaptop.price_segment_id == price_segment).first()
            old_top.link = best_laptop.link
            old_top.score = best_laptop.score
            db.commit()

    @staticmethod
    def get_top(price_id):
        with Session() as db:
            return db.query(TopLaptop).filter(TopLaptop.price_segment_id == price_id).first()

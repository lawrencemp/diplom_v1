from DatabaseUtilities.DBConnect import Session
from DatabaseUtilities.DBConnect import GpuBenchData


class GpuCrud:
    @staticmethod
    def add_gpu(gpu: GpuBenchData):
        with Session() as db:
            db.add(gpu)
            db.commit()

    @staticmethod
    def get_gpus():
        with Session() as db:
            return db.query(GpuBenchData).all()




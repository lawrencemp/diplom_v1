from DatabaseUtilities.DBConnect import Session
from DatabaseUtilities.DBConnect import CpuBenchData


class CpuCrud:
    @staticmethod
    def add_cpu(cpu: CpuBenchData):
        with Session() as db:
            db.add(cpu)
            db.commit()

    @staticmethod
    def get_cpus():
        with Session() as db:
            return db.query(CpuBenchData).all()

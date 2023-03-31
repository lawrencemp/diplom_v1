from DatabaseUtilities.CpuCRUD import CpuCRUD, CpuBenchData
from DatabaseUtilities.GpuCRUD import GpuCRUD, GpuBenchData
from LaptopUtilities.NotebookSpecs import NotebookSpecs
from typing import List
from Models.CpuModel import CpuModel
from Models.GpuModel import GpuModel
from ScoreUtilities.marks import ram_dict, rom_dict
from ScoreUtilities.geekbench_parser import CpuScoreParser


class ScoreSetter():
    def __init__(self, laptops: List[NotebookSpecs]):
        self.laptops = laptops
        self.cpu_map = map([CpuModel(cpu_name=laptop.cpu, score=-1) for laptop in self.laptops])
        self.gpu_map = map([GpuModel(gpu_name=laptop.gpu, score=-1) for laptop in self.laptops])
        self.cpus_for_parse: List[CpuBenchData] = []
        self.cpu_without_score: List[CpuModel] = []
        self.gpu_without_score: List[GpuModel] = []

    def get_cpu_scores_from_db(self):
        cpus_from_bd: List[CpuBenchData] = CpuCRUD.get_cpus()
        for cpu in self.cpu_map:
            for cpu_from_bd in cpus_from_bd:
                if cpu.cpu_name == cpu_from_bd.cpu_name:
                    cpu.score = cpu_from_bd.geekbench_multiprocess

    def get_cpus_without_score(self):
        for cpu in self.cpu_map:
            if cpu.score == -1:
                self.cpus_for_parse.append(CpuBenchData(cpu_name=cpu.name, geekbench_multiprocess=None))

    def get_cpu_scores_from_geekbench(self):
        for cpu in self.cpus_for_parse:
            try:
                cpu.geekbench_multiprocess = CpuScoreParser.get_cpu_score(CpuScoreParser.get_html(cpu.cpu_name))
            except Exception:
                cpu.geekbench_multiprocess = 0

    def write_cpu_score_to_db(self):
        for cpu in self.cpus_for_parse:
            if cpu.score > 0:
                CpuCRUD.add_cpu(cpu)
                for cpu_ in self.cpu_map:
                    if cpu_.cpu_name == cpu.cpu_name:
                        cpu_.score = cpu.geekbench_multiprocess
        # for some logging which may appear in the next releases
        self.cpu_without_score = [CpuModel(cpu_name=cpu.cpu_name, score=-1) for cpu in self.cpus_for_parse if cpu.geekbench_multiprocess <= 0]

    def get_gpu_scores_from_db(self):
        gpus_from_db: List[GpuBenchData] = GpuCRUD.get_gpus()
        for gpu in self.gpu_map:
            for gpu_fom_db in gpus_from_db:
                if gpu.gpu_name == gpu_fom_db.gpu_name:
                    gpu.score = gpu_fom_db.bench_score
        self.gpu_without_score = [gpu for gpu in self.gpu_map if gpu.score == -1]

    def add_scores_in_specs_list(self):
        for laptop in self.laptops:
            for cpu in self.cpu_map:
                if laptop.cpu == cpu.cpu_name:
                    laptop.cpu_score = cpu.score
            for gpu in self.gpu_map:
                if laptop.gpu == gpu.gpu_name:
                    laptop.gpu_score = gpu.score
            try:
                laptop.ram_score = ram_dict[laptop.ram]
                laptop.rom_score = rom_dict[laptop.rom]
            except Exception:
                #also for some logging if no such ram or rom in dict
                pass
            laptop.score = laptop.rom_score + laptop.ram_score + laptop.gpu_score + laptop.cpu_score


    def find_best_laptop(self):
        best_laptop = self.laptops[0]
        for laptop in self.laptops:
            if laptop.score > best_laptop.score:
                best_laptop = laptop
        return best_laptop


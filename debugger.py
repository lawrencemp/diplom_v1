import time
import json
from LaptopUtilities.Citilink import Citilink
from LaptopUtilities.NotebookSpecs import NotebookSpecs
from DatabaseUtilities.PriceSegmentCRUD import PriceSegmentCrud, PriceSegment
from ScoreUtilities.score_setter import ScoreSetter
from DatabaseUtilities.TopLaptopCRUD import TopLaptopCrud


def job_parse_every_day():
    print("start working")
    segments = PriceSegmentCrud.get_price_segments()
    #segments = [4]
    for segment in segments:
        start = time.time()
        citilink_parser = Citilink(segment.id)
        citilink_parser.make_url_with_prices()
        citilink_parser.selenium_start()
        max_pages = citilink_parser.find_last_page()
        citilink_parser.parse_notebook_list(max_pages)
        citilink_parser.selenium_quit()
        parsed_data_process = ScoreSetter(citilink_parser.notebooks)
        parsed_data_process.get_cpu_scores_from_db()
        parsed_data_process.get_cpus_without_score()
        parsed_data_process.get_cpu_scores_from_geekbench()
        parsed_data_process.write_cpu_score_to_db()
        parsed_data_process.get_gpu_scores_from_db()
        parsed_data_process.add_scores_in_specs_list()
        best_laptop = parsed_data_process.find_best_laptop()
        TopLaptopCrud.write_top_with_price_segment(best_laptop, citilink_parser.price_segment)
        with open("without_score_cpu.json", "a") as jsonFile:
            for cpu_without_score_ in parsed_data_process.cpu_without_score:
                jsonFile.write(cpu_without_score_.to_json())
                jsonFile.write("\n")
        with open("without_score_gpu.json", "a") as jsonFile:
            for gpu_without_score_ in parsed_data_process.gpu_without_score:
                jsonFile.write(gpu_without_score_.to_json())
                jsonFile.write("\n")
        end = time.time()
        print("Time of execution" + str(segment.id) + " segment is " + str(end-start) + " sec." )



job_parse_every_day()
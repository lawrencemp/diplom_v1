#import sqlite3

ram_dict = {
    "ram 4 гб": 6,
    "ram 8 гб": 14,
    "ram 2 гб": 2,
    "ram 16 гб": 20,
    "ram 12 гб": 17,
    "ram 32 гб": 28,
    "ram 6 гб": 10
}

rom_dict = {
'hdd 1000 гб ssd 128 гб': 10,
'ssd 256 гб': 8.5, 
'emmc 128 гб': 3,
'emmc 32 гб': 1, 
'hdd 1000 гб': 8.5, 
'ssd 128 гб': 4, 
'emmc 64 гб': 2, 
'ssd 1000 гб': 18, 
'ssd 120 гб emmc 128 гб': 7, 
'ssd 240 гб': 8, 
'ssd 256 гб intel uhd graphics ': 8.5, 
'hdd 1000 гб ssd 256 гб': 12,
'ssd 2000 гб': 22, 
'ssd 1024 гб': 18.5, 
'ssd 512 гб': 12   
}

# def myFunc(e):
#   return e['score']
#
# def specs_marks(notebook_specs, cpu_scores):
#     con = sqlite3.connect('notebook_bench_data.db')
#     cur = con.cursor()
#     cur.execute("select gpu_name, score from gpu;")
#     gpu_data = cur.fetchall()
#     gpu_not_in_list = []
#     gpu_dict = {gpu_[0] : gpu_[1] for gpu_ in gpu_data}
#     for notebook in notebook_specs:
#         i = 0
#         i += ram_dict[notebook['ram']]
#         notebook['ram_score'] = i
#         i += rom_dict[notebook['rom']]
#         i += cpu_scores[notebook['cpu']]/250
#         notebook['cpu_score'] = cpu_scores[notebook['cpu']]/250
#         if notebook['gpu'] in gpu_dict.keys():
#             i += gpu_dict[notebook['gpu']]/500
#             notebook['gpu_score'] = gpu_dict[notebook['gpu']]/500
#         else:
#             gpu_not_in_list.append(notebook['gpu'])
#             if notebook['gpu'].startswith('ssd') or notebook['gpu'].startswith('emmc'):
#                 gpu_not_in_list.append(notebook['link'])
#         notebook['score'] = i
#     con.commit()
#     con.close()
#     with open("notebook_sets", "w") as somefile2:
#         set_rom = set([notebook['rom'] for notebook in notebook_specs])
#         set_gpu = set(gpu_not_in_list)
#         print(set_rom, file = somefile2)
#         print(set_gpu, file = somefile2)
#         notebook_specs.sort(key=myFunc)
#         print(notebook_specs[:25])
#     return notebook_specs


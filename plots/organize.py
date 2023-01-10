import os
import shutil

here = "plots\KA824\D1.15\simfiles"

folders = os.listdir(here)

prev_temp = None
for folder in folders:
    # if folder[-2] == "n":
    #     shutil.rmtree(f"{here}/{folder}")
    #     print(f"{here}/{folder} deleted")



    # if folder[:6] == "T0.652":
    #     temp = f"{folder[:6]}"
    # else:
    #     temp = f"{folder[:4]}"
    # run_num = f"{folder[-1:]}"
    # if temp != prev_temp:
    #     os.mkdir(f"{here}/{temp}")
    #     print(f"{temp} created")


    
    os.rename(f"{here}/{folder}", f"{here}/T{folder}")
    os.mkdir(f"{here}/T{folder}/run-last")
    files = os.listdir(f"{here}/T{folder}/")
    for file in files:
        if file != 'run-last':
            os.rename(f"{here}/T{folder}/{file}", f"{here}/T{folder}/run-last/{file}")



    # os.mkdir(f"{here}/{temp}/run-{run_num}")

    # # #list all files in folder and move
    # files = os.listdir(f"{here}/{folder}")
    # for file in files:
    #     os.rename(f"{here}/{folder}/{file}", f"{here}/{temp}/run-{run_num}/{file}")
    # print(f"{temp} files moved to {temp}/run-{run_num}")
    # prev_temp = temp



    # os.rename(f"{here}/{folder}", f"{here}/../{folder}")


# print(folders)
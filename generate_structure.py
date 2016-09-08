import os
import subprocess
import shutil
import argparse
from loremipsum import get_sentences
import numpy as np

rng = np.random.RandomState(1)

depth = 3
number_of_dirs = 15
file_ext = [".txt", ".mp3"]
max_size = 4000


dir_names = [
    "Brian_Morales",
    "Sheila_Wheeler",
    "Mary_Todd",
    "Ella_Howard",
    "Daniel_Jackson",
    "Micheal_Sanders",
    "Kerry_Ross",
    "Lindsey_Cain",
    "Bernard_Cannon",
    "Darren_Neal",
    "Corey_Montgomery",
    "Tony_Watson",
    "Kevin_Curry",
    "Steven_Gibson",
    "Deanna_Knight",
    "Hugo_Mason",
    "Jerome_Rios",
    "Leroy_Jacobs",
    "Alonzo_Lynch",
    "Lawrence_Duncan",
    "Shelly_Johnston",
    "Rebecca_Francis",
    "Constance_Morrison",
    "Estelle_Mullins",
    "Karen_Coleman",
]

file_names = [
    "Kristopher Oliver",
    "Omar Barnes",
    "Kent Pearson",
    "Francis Powell",
    "Gina Shaw",
    "Nichole Hodges",
    "Dwight Walker",
    "Dianne Adkins",
    "Peggy Sandoval",
    "Don Sullivan",
    "Gilbert Mckenzie",
    "Ralph Park",
    "Darin Stokes",
    "Della Vega",
    "Alfredo Williamson",
    "Rolando Johnston",
    "Nick Aguilar",
    "Maxine Glover",
    "Megan French",
    "Willard Ford",
    "Timmy Gonzales",
    "Wm Douglas",
    "Hope Jimenez",
    "Rosalie Flowers",
    "Darren Shelton",
    "Brad Wheeler",
    "Muriel Walton",
    "Angelo Saunders",
    "Cassandra Cook",
    "Suzanne Daniels",
    "Velma Banks",
    "Carl Patton",
    "Ada Garrett",
    "Patricia Keller",
    "Colin Chandler",
    "Sophie Manning",
    "Marty Riley",
    "Rochelle Griffin",
    "Latoya Dunn",
    "Harold Day",
    "Gertrude Norris",
    "Dana Long",
    "Nettie Ellis",
    "Edna Martin",
    "Owen Santiago",
    "Angie Ball",
    "Bert Ramos",
    "Andy Austin",
    "Kyle Newton",
    "Eula Welch",
    "Steve Berry",
    "Fernando Wright",
    "Kayla Fletcher",
    "Ira Frazier",
    "Inez Caldwell",
    "Luke Simon",
    "Irvin Mcguire",
    "Elaine Armstrong",
    "Chad Munoz",
    "Paula Dean",
    "Gerald Mann",
    "Monica Carter",
    "Herman Hicks",
    "Freda Tucker",
    "Phil Wood",
    "Ian Andrews",
    "Constance Moss",
    "Rogelio Weber",
    "Christie Hardy",
    "Dwayne Salazar",
    "Roberto Garcia",
    "Randy Williams",
    "Heidi Evans",
    "Howard Watts",
    "Kathy Moran",
    "Simon Hogan",
    "Martin Little",
    "Viola Jefferson",
    "Paul Boyd",
    "Willis Page",
    "Darlene Simpson",
    "Nicolas Dennis",
    "Leroy Allen",
    "Elena Benson",
    "Judy Moody",
    "Vicky Montgomery",
    "Kim Lee",
    "Raquel Wilkins",
    "Isabel Roberts",
    "Danielle Hopkins",
    "Linda Schmidt",
    "Tony Curry",
    "Luis Meyer",
    "Claude Kennedy",
    "Jennifer Bowen",
    "Lori Black",
    "Judith Watson",
    "Clarence Greene",
    "Ed Perez",
    "Rickey Owens",
]

def create_files(number):
    for i in range(number):
        size = rng.randint(0, max_size)
        idx = rng.randint(0, len(file_names))
        ext = rng.randint(0, len(file_ext))
        with open("{}{}".format(file_names[idx], file_ext[ext]), 'w') as f:
            f.write('\n'.join(get_sentences(size)))

def create_dir(number, step=0):
    if step >= depth:
        return

    dirs = rng.randint(0, number)
    files = number-dirs

    create_files(files)

    for d in range(dirs):
        name = dir_names[rng.randint(len(dir_names))]
        if os.path.exists(name):
            continue
        os.mkdir(name)
        os.chdir(name)
        create_dir(number, step+1)
        os.chdir('..')

    pass

def generate_structure(fct, dir_name=None):

    if os.path.exists(dir_name):
        shutil.rmtree(dir_name)
    os.mkdir(dir_name)
    os.chdir(dir_name)

    fct()

    os.chdir('..')

def main():
    import ipdb;ipdb.set_trace()

    # Function wrapper to easily reuse code
    def f():
        def inner():
            return create_dir(number_of_dirs)
        return inner

    generate_structure(f(), dir_name='random_structure')


    # function to generate 10 directory and 10 file
    def f():
        for i in range(10):
            os.mkdir('{}{}'.format(dir_names[10], i))
            os.mkdir('{}{}'.format(file_names[10], i))
            subprocess.call(['touch', "{}{}{}".format(file_names[10], i, file_ext[0])])

    generate_structure(f, dir_name='rename_structure')



if __name__ == "__main__":
    main()
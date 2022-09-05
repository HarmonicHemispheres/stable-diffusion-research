#### IMPORTS
import typer
from rich import print
from pathlib import Path, WindowsPath
from random import randint
import sys
import os
sys.path.insert(1, r'C:\Users\heavy\projects\stable-diffusion-opt\stable-diffusion\optimizedSD')


import optimized_txt2img as txt2img

#### GLOBALS
ARTISTS = (
    # "matthew stewart",
    "John Berkey",
    "Seb McKinnon",
    # "John William Waterhouse",
    "Anton Fadeev",
    "Ian McQue",
    "Martin Deschambault",
    "Raphael Lacoste",
    "Neil Blevins",
    "Tyler Edlin",
    "Peter Draws",
    "Hubert Robert",
    "HR Giger",
    # "Bill Peet",
    # "Leonardo da Vinci",
)




#### METHODS

def main(
    prompt: str = "space ship",
    outdir: str = r"C:\Users\heavy\projects\stable-diffusion-opt\stable-diffusion\outputs\experiments-03"
    ):
    
    #### RES Small (512x512) ####
    rnd_int = randint(1,900000)

    txt2img.Args.H = 512
    txt2img.Args.W = 512
    txt2img.Args.seed = rnd_int
    txt2img.Args.n_iter = 3
    txt2img.Args.n_samples = 3
    txt2img.Args.ddim_steps = 50
    txt2img.Args.turbo = True
    txt2img.Args.outdir = f"{outdir}"
    
    for artist1 in ARTISTS:
        for artist2 in ARTISTS:
            # get in the right place
            os.chdir(r"C:\Users\heavy\projects\stable-diffusion-opt\stable-diffusion")


            # reconfigure args
            if artist1 == artist2:
                txt2img.Args.prompt = f"{prompt} {artist1}"

                # display info \ progress
                print(f"[bold yellow]i|RUNNING:  {artist1}--512x512--{rnd_int}[/bold yellow]")
                print(f"[bold yellow]i|    Saving to:  {outdir}[/bold yellow]")
            else:
                txt2img.Args.prompt = f"{prompt} {artist1} and {artist2}"

                # display info \ progress
                print(f"[bold yellow]i|RUNNING:  {artist1}|{artist2}--512x512--{rnd_int}[/bold yellow]")
                print(f"[bold yellow]i|    Saving to:  {outdir}[/bold yellow]")

            # run generation
            txt2img.main(opt=txt2img.Args)


    #### RES Large (768x768) ####


if __name__ == "__main__":
    typer.run(main)


# Tips and Shortcuts


# Upscaling
to get >3000px upscaled images from stable diffusion on a lower end graphics card (i use 2070 super) follow this process
- use `txt2img` or `img2img` from https://github.com/basujindal/stable-diffusion as this solution allows for higher res base generation (768x768 is the highest i can generate)
- after a 768x768 image is generated, use `txt2imghd` from https://github.com/jquesnelle/txt2imghd with `--H 256 --W 256` to get a 1536x1536 image
- run the 1536x1536 image through `txt2imghd` again with `--H 256 --W 256` to get a >3000x3000 px image
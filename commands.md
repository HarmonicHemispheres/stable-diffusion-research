# Commands
Here are some common commands i run with my workflow

<br>
<br>
<br>


## basujindal/stable-diffusion - `optimized_txt2img`
https://github.com/basujindal/stable-diffusion

```
python .\optimizedSD/optimized_txt2img.py `
--prompt "<TEXT>" `
--H 768 --W 768 `
--seed 12253 `
--n_iter 12 `
--n_samples 2 `
--ddim_steps 50 `
--turbo `
--out "<PATH>"
```

<br>


## basujindal/stable-diffusion - `optimized_img2img`
https://github.com/basujindal/stable-diffusion

```
python .\optimizedSD\optimized_img2img.py `
--prompt "<TEXT>" `
--init-img "<PIC PATH>" `
--seed 2487 `
--n_iter 7 `
--n_samples 2 `
--W 512 --H 512 `
--strength 0.6
```

<br>

## jquesnelle /txt2imghd - `txt2imghd`
https://github.com/jquesnelle/txt2imghd

```
python .\scripts\txt2imghd.py `
--prompt "<TEXT>" `
--img "<IMG TO UPSCALE>" `
--H 256 --W 256 `
--seed 000001 `
--n_iter 1  `
--steps 50 `
--out "<PATH>" `
--strength 0.5
```
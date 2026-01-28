Install manim - https://docs.manim.community/en/stable/installation.html

Then you can render each python file with:
manim --save_sections -qm <filename.py>

It will generate a video file in the media/videos/filename folder 

If the animation is divided into sections, you'll also get a section folder in there, which each section in a different video file.
You can change the quality by using -ql (480p) -qm(720p) or -qh(1080p).

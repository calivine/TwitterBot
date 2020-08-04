from gif import GIF_Factory
import sys



if len(sys.argv) > 3:
    path = sys.argv[1]
    scale = sys.argv[2]
    start = sys.argv[3]
    end = sys.argv[4]
    GIF_Factory.make_gif(path, int(scale), set=[int(start), int(end)])
elif len(sys.argv) == 3:
    path = sys.argv[1]
    scale = sys.argv[2]
    GIF_Factory.make_gif(path, int(scale))
else:
    GIF_Factory.scale_width_down('media/resize/6634449.gif', 'media/6634449.gif', '620')

import sys
import LayersController

# =============================
if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
    except IndexError:
        sys.exit("\nUsage: python reduce_multilayer.py <input_file>  \n"
                 "\t [-o <output_file>] [-l <layer ID>] [-with_tof] ")
    sys.stdout.write("-------------------------------------\n")
    sys.stdout.flush()

    # transformation options
    options = map(lambda x: x.lower(), sys.argv[2:])  # all to lowercase

    # check whether to correct TOF
    if '-with_tof' in options:
        lc = LayersController.LayersController(adjust_times=True)
    else:
        lc = LayersController.LayersController()

    # import data
    lc.read_data(file_name)
    # check layer if other than 1
    if '-l' in options:
        layer_id = int(options[options.index('-l') + 1])
    else:
        layer_id = 1
    # !!! Here is the remap itself (static_radiuses could be set here) !!!
    lc.remap_data(out_layer_id=layer_id, static_radiuses=False)

    # export output
    out_filename = None
    if '-o' in options:
        out_filename = options[options.index('-o') + 1]
    lc.export_remapped_data(out_filename)



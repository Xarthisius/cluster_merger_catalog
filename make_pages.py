import os
import django.template
import django.conf
import re
import girder_client

try:
    django.conf.settings.configure()
    django.setup()
except RuntimeError as msg:
    print(msg)

GIRDER_API_URL = "https://girder.hub.yt/api/v1"

gc = girder_client.GirderClient(apiUrl=GIRDER_API_URL)

sim_dict = {"1to3_b0": ("R = 1:3, b = 0 kpc", 
                        [0, 20, 30, 40, 50, 55, 60, 65, 70, 80, 90, 
                         100, 110, 120, 130, 140, 145, 150, 160, 170, 
                         180, 185, 190, 200, 210, 220, 230, 240, 250,
                         260, 300])}

def make_main_page(sims):
    sim_pages = []
    for sim, sim_info in sims.items():
        sim_pages.append(make_png_page(sim, sim_info[0], sim_info[1]))
    context = {'sim_pages': sim_pages}
    template_file = 'templates/index_template.rst'
    make_template('source/index.rst', template_file, context)

def make_png_page(sim, sim_name, filenos):
    info = []
    for fileno in filenos:
        imgs = {}
        for field in ["xray_emissivity","kT","total_density","szy"]:
            filename = "fiducial_%s_hdf5_plt_cnt_%04d_proj_z_%s" % (sim, fileno, field)
            item = gc.get("resource/search", {"q": filename, "types": '["item"]'})['item'][0]
            name = item['name']
            field = name[name.find("proj_z_")+7:name.find(".png")]
            print(field)
            imgs[field] = "http://girder.hub.yt/api/v1/item/%s/download" % item['_id']
        time = "t = %4.2f Gyr" % (fileno*0.02)
        info.append(["%04d" % fileno, time, imgs])
    outfile = "source/%s.rst" % sim
    context = {'sim': sim,
               'sim_name': sim_name,
               'info': info,
               }
    template_file = 'templates/sim_template.rst'
    make_template(outfile, template_file, context)
    return os.path.split(outfile[:-4])[-1]

def make_template(outfile, template_file, context):
    django_context = django.template.Context(context)
    template = open(template_file).read()
    template = re.sub(r' %}\n', ' %}', template)
    template = django.template.Template(template)
    open(outfile, 'w').write(template.render(django_context))

if __name__ == "__main__":
    make_main_page(sim_dict)
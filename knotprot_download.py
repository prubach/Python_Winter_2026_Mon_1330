import shutil
import logging
import os
from pathlib import Path
from urllib.request import urlopen, Request
from time import time
from PIL import Image
from multiprocessing import Pool
from functools import partial


#SEARCH_STRING = 'https://knotprot.cent.uw.edu.pl/browse/?set=True&bridgeType=probab&knotTypes=%2B31&array=0&raw=1'
SEARCH_STRING = 'https://knotprot.cent.uw.edu.pl/browse/?set=True&bridgeType=probab&slipknotTypes=%2B31&array=0&raw=1'
DOWNLOAD_LINK = 'https://knotprot.cent.uw.edu.pl/static/knot_data/{0}/{1}/{0}_{1}.png'

logger = logging.getLogger(__name__)

def get_proteins(search_string=SEARCH_STRING):
    req = Request(search_string, method='GET')
    proteins = []
    with urlopen(req) as resp:
        data = resp.read().decode('utf-8')
        for line in data.splitlines():
            if len(line)>4 and not line.startswith('#'):
                cells = line.strip().split(';')
                proteins.append((cells[0],cells[1]))
    return proteins


def download_link(directory, protein):
    download_path = os.path.join(directory, os.path.basename('{0}_{1}.png'.format(protein[0],protein[1])))
    link = DOWNLOAD_LINK.format(protein[0], protein[1])
    with urlopen(link) as image, open(download_path, 'wb') as f:
        f.write(image.read())
    logger.info('Downloaded %s', link)


def setup_download_dir(my_dir):
    download_dir = Path(my_dir)
    if download_dir.exists():
        shutil.rmtree(my_dir, ignore_errors=True)
    if not download_dir.exists():
        download_dir.mkdir()
    return str(download_dir)


def time_it(proc, dir):
    t0 = time()
    proc(dir)
    t = time()-t0
    print('Done {0} in {1} s.'.format(proc.__name__, round(t, 3)))



##########

def create_thumbnail(size, path):
    """
    Creates a thumbnail of an image with the same name as image but with
    _thumbnail appended before the extension. E.g.:

    #>>> create_thumbnail((128, 128), 'image.jpg')

    A new thumbnail image is created with the name image_thumbnail.jpg

    :param size: A tuple of the width and height of the image
    :param path: The path to the image file
    :return: None
    """
    path = Path(path)
    name = path.stem + '_thumbnail' + path.suffix
    thumbnail_path = path.with_name(name)
    image = Image.open(path)
    image.thumbnail(size)
    image.save(thumbnail_path)


def run_download_loop(my_dir):
    proteins = get_proteins()
    i = 0
    for protein in proteins:
        download_link(my_dir, protein)
        i += 1
    print('Downloaded {0} proteins.'.format(i))

def run_download_parallel(my_dir):
    proteins = get_proteins()
    download_link_dir = partial(download_link, my_dir)
    with Pool(processes=32) as pool:
        pool.map(download_link_dir, proteins)


def run_thumbnail_seq(my_dir):
    file_list = Path(my_dir).iterdir()
    for f in file_list:
        create_thumbnail((380, 380), f)


def run_thumbnail_parallel(my_dir):
    file_list = Path(my_dir).iterdir()
    cr_thumb = partial(create_thumbnail, (380, 380))
    with Pool(processes=8) as pool:
        pool.map(cr_thumb, file_list)


if __name__ == '__main__':
    my_dir = 'data_images'
    setup_download_dir(my_dir)
    #run_download_loop(my_dir)
    #time_it(run_download_loop, my_dir) # 165s
    #time_it(run_download_parallel, my_dir) # proc=4 37s
    #time_it(run_download_parallel, my_dir) # proc=8 18.5s
    time_it(run_download_parallel, my_dir) # proc=8 11.2s
    #time_it(run_thumbnail_seq, my_dir)
    time_it(run_thumbnail_parallel, my_dir)
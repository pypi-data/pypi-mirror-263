import re
from time import sleep
from typing import Literal

import arrow
import pyautogui as g
from hakai_api import Client

from ix_aims import imgs

g.PAUSE = 0.1


def move(img, confidence: float = .95):
    if loc := g.locateOnScreen(img, confidence=confidence):
        g.moveTo(*g.center(loc))


def click(img, confidence: float = .95):
    if loc := g.locateOnScreen(img, confidence=confidence):
        g.click(*g.center(loc))


def open_ix_capture():
    g.click(10, g.size().height)
    g.typewrite('ixcapture')
    g.hotkey('enter')


def go_to_processes_tab():
    click(imgs.processesBtn)


def click_yes():
    click(imgs.yesBtn)


def get_camera_params(d: 'Arrow', camera: Literal["rgb"] | Literal["nir"]):
    c = Client()
    cal = c.get(
        f"{c.api_root}/aco/camera_calibration?camera_type={camera}&valid_from<={d.isoformat()}&sort=-valid_from&limit=1").json()[
        0]
    return cal


def get_acquisitions(workorder):
    c = Client()
    res = c.get(
        f"{c.api_root}/aco/views/projects/phases/flights/dces?projectphase_num={workorder}&fields=acq_date,sess_num&distinct&sort=acq_date,sess_num")

    if res.status_code == 200:
        return res.json()
    else:
        res.raise_for_status()


def setup_work_order_day(recipe_name, save_folder, rgb_params, nir_params, year, doy):
    # New Recipe
    click(imgs.plusTab, 0.9)
    sleep(2)
    g.hotkey('tab')
    g.hotkey('ctrl', 'a')
    g.hotkey('del')
    g.typewrite(recipe_name)

    # Skip prefix name
    g.hotkey('tab')

    # Save to Folder
    g.hotkey('tab')
    g.hotkey('ctrl', 'a')
    g.hotkey('del')
    g.typewrite(save_folder)

    # Skip rgb and nir watch
    g.hotkey('tab')
    g.hotkey('tab')

    # CIR system
    g.hotkey('tab')
    g.hotkey('c')

    # Skip camera
    g.hotkey('tab')

    # Output type tiff
    g.hotkey('tab')
    g.hotkey('t')

    # Output 4-band CIR
    for _ in range(6):
        g.hotkey('tab')
    g.hotkey('space')
    g.hotkey('tab')

    # LZW compression
    for _ in range(6):
        g.hotkey('tab')
    g.typewrite('l')

    # Calibration params
    for _ in range(2):
        g.hotkey('tab')

    for param in [
        'camera_sn',
        'pixel_size_mm',
        'focal_length_mm',
        'xp_mm',
        'yp_mm',
        'k1',
        'k2',
        'k3',
        'p1',
        'p2',
        'b1',
        'b2',
    ]:
        g.hotkey('tab')
        g.hotkey('del')
        g.typewrite(str(rgb_params[param]))

        g.hotkey('tab')
        g.hotkey('del')
        g.typewrite(str(nir_params[param]))


def check_work_order_param(value: str):
    """Check worker order matches regex dd_dddd_dd pattern"""
    assert re.match(r'\d{2}_\d{4}_\d{2}',
                    value), "Work order must be in format dd_dddd_dd"
    return value


def auto_ix(work_order: str):
    work_order = check_work_order_param(work_order)
    flights = get_acquisitions(work_order)

    # Open iXCapture
    print()
    for i in range(5, 1, -1):
        # Count down to give time to switch to iXCapture
        print(f"Starting autofill in iXCapture in {i} seconds...", end='\r')
        sleep(1)
    print("Running...")

    for flight in flights:
        date = arrow.get(flight['acq_date'])
        sess = flight['sess_num']
        year = date.format('YYYY')
        doy = date.format('DDD')

        nir_params = get_camera_params(date, "nir")
        rgb_params = get_camera_params(date, "rgb")

        recipe_name = f"{work_order}_d{doy}"
        if sess:
            recipe_name += f"s{sess}"
        save_folder = f'U:\\CIR_files\\{year}'

        setup_work_order_day(recipe_name, save_folder, rgb_params, nir_params, year,
                             doy)

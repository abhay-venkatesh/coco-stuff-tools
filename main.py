# from datasets.coco_stuff_weak_bb import build_coco_stuff_weak_bb
from datasets.coco_stuff_weak_bb import verify_coco_stuff_weak_bb
from pathlib import Path

if __name__ == "__main__":
    verify_coco_stuff_weak_bb(
        filtered_data_root=Path(
            "D:/code/data/filtered_datasets/coco_sky_weak_bb_small_agg"))


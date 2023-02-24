from src.main.homework1.backend.cpu_computing import compute_on_cpu
from src.main.homework1.backend.gpu_computing import compute_on_gpu
from src.main.homework1.backend.utils import pixmap_to_image_with_format, matrix_to_pixmap


def compute(pixmaps, filters_matrices_list, on_cpu):
    images_with_formats = [pixmap_to_image_with_format(p) for p in pixmaps]
    pixmaps_matrices_list = [p[0] for p in images_with_formats]

    method = compute_on_cpu if on_cpu else compute_on_gpu
    matrices_after_filters = method(pixmaps_matrices_list, filters_matrices_list)

    return [(p, matrix_to_pixmap(matrices_after_filters[i], images_with_formats[i][1]))
            for i, p in enumerate(pixmaps)]


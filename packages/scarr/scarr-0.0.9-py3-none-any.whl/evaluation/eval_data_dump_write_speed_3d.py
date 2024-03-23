import zarr
from imagecodecs.numcodecs import JpegXl
from numcodecs import Blosc
import numpy as np
import numcodecs
import shutil
import perfplot
from pathlib import Path
from os.path import join
import plotly.graph_objects as go
import dask.array as da
import pickle
import inspect
from collections import defaultdict
import random
import utils
import time

numcodecs.register_codec(JpegXl)

def m_numpy_uncompressed(name, array, chunk_size):
    # print(f"{inspect.currentframe().f_code.co_name}: {name}")
    np.save(join(tmp_dir, f"{inspect.currentframe().f_code.co_name}_{name}.npy"), array)

def m_numpy_compressed(name, array, chunk_size):
    # print(f"{inspect.currentframe().f_code.co_name}: {name}")
    np.savez_compressed(join(tmp_dir, f"{inspect.currentframe().f_code.co_name}_{name}.npz"), array=array)

def m_zarr_default(name, array, chunk_size):
    # print(f"{inspect.currentframe().f_code.co_name}: {name}")
    array_zarr = zarr.open(join(tmp_dir, f"{inspect.currentframe().f_code.co_name}_{name}.zarr"), shape=array.shape, chunks=chunk_size, dtype=array.dtype, mode='w')
    array_zarr[...] = array

def m_zarr_uncompressed(name, array, chunk_size):
    # print(f"{inspect.currentframe().f_code.co_name}: {name}")
    array_zarr = zarr.open(join(tmp_dir, f"{inspect.currentframe().f_code.co_name}_{name}.zarr"), shape=array.shape, chunks=chunk_size, dtype=array.dtype, mode='w', compressor=None)
    array_zarr[...] = array

# def m_zarr_dask_default(name, array, chunk_size):
#     # print(f"{inspect.currentframe().f_code.co_name}: {name}")
#     array_zarr = zarr.open(join(tmp_dir, f"{inspect.currentframe().f_code.co_name}_{name}.zarr"), shape=array.shape, chunks=chunk_size, dtype=array.dtype, mode='w')
#     dask_array = da.from_array(array, chunks=chunk_size)
#     da.store(dask_array, array_zarr)

# def m_zarr_dask_uncompressed(name, array, chunk_size):
#     # print(f"{inspect.currentframe().f_code.co_name}: {name}")
#     array_zarr = zarr.open(join(tmp_dir, f"{inspect.currentframe().f_code.co_name}_{name}.zarr"), shape=array.shape, chunks=chunk_size, dtype=array.dtype, mode='w', compressor=None)
#     dask_array = da.from_array(array, chunks=chunk_size)
#     da.store(dask_array, array_zarr)

def m_zarr_jpegxl_lossless(name, array, chunk_size):
    # print(f"{inspect.currentframe().f_code.co_name}: {name}")
    array_zarr = zarr.open(join(tmp_dir, f"{inspect.currentframe().f_code.co_name}_{name}.zarr"), shape=array.shape, chunks=chunk_size, dtype=array.dtype, mode='w', compressor=JpegXl(lossless=True))
    array_zarr[...] = array

def m_zarr_jpegxl_lossy(name, array, chunk_size):
    # print(f"{inspect.currentframe().f_code.co_name}: {name}")
    array_zarr = zarr.open(join(tmp_dir, f"{inspect.currentframe().f_code.co_name}_{name}.zarr"), shape=array.shape, chunks=chunk_size, dtype=array.dtype, mode='w', compressor=JpegXl(lossless=False))
    array_zarr[...] = array

# def m_zarr_dask_jpegxl_lossless(name, array, chunk_size):
#     # print(f"{inspect.currentframe().f_code.co_name}: {name}")
#     array_zarr = zarr.open(join(tmp_dir, f"{inspect.currentframe().f_code.co_name}_{name}.zarr"), shape=array.shape, chunks=chunk_size, dtype=array.dtype, mode='w', compressor=JpegXl(lossless=True))
#     dask_array = da.from_array(array, chunks=chunk_size)
#     da.store(dask_array, array_zarr)

def m_zarr_blosc_blosclz(name, array, chunk_size):
    # print(f"{inspect.currentframe().f_code.co_name}: {name}")
    compressor = Blosc('blosclz')
    array_zarr = zarr.open(join(tmp_dir, f"{inspect.currentframe().f_code.co_name}_{name}.zarr"), shape=array.shape, chunks=chunk_size, dtype=array.dtype, mode='w', compressor=compressor)
    array_zarr[...] = array

def m_zarr_blosc_lz4(name, array, chunk_size):
    # print(f"{inspect.currentframe().f_code.co_name}: {name}")
    compressor = Blosc('lz4')
    array_zarr = zarr.open(join(tmp_dir, f"{inspect.currentframe().f_code.co_name}_{name}.zarr"), shape=array.shape, chunks=chunk_size, dtype=array.dtype, mode='w', compressor=compressor)
    array_zarr[...] = array

def m_zarr_blosc_lz4hc(name, array, chunk_size):
    # print(f"{inspect.currentframe().f_code.co_name}: {name}")
    compressor = Blosc('lz4hc')
    array_zarr = zarr.open(join(tmp_dir, f"{inspect.currentframe().f_code.co_name}_{name}.zarr"), shape=array.shape, chunks=chunk_size, dtype=array.dtype, mode='w', compressor=compressor)
    array_zarr[...] = array

def m_zarr_blosc_zlib(name, array, chunk_size):
    # print(f"{inspect.currentframe().f_code.co_name}: {name}")
    compressor = Blosc('zlib')
    array_zarr = zarr.open(join(tmp_dir, f"{inspect.currentframe().f_code.co_name}_{name}.zarr"), shape=array.shape, chunks=chunk_size, dtype=array.dtype, mode='w', compressor=compressor)
    array_zarr[...] = array

def m_zarr_blosc_zstd(name, array, chunk_size):
    # print(f"{inspect.currentframe().f_code.co_name}: {name}")
    compressor = Blosc('zstd')
    array_zarr = zarr.open(join(tmp_dir, f"{inspect.currentframe().f_code.co_name}_{name}.zarr"), shape=array.shape, chunks=chunk_size, dtype=array.dtype, mode='w', compressor=compressor)
    array_zarr[...] = array

def m_zarr_zip(name, array, chunk_size):
    # print(f"{inspect.currentframe().f_code.co_name}: {name}")
    zip_store = zarr.ZipStore(join(tmp_dir, f"{inspect.currentframe().f_code.co_name}_{name}.zip"), compression=0, mode='w')
    grp = zarr.group(zip_store)
    grp.create_dataset("array", data=array, chunks=chunk_size, dtype=array.dtype)
    zip_store.close()

# def m_zarr_dask_zip(name, array, chunk_size):
#     # print(f"{inspect.currentframe().f_code.co_name}: {name}")
#     array_zarr = zarr.create(shape=array.shape, chunks=chunk_size, dtype=array.dtype, store=zarr.ZipStore(join(tmp_dir, f"{inspect.currentframe().f_code.co_name}_{name}.zip"), compression=0, mode='w'))
#     dask_array = da.from_array(array, chunks=chunk_size)
#     da.store(dask_array, array_zarr)

def m_zarr_zip_uncompressed(name, array, chunk_size):
    # print(f"{inspect.currentframe().f_code.co_name}: {name}")
    zip_store = zarr.ZipStore(join(tmp_dir, f"{inspect.currentframe().f_code.co_name}_{name}.zip"), compression=0, mode='w')
    grp = zarr.group(zip_store)
    grp.create_dataset("array", data=array, chunks=chunk_size, dtype=array.dtype, compressor=None)
    zip_store.close()

# def m_zarr_dask_zip_uncompressed(name, array, chunk_size):
#     # print(f"{inspect.currentframe().f_code.co_name}: {name}")
#     array_zarr = zarr.create(shape=array.shape, chunks=chunk_size, dtype=array.dtype, compression=None, store=zarr.ZipStore(join(tmp_dir, f"{inspect.currentframe().f_code.co_name}_{name}.zip"), compression=0, mode='w'))
#     dask_array = da.from_array(array, chunks=chunk_size)
#     da.store(dask_array, array_zarr)

def m_zarr_zip_jpegxl_lossless(name, array, chunk_size):
    # print(f"{inspect.currentframe().f_code.co_name}: {name}")
    zip_store = zarr.ZipStore(join(tmp_dir, f"{inspect.currentframe().f_code.co_name}_{name}.zip"), compression=0, mode='w')
    grp = zarr.group(zip_store)
    grp.create_dataset("array", data=array, chunks=chunk_size, dtype=array.dtype, compressor=JpegXl(lossless=True))
    zip_store.close()

def m_zarr_zip_jpegxl_lossy(name, array, chunk_size):
    # print(f"{inspect.currentframe().f_code.co_name}: {name}")
    zip_store = zarr.ZipStore(join(tmp_dir, f"{inspect.currentframe().f_code.co_name}_{name}.zip"), compression=0, mode='w')
    grp = zarr.group(zip_store)
    grp.create_dataset("array", data=array, chunks=chunk_size, dtype=array.dtype, compressor=JpegXl(lossless=False))
    zip_store.close()

# def m_zarr_dask_zip_jpegxl_lossless(name, array, chunk_size):
#     print(f"{inspect.currentframe().f_code.co_name}: {name}")
#     array_zarr = zarr.create(shape=array.shape, chunks=chunk_size, dtype=array.dtype, compressor=JpegXl(lossless=True), store=zarr.ZipStore(join(tmp_dir, f"{inspect.currentframe().f_code.co_name}_{name}.zip"), compression=0, mode='w'))
#     dask_array = da.from_array(array, chunks=chunk_size)
#     da.store(dask_array, array_zarr)

# def m_zarr_dask_zip_jpegxl_lossy(name, array, chunk_size):
#     print(f"{inspect.currentframe().f_code.co_name}: {name}")
#     array_zarr = zarr.create(shape=array.shape, chunks=chunk_size, dtype=array.dtype, compressor=JpegXl(lossless=False), store=zarr.ZipStore(join(tmp_dir, f"{inspect.currentframe().f_code.co_name}_{name}.zip"), compression=0, mode='w'))
#     dask_array = da.from_array(array, chunks=chunk_size)
#     da.store(dask_array, array_zarr)

def setup(index):
    array = utils.load_nifti(join(dataset_dir, f"{names[index]}.nii.gz")).astype(np.float32)
    return names[index], array, False

def plot(methods, eval_results, title, save_filepath):
    fig = go.Figure()
    for method in methods:
        fig.add_trace(go.Scatter(x=names, y=eval_results[method.__name__], mode='lines', name=method.__name__[2:]))
    fig.update_layout(title=title, xaxis_title='Dataset', yaxis_title='Runtime [s]')
    fig.write_image(save_filepath)

if __name__ == '__main__':
    start_time = time.time()
    tmp_dir = "/home/k539i/Documents/projects/Scarr/evaluation/tmp"
    Path(tmp_dir).mkdir(parents=True, exist_ok=True)

    random.seed(2024)
    dataset_dir = "/home/k539i/Documents/datasets/original/HI_2023_ScribbleSupervision/evaluation/Dataset1200_AMOS2022_task2/imagesTr"
    names = utils.load_filenames(dataset_dir)
    random.shuffle(names)
    names = names[:10]

    methods = [globals()[name] for name in globals() if callable(globals()[name]) and name.startswith('m_')]

    b = perfplot.bench(
        setup=setup,
        kernels=methods,
        title="3D data dump write speed comparison",
        n_range=range(len(names)),
        xlabel="Dataset",
        equality_check=None,
    )

    eval_results = {method.__name__: method_runtime for method, method_runtime in zip(methods, b.timings_s)}

    # shutil.rmtree(tmp_dir)
    # shutil.rmtree("/home/k539i/Documents/network_drives/cluster-home/projects/scarr/evaluation/tmp", ignore_errors=True)

    with open('/home/k539i/Documents/projects/Scarr/evaluation/results/eval_data_dump_write_speed_3d/eval_results.pkl', 'wb') as handle:
        pickle.dump(eval_results, handle, protocol=pickle.HIGHEST_PROTOCOL)

    duration = np.round(((time.time() - start_time) / 60), 0)
    print(f"Benchmarking time: {duration}m")

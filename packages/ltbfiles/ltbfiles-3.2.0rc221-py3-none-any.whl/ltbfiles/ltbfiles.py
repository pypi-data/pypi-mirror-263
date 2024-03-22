"""
This module contains functions designed for reading file formats used by LTB spectrometers.

LICENSE
  Copyright (C) 2023 Dr. Sven Merk

  This program is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation; either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License along
  with this program; if not, write to the Free Software Foundation, Inc.,
  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""
import collections
import configparser
import json
from pathlib import Path
import struct
from typing import Union, Optional, Tuple, List, BinaryIO
import zipfile
import numpy as np
import numpy.typing as npt

__pdoc__ = {}

Spectra = collections.namedtuple('Spectra', ['Y', 'x', 'o', 'head'])
"""Named tuple containing the data loaded from files."""
__pdoc__['Spectra.Y'] = 'A p x n numpy array with "n" being the number of spectra and "p" the number of pixels.'
__pdoc__['Spectra.x'] = 'The wavelength axis, a p x 1 numpy array.'
__pdoc__['Spectra.o'] = 'The spectral order information, a p x 1 numpy array.'
__pdoc__['Spectra.head'] = 'A list[dict] containing the spectra metadata. Its len is "n"'


SPEC_EXTENSIONS = ['.ary', '.aryx']
"""Default set of supported extensions for Aryelle spectra files."""


class UnknownTypeException(Exception):
    """Exception thrown when trying to load a spectrum file that is not supported."""

    def __init__(self, extension: str):
        """Construct an exception message with the given file extension."""
        super().__init__(f"Unknown file extension '{extension}'")


class IncompatibleSpectraException(Exception):
    """Exception thrown whenever spectra are not compatible, e.g. the wavelength does not match."""


def _load_file(filename: Union[Path,str]) -> Spectra:
    filename = Path(filename)
    ext = filename.suffix.lower()
    if ".ary" == ext:
        return read_ltb_ary(filename)
    if  ".aryx" == ext:
        return read_ltb_aryx(filename)
    raise UnknownTypeException(ext)


def load_files(filelist: Union[List[Path],List[str]], *, interpolate:bool=False) -> Spectra:
    """
    Read the content of multiple spectra files into a merged numpy-array.

    :param filenames: List of filenames to be loaded

    Keyword Arguments
    
    :param interpolate: Interpolate if wavelength axis does not match.

    :return:
    - `Spectra`: namedtuple
        A named tuple containing the loaded data.
    """
    if not isinstance(filelist, list):
        filelist = [filelist]
    assert len(filelist) > 0, "At least one file must be passed"
    y, wl, order, h = _load_file(filelist[0])
    Y = np.full((len(y), len(filelist)), np.nan)
    Y[:,0] = y
    head = [h]
    if len(filelist) > 1:
        for i_file, file in enumerate(filelist[1:], start=1):
            y,x,o,h = _load_file(file)
            if not (np.array_equal(x, wl) and np.array_equal(o, order)):
                if not interpolate:
                    raise IncompatibleSpectraException(
                        f"Can only merge spectra with identical wavelength axis (current: '{str(file)}'")
                y = np.interp(wl, x, y)
                order = np.zeros(x.shape)
            Y[:,i_file] = y
            head.append(h)
    return Spectra(Y, wl, order, head)


def scan_for_files(folder: Union[Path,str], *, extensions=None) -> List[Path]:
    """
    Create a list of all spectra in a given folder.

    :param folder: Name of the folder to be scanned for files
    
    Keyword Arguments

    :param extensions: File extensions that should be searched for. Default = `SPEC_EXTENSIONS`
    
    :return:

    - files: list[Path]
        List of spectra files found within the folder.
    """
    folder = Path(folder)
    if extensions is None:
        extensions = SPEC_EXTENSIONS
    return [
        folder / file for file in folder.iterdir()
        if any(ext == file.suffix for ext in extensions)
    ]


def load_folder(folder: Union[Path,str], *, interpolate:bool=False, extensions=None) -> Optional[Spectra]:
    """
    Load all spectra to be found in a given folder.

    :param folder: Name of the folder to be scanned for spectra
    
    Keyword Arguments
    
    :param interpolate: Interpolate if wavelength axis does not match.
    :param extensions: File extensions that should be searched for. Default = `SPEC_EXTENSIONS`
    
    :return:
    - `Spectra`: namedtuple
        Spectra loaded from the folder.
    """
    if extensions is None:
        extensions = SPEC_EXTENSIONS
    files = scan_for_files(folder, extensions=extensions)
    if len(files) > 0:
        Y, x, o, head = load_files(files, interpolate=interpolate)
        return Spectra(Y,x,o,head)
    return None


AIF_DTYPE_ARY = np.dtype([('indLow', np.int32),
                        ('indHigh', np.int32),
                        ('order', np.int16),
                        ('lowPix', np.int16),
                        ('highPix', np.int16),
                        ('foo', np.int16),
                        ('lowWave', np.float32),
                        ('highWave', np.float32)])


def __read_ary_spec(spec: bytes, sort_wl: bool) -> Tuple[npt.NDArray, npt.NDArray, npt.NDArray]:
    dt = np.dtype([('int', np.float32), ('wl', np.float32)])
    values = np.frombuffer(spec, dtype=dt)
    if sort_wl:
        sort_order = np.argsort(values['wl'])
        x = values['wl'][sort_order]
        y = values['int'][sort_order]
    else:
        sort_order = np.arange(0, len(values['wl']))
        x = values['wl']
        y = values['int']
    return y, x, sort_order


def __read_ary_meta(meta) -> dict:
    head = {}
    for i_line in meta:
        stripped_line = str.strip(i_line)
        if '[end of file]' == str.strip(stripped_line):
            break
        new_entry = stripped_line.split('=')
        head[new_entry[0].replace(' ', '_')] = new_entry[1]
    return head


def read_ltb_ary(file: Union[Path,str,BinaryIO], *, sort_wl: bool=True) -> Spectra:
    """
    Read data from a binary *.ary file for LTB spectrometers.

    :param file: Either the Name of the *.aryx file to be read, an open file handle or a `io.BinaryIO` object.
        If a name is given, it may be a relative path or full filename.

    Keyword Arguments
    
    :param sortWL: Specify if spectra should be sorted by their wavelength after reading. default = True
    
    :return:

    - `Spectra`: namedtuple
        The spectrum loaded.

    Caution! Due to order overlap, it may happen that two pixels have the
    same wavelength. If this causes problems in later data treatment, such
    pixels should be removed using

    ```
    x, ind = numpy.unique(x, True)
    o=o[ind]
    y=y[ind]
    ```
    """
    x = None
    y = None
    sort_order = None
    order_info = None
    head = {}

    with zipfile.ZipFile(file) as f_zip:
        file_list = f_zip.namelist()

        for i_file in file_list:
            if i_file.endswith('~tmp'):
                y, x, sort_order = __read_ary_spec(f_zip.read(i_file), sort_wl=sort_wl)
            elif i_file.endswith('~aif'):
                order_info = np.frombuffer(f_zip.read(i_file), AIF_DTYPE_ARY)
            elif i_file.endswith('~rep'):
                head = __read_ary_meta(f_zip.read(i_file).decode("utf-8").splitlines())

        assert x is not None and y is not None, "File is corrupted. No spectral information was found."
        scaling = str(head.get("Scaling"))
        head["Raman_excitation_wavelength"] = str(head.pop("Raman_exitation_wavelength", "0"))
        excitation_wl = float(head["Raman_excitation_wavelength"])
        if (scaling is not None) and ("Raman" in scaling) and (excitation_wl > 0):
            x = (1e7 / excitation_wl) - (1e7 / x)
            head["x_unit"] = "cm^{-1}"
            head["x_name"] = "Raman shift"
        else:
            head["x_unit"] = "nm"
            head["x_name"] = "Wavelength"
        if (sort_order is not None) and (order_info is not None):
            o = np.empty(x.size)
            o[:] = np.NAN
            for i_curr_order in order_info:
                o[i_curr_order['indLow']:i_curr_order['indHigh'] + 1] = i_curr_order['order']
            o = o[sort_order]
        else:
            o = np.ones(x.size)

    if isinstance(file, (Path, str)):
        head['filename'] = Path(file)
    elif hasattr(file, "name"):
        head['filename'] = Path(file.name)
    else:
        head['filename'] = "memory"
    return Spectra(y, x, o, head)


AIF_DTYPE_ARYX = np.dtype([('indLow', np.int32),
                      ('indHigh', np.int32),
                      ('order', np.int16),
                      ('lowPix', np.int16),
                      ('highPix', np.int16),
                      ('foo', np.int16),
                      ('lowWave', np.float64),
                      ('highWave', np.float64)])


def __read_aryx_spec(spec: bytes, sort_wl: bool) -> Tuple[npt.NDArray, npt.NDArray, npt.NDArray]:
    dt = np.dtype([('int', np.float64), ('wl', np.float64)])
    values = np.frombuffer(spec, dtype=dt)
    if sort_wl:
        sort_order = np.argsort(values['wl'])
    else:
        sort_order = np.arange(0, len(values['wl']))
    x = values['wl'][sort_order]
    y = values['int'][sort_order]
    return y, x, sort_order


def read_ltb_aryx(file: Union[Path,str,BinaryIO], *, sort_wl:bool=True) -> Spectra:
    """
    Read data from a binary *.aryx file for LTB spectrometers.

    :param file: Either the Name of the *.aryx file to be read, an open file handle or a `io.BinaryIO` object.
        If a name is given, it may be a relative path or full filename.
    
    Keyword Arguments
    
    :param sortWL: Specify if spectra should be sorted by their wavelength after reading. default = True
    
    :return:

    - `Spectra`: namedtuple
        The spectrum loaded.
    """
    x = None
    y = None
    sort_order = None
    order_info = None
    head = {}

    with zipfile.ZipFile(file) as f_zip:
        file_list = f_zip.namelist()
        for i_file in file_list:

            if i_file.endswith('~tmp'):
                y, x, sort_order = __read_aryx_spec(f_zip.read(i_file), sort_wl=sort_wl)
            elif i_file.endswith('~aif'):
                aif = f_zip.read(i_file)
                order_info = np.frombuffer(aif, AIF_DTYPE_ARYX)
            elif i_file.endswith('~json'):
                rep = f_zip.read(i_file).decode("utf-8")
                head = json.loads(rep)

        assert x is not None and y is not None, "File is corrupted. No spectral information was found."
        excitation_wl = head["measure"].get("ExcitationLength")
        if excitation_wl is not None:
            x = (1e7 / float(excitation_wl)) - (1e7 / x)
            head["x_unit"] = "cm^{-1}"
            head["x_name"] = "Raman shift"
        else:
            head["x_unit"] = "nm"
            head["x_name"] = "Wavelength"
        if (sort_order is not None) and (order_info is not None):
            o = np.empty(x.size)
            o[:] = np.NAN
            for i_curr_order in order_info:
                o[i_curr_order['indLow']:i_curr_order['indHigh'] + 1] = i_curr_order['order']
            o = o[sort_order]
        else:
            o = np.ones(x.size)

    if isinstance(file, (Path, str)):
        head['filename'] = Path(file)
    elif hasattr(file, "name"):
        head['filename'] = Path(file.name)
    else:
        head['filename'] = "memory"
    return Spectra(y, x, o, head)


def write_ltb_aryx(file: Union[str,Path,BinaryIO], spec: Spectra) -> None:
    """
    Write data to a binary *.aryx file for LTB spectrometers, readable by Sophi_nXt.

    :param file: Target for writing. Can be a file name, BytesIO object or an open file handle.
    :param spec: Named tuple `Spectra` containing the spectrum to be written.
        Only a single spectrum can be written to a file.
    """
    if len(spec.Y.shape) > 1:
        raise ValueError("The aryx file format can only store singular spectra")
    ind = np.lexsort((spec.x, -spec.o))
    y = spec.Y[ind]
    x = spec.x[ind]
    o = spec.o[ind]

    orders = np.unique(o)
    aif = np.empty((len(orders)), dtype=AIF_DTYPE_ARYX)
    for i, order in enumerate(orders):
        i_order = np.argwhere(order == o)
        first_pix = i_order[0]
        last_pix = i_order[-1]
        aif["indLow"][i] = first_pix
        aif["indHigh"][i] = last_pix
        aif["order"][i] = order
        aif["lowPix"][i] = 0 # raw image column start, can not be recovered -> fake
        aif["highPix"][i] = last_pix - first_pix # raw image column end, can not be recovered -> fake
        aif["foo"][i] = 0
        aif["lowWave"][i] = x[first_pix]
        aif["highWave"][i] = x[last_pix]

    head = spec.head
    head.pop("filename", None)

    if isinstance(file, (Path, str)):
        stem = Path(file).stem
    elif hasattr(file, "name"):
        stem = Path(file.name).stem
    else:
        stem = "spectrum"
    with zipfile.ZipFile(file, mode="w") as f_zip:
        f_zip.writestr(stem + ".~tmp", np.vstack((y,x)).T.tobytes())
        f_zip.writestr(stem + ".~aif", aif.tobytes())
        f_zip.writestr(stem + ".~json", json.dumps(head, allow_nan=False))


def _make_header_from_array(data):
    head = {'ChipWidth': int(data[0]),
            'ChipHeight': int(data[1]),
            'PixelSize': float(data[2]),
            'HorBinning': int(data[3]),
            'VerBinning': int(data[4]),
            'BottomOffset': int(data[5]),
            'LeftOffset': int(data[6]),
            'ImgHeight': int(data[7]),
            'ImgWidth': int(data[8])
            }
    return head


def read_ltb_raw(file: Union[Path,str,BinaryIO]) -> Tuple[np.ndarray, dict]:
    """
    Read a *.raw image file created with LTB spectrometers.
    
    :param file: Either the Name of the *.aryx file to be read, an open file handle or a `io.BinaryIO` object.
        If a name is given, it may be a relative path or full filename.

    :return:
    
    - image: np.array of image shape
    - head: dict containing image properties
    """
    data = np.loadtxt(file)
    head = _make_header_from_array(data[0:9])
    image = np.reshape(data[9:].astype(np.int32), (head['ImgHeight'], head['ImgWidth']))
    return image, head


def read_ltb_rawb(filename: Union[Path,str]) -> Tuple[np.ndarray, dict]:
    """
    Read a *.rawb image file created with LTB spectrometers.
    
    :param filename: Name of the *.rawb file to be read. May be a relative path or full filename.

    :return:

    - image : np.array of image shape
    - head : dict containing image properties
    """
    struct_fmt = '=iidiiiiii'
    struct_len = struct.calcsize(struct_fmt)
    struct_unp = struct.Struct(struct_fmt).unpack_from

    with open(filename,'rb') as f_file:
        metadata = f_file.read(struct_len)
        im_stream = np.fromfile(f_file, dtype=np.int32)
        h = struct_unp(metadata)
        head = _make_header_from_array(h)
        image = np.reshape(im_stream, (head['ImgHeight'], head['ImgWidth']))
    return image, head


def read_ltb_rawx(file: Union[Path,str,BinaryIO]) -> Tuple[np.ndarray, dict]:
    """
    Reads a *.rawx image file created with LTB spectrometers.
    
    :param file: Either the Name of the *.aryx file to be read, an open file handle or a `io.BinaryIO` object.
        If a name is given, it may be a relative path or full filename.

    :return:
    - image : np.array of image shape
    - head : dict containing all measurement and spectrometer parameters
    """
    with zipfile.ZipFile(file) as f_zip:
        file_list = f_zip.namelist()
        image = None
        sophi_head = configparser.ConfigParser()
        aryelle_head = configparser.ConfigParser()
        for i_file in file_list:
            if i_file.endswith('rawdata'):
                img = f_zip.read(i_file).decode("utf-8").splitlines()
                image = np.loadtxt(img)
            elif i_file.lower() == 'aryelle.ini':
                ary_ini = f_zip.read(i_file).decode("utf-8")
                aryelle_head.read_string(ary_ini)
            elif i_file.lower() == 'sophi.ini':
                sophi_ini = f_zip.read(i_file).decode("utf-8")
                sophi_head.read_string(sophi_ini)
        width = int(aryelle_head['CCD']['width']) // int(sophi_head['Echelle 1']['vertical binning'])
        height = int(aryelle_head['CCD']['height']) // int(sophi_head['Echelle 1']['horizontal binning'])
        head = {'sophi_ini': sophi_head,
                'aryelle_ini': aryelle_head}
        assert image is not None
        image = image.reshape((height, width))

    return image, head

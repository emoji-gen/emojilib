# -*- encoding: utf-8 -*-
# cython: language_level=3

from cpython.bytes cimport PyBytes_FromStringAndSize
from libc.stdint cimport uint32_t
from libc.string cimport memset

# ------------------------------------------------------------------------------

cdef extern from 'emoji.h':

    # Error Codes
    #~~~~~~~~~~~~~~~
    ctypedef int EgError;

    cdef EgError EG_OK
    cdef EgError EG_INVALID_PARAMETER

    # Align
    #~~~~~~~~~
    ctypedef enum EgAlign:
        kLeft_Align,
        kCenter_Align,
        kRight_Align,

    # Format
    #~~~~~~~~~
    ctypedef enum EgFormat:
        kPNG_Format,
        kWEBP_Format,

    # Generate Params
    #~~~~~~~~~~~~~~~~~~
    ctypedef struct EgGenerateParams:
        # Text
        const char* fText

        # Sizes
        uint32_t fWidth
        uint32_t fHeight

        # Color
        uint32_t fColor
        uint32_t fBackgroundColor

        # Style
        EgAlign fTextAlign
        bint fTextSizeFixed
        bint fDisableStretch

        # Font
        const char* fTypefaceFile
        const char* fTypefaceName

        # Image
        EgFormat fFormat
        int fQuality

    # Generate Result
    #~~~~~~~~~~~~~~~~~~
    ctypedef struct EgGenerateResult:
        size_t fSize
        void* fData

    # Functions
    #~~~~~~~~~~~~~
    EgError emoji_generate(const EgGenerateParams* params, EgGenerateResult* result);
    void emoji_free(EgGenerateResult* const result);

# ------------------------------------------------------------------------------

cdef uint32_t convert_to_color(unicode color) except *:
    if color is None:
        raise TypeError("must be str")

    cdef size_t length = len(color)
    if length == 0:
        raise ValueError("invalid `color` format")

    cdef unsigned pos = 1 if color[0] == '#' else 0
    cdef unsigned scanned_color = int(color[pos:], 16)

    cdef unsigned red, green, blue, alpha
    if length - pos == 8:
        red = scanned_color >> 24 & 0xff
        green = scanned_color >> 16 & 0xff
        blue = scanned_color >> 8 & 0xff
        alpha = scanned_color & 0xff
        return alpha << 24 | red << 16 | green << 8 | blue

    raise ValueError("invalid `color` format")


cdef EgAlign convert_to_align(unicode align) except *:
    if align is None:
        raise TypeError("`align` must be str")

    cdef unicode lowered_align = align.lower()
    if lowered_align == 'left':
        return kLeft_Align
    if lowered_align == 'center':
        return kCenter_Align
    if lowered_align == 'right':
        return kRight_Align

    raise ValueError("invalid `align` format")


cdef EgFormat convert_to_format(unicode format) except *:
    if format is None:
        raise TypeError("`format` must be str")

    cdef unicode lowered_format = format.lower()
    if lowered_format == 'png':
        return kPNG_Format
    if lowered_format == 'webp':
        return kWEBP_Format

    raise ValueError("invalid `format` format")

# ------------------------------------------------------------------------------

def generate(
        *,
        unicode text='ab\nc.',
        int width=128,
        int height=128,
        unicode color='#000000FF',
        unicode background_color='#00000000',
        unicode align='center',
        bint size_fixed=False,
        bint disable_stretch=False,
        unicode typeface_file=None,
        unicode typeface_name=None,
        unicode format='png',
        int quality=100):

    # パラメーター生成
    cdef EgGenerateParams params
    memset(&params, 0, sizeof(EgGenerateParams))

    if text is None:
        raise TypeError("`text` must be str")
    if text == '':
        raise ValueError("invalid `text` format")
    cdef bytes text_bytes = text.encode('utf-8')
    params.fText = text_bytes

    if width <= 0:
        raise ValueError("invalid `width` format")
    params.fWidth = width

    if height <= 0:
        raise ValueError("invalid `height` format")
    params.fHeight = height

    params.fColor = convert_to_color(color)
    params.fBackgroundColor = convert_to_color(background_color)
    params.fTextAlign = convert_to_align(align)
    params.fTextSizeFixed = size_fixed
    params.fDisableStretch = disable_stretch

    cdef bytes typeface_file_bytes = None
    if typeface_file == '':
        raise ValueError("invalid `typeface_name` value")
    if typeface_file is not None:
        typeface_file_bytes = typeface_file.encode('utf-8')
        params.fTypefaceFile = typeface_file_bytes

    cdef bytes typeface_name_bytes = None
    if typeface_name == '':
        raise ValueError("invalid `typeface_name` value")
    if typeface_name is not None:
        typeface_name_bytes = typeface_name.encode('utf-8')
        params.fTypefaceName = typeface_name_bytes

    params.fFormat = convert_to_format(format)

    if quality < 0 or quality > 100:
        raise ValueError("`quality` should be above 0 and bellow 100")
    params.fQuality = quality

    # 生成
    cdef EgGenerateResult result
    memset(&result, 0, sizeof(EgGenerateResult));

    cdef EgError err = emoji_generate(&params, &result)
    if err != EG_OK:
        if err == EG_INVALID_PARAMETER:
            emoji_free(&result)
            raise RuntimeError("invalid parameter")

        emoji_free(&result)
        raise RuntimeError("unknown error");

    cdef bytes data = PyBytes_FromStringAndSize(<char*>result.fData, result.fSize)
    if data is None:
        emoji_free(&result)
        raise RuntimeError("cannot generate emoji data")

    emoji_free(&result)
    return data


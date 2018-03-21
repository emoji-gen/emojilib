#include <Python.h>

#include <strings.h>
#include <stdbool.h>
#include <stdint.h>

#include "emoji.h"

// --------------------------------------------------------------------------------------

static bool convert_to_color(const char* color_string, uint32_t* color) {
    if (color_string == NULL) return false;

    int length = strlen(color_string);
    if (length == 0) return false;

    unsigned pos = *color_string == '#' ? 1 : 0;
    uint32_t scanned_color;
    if (sscanf(color_string + pos, "%" PRIx32, &scanned_color) != 1) {
        return false;
    }

    if (length - pos == 8) {
        unsigned red = scanned_color >> 24 & 0xff;
        unsigned green = scanned_color >> 16 & 0xff;
        unsigned blue = scanned_color >> 8 & 0xff;
        unsigned alpha = scanned_color & 0xff;
        *color = alpha << 24 | red << 16 | green << 8 | blue;
        return true;
    }

    return false;
}

static bool convert_to_align(const char* align_string, EgAlign* align) {
    if (strcasecmp(align_string, "left") == 0) {
        *align = kLeft_Align;
        return true;
    }
    if (strcasecmp(align_string, "center") == 0) {
        *align = kCenter_Align;
        return true;
    }
    if (strcasecmp(align_string, "right") == 0) {
        *align = kRight_Align;
        return true;
    }
    return false;
}

static bool convert_to_format(const char* format_string, EgFormat* format) {
    if (strcasecmp(format_string, "png") == 0) {
        *format = kPNG_Format;
        return true;
    }
    if (strcasecmp(format_string, "webp") == 0) {
        *format = kWEBP_Format;
        return true;
    }
    return false;
}

// --------------------------------------------------------------------------------------

typedef struct {
    const char* text;
    int width;
    int height;
    const char* color;
    const char* background_color;
    const char* align;
    bool size_fixed;
    bool disable_stretch;
    const char* typeface_file;
    const char* typeface_name;
    const char* format;
    int quality;
} GenerateParams;

static void init_params(GenerateParams *params) {
    params->text = "ab\nc.";
    params->width = 128;
    params->height = 128;
    params->color = "#000000FF";
    params->background_color = "#00000000";
    params->align = "center";
    params->size_fixed = false;
    params->disable_stretch = false;
    params->typeface_file = NULL;
    params->typeface_name = NULL;
    params->format = "png";
    params->quality = 100;
}

static bool parse_params(PyObject* args, PyObject *kwargs, GenerateParams* params) {
    static char *kwlist[] = {
        "text",
        "width",
        "height",
        "color",
        "background_color",
        "align",
        "size_fixed",
        "disable_stretch",
        "typeface_file",
        "typeface_name",
        "format",
        "quality",
        NULL
    };

    if (!PyArg_ParseTupleAndKeywords(
            args,
            kwargs,
            "|siisssppsssi",
            kwlist,
            &params->text,
            &params->width,
            &params->height,
            &params->color,
            &params->background_color,
            &params->align,
            &params->size_fixed,
            &params->disable_stretch,
            &params->typeface_file,
            &params->typeface_name,
            &params->format,
            &params->quality))
    {
        return false;
    }

    return true;
}

static bool convert_params(GenerateParams* in_params, EgGenerateParams *params) {
    uint32_t color;
    uint32_t background_color;
    EgAlign align;
    EgFormat format;

    // Validation
    if (in_params->text == NULL || strlen(in_params->text) == 0) {
        PyErr_SetString(PyExc_ValueError, "invalid `text` format");
        return false;
    }

    if (in_params->width <= 0) {
        PyErr_SetString(PyExc_ValueError, "invalid `width` format");
        return false;
    }

    if (in_params->height <= 0) {
        PyErr_SetString(PyExc_ValueError, "invalid `height` format");
        return false;
    }

    if (!convert_to_color(in_params->color, &color)) {
        PyErr_SetString(PyExc_ValueError, "invalid `color` format");
        return false;
    }

    if (!convert_to_color(in_params->background_color, &background_color)) {
        PyErr_SetString(PyExc_ValueError, "invalid `background_color` format");
        return false;
    }

    if (!convert_to_align(in_params->align, &align)) {
        PyErr_SetString(PyExc_ValueError, "`align` should be one of \"left\", \"center\" or \"right\"");
        return false;
    }

    if (in_params->typeface_file != NULL && strlen(in_params->typeface_file) == 0) {
        PyErr_SetString(PyExc_ValueError, "invalid `typeface_file` value");
        return false;
    }

    if (in_params->typeface_name != NULL && strlen(in_params->typeface_name) == 0) {
        PyErr_SetString(PyExc_ValueError, "invalid `typeface_name` value");
        return false;
    }

    if (!convert_to_format(in_params->format, &format)) {
        PyErr_SetString(PyExc_ValueError, "`format` should be one of \"png\" or \"webp\"");
        return false;
    }

    if (in_params->quality < 0 || in_params->quality > 100) {
        PyErr_SetString(PyExc_ValueError, "`quality` should be above 0 and bellow 100");
        return false;
    }


    // Copy parameters
    memset(params, 0, sizeof(EgGenerateParams));
    params->fText = in_params->text;
    params->fWidth = in_params->width;
    params->fHeight = in_params->height;
    params->fColor = color;
    params->fBackgroundColor = background_color;
    params->fTextAlign = align;
    params->fTextSizeFixed = in_params->size_fixed;
    params->fDisableStretch = in_params->disable_stretch;
    params->fTypefaceFile = in_params->typeface_file;
    params->fTypefaceName = in_params->typeface_name;
    params->fFormat = format;
    params->fQuality = in_params->quality;

    return true;
}

// --------------------------------------------------------------------------------------

static PyObject* EmojiError;

static PyObject* pyemoji_generate(
    __attribute__ ((unused)) PyObject* self,
    PyObject* args,
    PyObject *kwargs
    )
{
    // パラメーター生成
    GenerateParams in_params;
    EgGenerateParams params;

    init_params(&in_params);
    if (!parse_params(args, kwargs, &in_params)) return NULL;
    if (!convert_params(&in_params, &params)) return NULL;

    // 生成
    EgGenerateResult result;
    EgError err = emoji_generate(&params, &result);
    if (err != EG_OK) {
        if (err == EG_INVALID_PARAMETER) {
            emoji_free(&result);
            PyErr_SetString(EmojiError, "invalid parameter");
            return NULL;
        }

        emoji_free(&result);
        PyErr_SetString(EmojiError, "unknown error");
        return NULL;
    }

    PyObject* data = Py_BuildValue("y#", result.fData, result.fSize);
    if (data == NULL) {
        emoji_free(&result);
        PyErr_SetString(EmojiError, "cannot generate emoji data");
        return NULL;
    }

    emoji_free(&result);
    return data;
}

// --------------------------------------------------------------------------------------

static PyMethodDef EmojiMethods[] = {
    { "generate", (PyCFunction)pyemoji_generate, METH_VARARGS | METH_KEYWORDS, "" },
    { NULL, NULL, 0, NULL }
};


static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "emojilib",
    NULL,
    -1,
    EmojiMethods
};

PyMODINIT_FUNC
PyInit_emojilib(void)
{
    PyObject *m;

    m = PyModule_Create(&module);
    if (m == NULL)
        return NULL;

    EmojiError = PyErr_NewException("emojilib.error", NULL, NULL);
    Py_INCREF(EmojiError);
    PyModule_AddObject(m, "error", EmojiError);

    return m;
}

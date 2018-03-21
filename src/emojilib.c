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

static PyObject* EmojiError;

static PyObject* pyemoji_generate(
    __attribute__ ((unused)) PyObject* self,
    PyObject* args,
    PyObject *kwargs
    )
{
    const char* text = "";
    int width = 128;
    int height = 128;
    const char* color_string = "#000000FF";
    const char* background_color_string = "#00000000";
    const char* typeface_name = NULL;
    const char* align_string = "center";
    const char* format_string = "png";
    int quality = 100;

    static char *kwlist[] = {
        "text",
        "width",
        "height",
        "color",
        "background_color",
        "align",
        "typeface_name",
        "format",
        "quality",
        NULL
    };

    // バリデーション
    if (!PyArg_ParseTupleAndKeywords(args, kwargs, "|siisssssi", kwlist,
            &text, &width, &height, &color_string, &background_color_string,
            &align_string, &typeface_name, &format_string, &quality))
    {
        return NULL;
    }

    if (height <= 0) {
        PyErr_SetString(PyExc_ValueError, "invalid height format");
        return NULL;
    }

    uint32_t color;
    if (!convert_to_color(color_string, &color)) {
        PyErr_SetString(PyExc_ValueError, "invalid color format");
        return NULL;
    }

    uint32_t background_color;;
    if (!convert_to_color(background_color_string, &background_color)) {
        PyErr_SetString(PyExc_ValueError, "invalid color format");
        return NULL;
    }

    EgAlign align;
    if (!convert_to_align(align_string, &align)) {
        PyErr_SetString(PyExc_ValueError, "`align` should be one of \"Left\", \"Center\" or \"Right\"");
        return NULL;
    }

    EgFormat format;
    if (!convert_to_format(format_string, &format)) {
        PyErr_SetString(PyExc_ValueError, "`format` should be one of \"PNG\" or \"WEBP\"");
        return NULL;
    }

    if (quality < 0 || quality > 100) {
        PyErr_SetString(PyExc_ValueError, "`quality` should be above 0 and bellow 100");
        return NULL;
    }

    // パラメーター生成
    EgGenerateParams params;
    memset(&params, 0, sizeof(params));
    params.fText = text;
    params.fWidth = width;
    params.fHeight = height;
    params.fColor = color;
    params.fBackgroundColor = background_color;
    params.fTextAlign = align;
    params.fTypefaceName = typeface_name;
    params.fFormat = format;
    params.fQuality = quality;

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

    EmojiError = PyErr_NewException("pyemoji.error", NULL, NULL);
    Py_INCREF(EmojiError);
    PyModule_AddObject(m, "error", EmojiError);

    return m;
}

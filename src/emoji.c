#include <Python.h>

#include <strings.h>
#include <stdbool.h>

#include "emoji.h"

static PyObject *EmojiError;

static bool parseAlign(const char* alignString, EgAlign* align) {
    if (strcasecmp(alignString, "left") == 0) {
        *align = kLeft_Align;
        return true;
    }
    if (strcasecmp(alignString, "center") == 0) {
        *align = kCenter_Align;
        return true;
    }
    if (strcasecmp(alignString, "right") == 0) {
        *align = kRight_Align;
        return true;
    }
    return false;
}

static bool parseFormat(const char* formatString, EgFormat* format) {
    if (strcasecmp(formatString, "png") == 0) {
        *format = kPNG_Format;
        return true;
    }
    if (strcasecmp(formatString, "webp") == 0) {
        *format = kWEBP_Format;
        return true;
    }
    return false;
}

static PyObject* emoji_py_generate(
    __attribute__ ((unused)) PyObject* self,
    PyObject* args,
    PyObject *kwargs
    )
{
    const char* text = "絵文\n字。";
    int width = 128;
    int height = 128;
    const char* typeface_name = NULL;
    const char* align_string = "center";
    const char* format_string = "png";
    int quality = 100;

    static char *kwlist[] = {
        "text",
        "width",
        "height",
        "align",
        "typeface_name",
        "format",
        "quality",
        NULL
    };

    if (!PyArg_ParseTupleAndKeywords(args, kwargs, "|siisssi", kwlist,
            &text, &width, &height, &align_string, &typeface_name, &format_string, &quality))
    {
        return NULL;
    }

    EgAlign align;
    if (!parseAlign(align_string, &align)) {
        PyErr_SetString(PyExc_ValueError, "`align` should be one of \"Left\", \"Center\" or \"Right\"");
        return NULL;
    }

    EgFormat format;
    if (!parseFormat(format_string, &format)) {
        PyErr_SetString(PyExc_ValueError, "`format` should be one of \"PNG\" or \"WEBP\"");
        return NULL;
    }

    if (quality < 0 || quality > 100) {
        PyErr_SetString(PyExc_ValueError, "`quality` should be above 0 and bellow 100");
        return NULL;
    }

    EgGenerateParams params;
    params.fText = text;
    params.fWidth = width;
    params.fHeight = height;
    params.fColor = 0xFFEC71A1;
    params.fBackgroundColor = 0x00FFFFFF;
    params.fTextAlign = align;
    params.fTypefaceName = typeface_name;
    params.fFormat = format;
    params.fQuality = quality;

    EgGenerateResult result;
    emoji_generate(&params, &result);

    PyObject* data = Py_BuildValue("y#", result.fData, result.fSize);
    emoji_free(&result);
    if (data == NULL) return NULL;

    return data;
}

static PyMethodDef EmojiMethods[] = {
    { "generate", (PyCFunction)emoji_py_generate, METH_VARARGS | METH_KEYWORDS, "" },
    { NULL, NULL, 0, NULL }
};


static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "emoji",
    NULL,
    -1,
    EmojiMethods
};

PyMODINIT_FUNC
PyInit_emoji(void)
{
    PyObject *m;

    m = PyModule_Create(&module);
    if (m == NULL)
        return NULL;

    EmojiError = PyErr_NewException("emoji.error", NULL, NULL);
    Py_INCREF(EmojiError);
    PyModule_AddObject(m, "error", EmojiError);

    return m;
}

#include <Python.h>

#include "emoji.h"

int foo() {
    EgGenerateParams params;
    params.fText = "確実に\n痩せる";
    params.fWidth = 1024;
    params.fHeight = 1024;
    params.fColor = 0xFFEC71A1;
    params.fBackgroundColor = 0x00FFFFFF;
    params.fTextAlign = kLeft_Align;
    params.fTypefaceName = "Noto Sans Mono CJK JP Bold";
    params.fFormat = kPNG_Format;
    params.fQuality = 100;

    EgGenerateResult result;
    emoji_generate(&params, &result);

    FILE *fp = fopen("./emoji.png", "w");
    fwrite(result.fData, result.fSize, 1, fp);
    fclose(fp);

    emoji_free(&result);

    return 0;
}

static PyMethodDef methods[] = {
    { NULL, NULL, 0, NULL }
};


static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "emoji",
    NULL,
    -1,
    methods
};

PyMODINIT_FUNC
PyInit_emoji(void)
{
    PyObject *m;

    m = PyModule_Create(&module);
    if (m == NULL)
        return NULL;


    /* EmojiError = PyErr_NewException("emoji.error", NULL, NULL); */
    /* Py_INCREF(EmojiError); */
    /* PyModule_AddObject(m, "error", EmojiError); */

    return m;
}

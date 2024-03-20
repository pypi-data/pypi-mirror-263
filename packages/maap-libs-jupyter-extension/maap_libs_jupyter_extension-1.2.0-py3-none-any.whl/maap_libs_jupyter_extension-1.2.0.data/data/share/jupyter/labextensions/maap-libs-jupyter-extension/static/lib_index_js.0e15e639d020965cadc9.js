(self["webpackChunkmaap_libs_jupyter_extension"] = self["webpackChunkmaap_libs_jupyter_extension"] || []).push([["lib_index_js"],{

/***/ "./node_modules/css-loader/dist/cjs.js!./style/index.css":
/*!***************************************************************!*\
  !*** ./node_modules/css-loader/dist/cjs.js!./style/index.css ***!
  \***************************************************************/
/***/ ((module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../node_modules/css-loader/dist/runtime/cssWithMappingToString.js */ "./node_modules/css-loader/dist/runtime/cssWithMappingToString.js");
/* harmony import */ var _node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../node_modules/css-loader/dist/runtime/api.js */ "./node_modules/css-loader/dist/runtime/api.js");
/* harmony import */ var _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _node_modules_css_loader_dist_runtime_getUrl_js__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../node_modules/css-loader/dist/runtime/getUrl.js */ "./node_modules/css-loader/dist/runtime/getUrl.js");
/* harmony import */ var _node_modules_css_loader_dist_runtime_getUrl_js__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_node_modules_css_loader_dist_runtime_getUrl_js__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _maap_svg__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./maap.svg */ "./style/maap.svg");
/* harmony import */ var _maap_svg__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_maap_svg__WEBPACK_IMPORTED_MODULE_3__);
// Imports




var ___CSS_LOADER_EXPORT___ = _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1___default()((_node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0___default()));
var ___CSS_LOADER_URL_REPLACEMENT_0___ = _node_modules_css_loader_dist_runtime_getUrl_js__WEBPACK_IMPORTED_MODULE_2___default()((_maap_svg__WEBPACK_IMPORTED_MODULE_3___default()));
// Module
___CSS_LOADER_EXPORT___.push([module.id, "\n:root {\n    --jp-icon-maap: url(" + ___CSS_LOADER_URL_REPLACEMENT_0___ + ");\n}\n\n.jp-MaapIcon {\n  background-image: var(--jp-icon-maap);\n}\n.Toastify__toast-body {\n  overflow: auto;\n}", "",{"version":3,"sources":["webpack://./style/index.css"],"names":[],"mappings":";AACA;IACI,uDAA+B;AACnC;;AAEA;EACE,qCAAqC;AACvC;AACA;EACE,cAAc;AAChB","sourcesContent":["\n:root {\n    --jp-icon-maap: url('maap.svg');\n}\n\n.jp-MaapIcon {\n  background-image: var(--jp-icon-maap);\n}\n.Toastify__toast-body {\n  overflow: auto;\n}"],"sourceRoot":""}]);
// Exports
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (___CSS_LOADER_EXPORT___);


/***/ }),

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   ButtonExtension: () => (/* binding */ ButtonExtension),
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _lumino_disposable__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @lumino/disposable */ "webpack/sharing/consume/default/@lumino/disposable");
/* harmony import */ var _lumino_disposable__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_lumino_disposable__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/notebook */ "webpack/sharing/consume/default/@jupyterlab/notebook");
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _lumino_domutils__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @lumino/domutils */ "webpack/sharing/consume/default/@lumino/domutils");
/* harmony import */ var _lumino_domutils__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_lumino_domutils__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _request__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./request */ "./lib/request.js");
/* harmony import */ var _style_index_css__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ../style/index.css */ "./style/index.css");









let DEFAULT_CODE = 'from maap.maap import MAAP\n' +
    'maap = MAAP()';
let api_server = '';
var valuesUrl = new URL(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_4__.PageConfig.getBaseUrl() + 'jupyter-server-extension/getConfig');
(0,_request__WEBPACK_IMPORTED_MODULE_6__.request)('get', valuesUrl.href).then((res) => {
    if (res.ok) {
        let environment = JSON.parse(res.data);
        api_server = environment['api_server'];
        DEFAULT_CODE = 'from maap.maap import MAAP\n' +
            'maap = MAAP(maap_host=\'' + api_server + '\')';
    }
});
/**
 * A notebook widget extension that adds a button to the toolbar.
 */
class ButtonExtension {
    /**
     * Create a new extension object.
     */
    createNew(panel, context) {
        let callback = () => {
            // Select the first cell of the notebook
            panel.content.activeCellIndex = 0;
            panel.content.deselectAll();
            if (panel.content.activeCell != null) {
                _lumino_domutils__WEBPACK_IMPORTED_MODULE_3__.ElementExt.scrollIntoViewIfNeeded(panel.content.node, panel.content.activeCell.node);
            }
            // Check if already there
            if (panel.content.activeCell != null) {
                if (panel.content.activeCell.model.value.text == DEFAULT_CODE) {
                    _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.Notification.error("MAAP defaults already imported to notebook.");
                }
                else {
                    // Insert code above selected first cell
                    _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_2__.NotebookActions.insertAbove(panel.content);
                    panel.content.activeCell.model.value.text = DEFAULT_CODE;
                }
            }
        };
        let button = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.ToolbarButton({
            className: 'myButton',
            iconClass: 'jp-MaapIcon foo jp-Icon jp-Icon-16 jp-ToolbarButtonComponent-icon',
            onClick: callback,
            tooltip: 'Import MAAP Libraries'
        });
        panel.toolbar.insertItem(0, 'insertDefaults', button);
        return new _lumino_disposable__WEBPACK_IMPORTED_MODULE_1__.DisposableDelegate(() => {
            button.dispose();
        });
    }
}
/**
 * Activate the extension.
 */
function activateNbDefaults(app) {
    app.docRegistry.addWidgetExtension('Notebook', new ButtonExtension());
    console.log("insert defaults to notebook extension activated");
}
;
function hidePanels() {
    const leftPanelParent = document.querySelector('.p-TabBar-content');
    let tabsPanel = null;
    if (leftPanelParent != null) {
        tabsPanel = leftPanelParent.querySelector('li[title="Open Tabs"]');
    }
    console.log('leftPanelParent');
    console.log(leftPanelParent);
    console.log('tabsPanel');
    console.log(tabsPanel);
    if (tabsPanel != null && leftPanelParent != null) {
        leftPanelParent.removeChild(tabsPanel);
    }
    console.log('removing panel!');
}
/**
 * Initialization data for the insert_defaults_to_notebook extension.
 */
const extensionNbDefaults = {
    id: 'insert_defaults_to_notebook',
    autoStart: true,
    activate: activateNbDefaults
};
const extensionHidePanels = {
    id: 'hide_unused_panels',
    autoStart: true,
    requires: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.ICommandPalette],
    activate: (app, palette) => {
        const open_command = 'defaults:removePanel';
        app.commands.addCommand(open_command, {
            label: 'Hide Tabs',
            isEnabled: () => true,
            execute: args => {
                hidePanels();
            }
        });
        palette.addItem({ command: open_command, category: 'User' });
        hidePanels(); // automatically call function at startup
        console.log('remove panels activated');
    }
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ([extensionNbDefaults, extensionHidePanels]);


/***/ }),

/***/ "./lib/request.js":
/*!************************!*\
  !*** ./lib/request.js ***!
  \************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   DEFAULT_REQUEST_OPTIONS: () => (/* binding */ DEFAULT_REQUEST_OPTIONS),
/* harmony export */   request: () => (/* binding */ request)
/* harmony export */ });
const DEFAULT_REQUEST_OPTIONS = {
    ignoreCache: false,
    headers: {
        Accept: 'application/json, text/javascript, text/plain'
    },
    // default max duration for a request in ms
    // currently set to 120s = 2min
    timeout: 5000,
};
function queryParams(params = {}) {
    return Object.keys(params)
        .map(k => encodeURIComponent(k) + '=' + encodeURIComponent(params[k]))
        .join('&');
}
function withQuery(url, params = {}) {
    const queryString = queryParams(params);
    return queryString ? url + (url.indexOf('?') === -1 ? '?' : '&') + queryString : url;
}
function parseXHRResult(xhr) {
    return {
        ok: xhr.status >= 200 && xhr.status < 300,
        status: xhr.status,
        statusText: xhr.statusText,
        headers: xhr.getAllResponseHeaders(),
        data: xhr.responseText,
        json: () => JSON.parse(xhr.responseText),
        url: xhr.responseURL
    };
}
function errorResponse(xhr, message = null) {
    return {
        ok: false,
        status: xhr.status,
        statusText: xhr.statusText,
        headers: xhr.getAllResponseHeaders(),
        data: message || xhr.statusText,
        json: () => JSON.parse(message || xhr.statusText),
        url: xhr.responseURL
    };
}
function request(method, url, queryParams = {}, body = null, options = DEFAULT_REQUEST_OPTIONS) {
    const ignoreCache = options.ignoreCache || DEFAULT_REQUEST_OPTIONS.ignoreCache;
    const headers = options.headers || DEFAULT_REQUEST_OPTIONS.headers;
    const timeout = options.timeout || DEFAULT_REQUEST_OPTIONS.timeout;
    return new Promise((resolve, reject) => {
        const xhr = new XMLHttpRequest();
        xhr.open(method, withQuery(url, queryParams));
        if (headers) {
            Object.keys(headers).forEach(key => xhr.setRequestHeader(key, headers[key]));
        }
        if (ignoreCache) {
            xhr.setRequestHeader('Cache-Control', 'no-cache');
        }
        xhr.timeout = timeout;
        xhr.onload = evt => {
            resolve(parseXHRResult(xhr));
        };
        xhr.onerror = evt => {
            resolve(errorResponse(xhr, 'Failed to make request.'));
        };
        xhr.ontimeout = evt => {
            resolve(errorResponse(xhr, 'Request took longer than expected.'));
        };
        if (method === 'post' && body) {
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.send(JSON.stringify(body));
        }
        else {
            xhr.send();
        }
    });
}


/***/ }),

/***/ "./style/index.css":
/*!*************************!*\
  !*** ./style/index.css ***!
  \*************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! !../node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js */ "./node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js");
/* harmony import */ var _node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _node_modules_css_loader_dist_cjs_js_index_css__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! !!../node_modules/css-loader/dist/cjs.js!./index.css */ "./node_modules/css-loader/dist/cjs.js!./style/index.css");

            

var options = {};

options.insert = "head";
options.singleton = false;

var update = _node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0___default()(_node_modules_css_loader_dist_cjs_js_index_css__WEBPACK_IMPORTED_MODULE_1__["default"], options);



/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (_node_modules_css_loader_dist_cjs_js_index_css__WEBPACK_IMPORTED_MODULE_1__["default"].locals || {});

/***/ }),

/***/ "./style/maap.svg":
/*!************************!*\
  !*** ./style/maap.svg ***!
  \************************/
/***/ ((module) => {

module.exports = "data:image/svg+xml,%3Csvg fill='%23E0E0E0' height='18' viewBox='0 0 24 24' width='18' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E %3Cpath d='M0 0h24v24H0z' fill='none'/%3E %3Ctext x='50%25' y='50%25' dominant-baseline='central' text-anchor='middle' font-family='sans-serif' font-size='8px' fill='blue'%3EMAAP%3C/text%3E %3C/svg%3E"

/***/ })

}]);
//# sourceMappingURL=lib_index_js.0e15e639d020965cadc9.js.map
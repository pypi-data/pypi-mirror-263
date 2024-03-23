"use strict";
(self["webpackChunkiinit"] = self["webpackChunkiinit"] || []).push([["lib_index_js"],{

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/notebook */ "webpack/sharing/consume/default/@jupyterlab/notebook");
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0__);

/**
 * Initialization data for the iinit extension.
 */
const plugin = {
    id: 'iinit:plugin',
    description: 'A jupyter lab/notebook front-end extension for running/executing cells on kernel start-up',
    autoStart: true,
    requires: [_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0__.INotebookTracker],
    activate: (app, notebookTracker) => {
        console.log('JupyterLab extension iinit is activated!');
        // Detect whether a new notebook file has been opened
        notebookTracker.widgetAdded.connect(() => {
            // console.log("New Notebook File Opened");
            // get the current notebook panel
            let labShell = app.shell;
            let panel = labShell.currentWidget;
            // get the current/open notebook
            const current = notebookTracker.currentWidget;
            let notebook = current === null || current === void 0 ? void 0 : current.content;
            // check if panel is defined
            if (panel) {
                panel.revealed.then(() => {
                    // console.log("Panel Revealed");
                    // detect whether kernel has been loaded in jupyter shell lab
                    panel.context.sessionContext.ready.then(() => {
                        panel.context.sessionContext.session.kernel.connectionStatusChanged.connect(() => {
                            var _a, _b;
                            // if notebook metadata is set as "iinit:": true, then run all cells at startup
                            let iinit = (_a = notebook === null || notebook === void 0 ? void 0 : notebook.model) === null || _a === void 0 ? void 0 : _a.sharedModel.getMetadata("iinit");
                            console.log("run all cells (notebook metadata iinit)" + iinit);
                            if (iinit === true) {
                                app.commands.execute('notebook:run-all-cells');
                            }
                            else {
                                // retrieve all the cells from the notebook panel
                                let cellList = (_b = panel.content.model) === null || _b === void 0 ? void 0 : _b.cells;
                                // iterate over all the cells in the notebook panel
                                // check for cells having metadata "iinit"
                                // if so, execute the cell source at startup, otherwise don't
                                let l = cellList === null || cellList === void 0 ? void 0 : cellList.length; // store the number of cells (at notebook reveal)
                                // check if length is defined before iterating
                                if (l) {
                                    for (let i = 0; i < l; i++) {
                                        // if cell contains the iinit metadata then run the source code at startup
                                        if (cellList === null || cellList === void 0 ? void 0 : cellList.get(i).getMetadata("iinit")) {
                                            // check if notebook is defined
                                            if (notebook) {
                                                // set active cell
                                                notebook.activeCellIndex = i;
                                                // get source code from cell
                                                // let source = notebook?.activeCell?.model.sharedModel.source;
                                                // console.log("metadata found at cell index " + i);
                                                // console.log(source);
                                                // run the currently active/selected cell
                                                // app.commands.execute('notebook:run-cell-and-select-next')
                                                app.commands.execute('notebook:run-cell');
                                            }
                                        }
                                    }
                                }
                            }
                        });
                    });
                });
            }
        });
    }
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);


/***/ })

}]);
//# sourceMappingURL=lib_index_js.0fe1371c1e33b84ec9d4.js.map
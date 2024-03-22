"use strict";
(self["webpackChunkiloadmagics"] = self["webpackChunkiloadmagics"] || []).push([["lib_index_js"],{

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
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__);

// Import for adding Lumino Widgets to the Notebook Panel


/**
 * Initialization data for the iloadmagics extension.
 */
// CSS class name for top area panel anchor/image widget
const ilambda_Anchor_CSS_CLASS = 'jp-ilambda-Anchor';
let iloadmagics_dummy_cell_magic = "%%iCustomMagic\nprint(\"This is a test\")"; // metadata key
// to be improved - let user specify via jupyter lab menu where to look/find appropriate ipython magic classes
let iloadmagics_cell_source = "import iloadmagics";
const plugin = {
    id: 'iloadmagics:plugin',
    description: 'A jupyter lab/notebook front-end extension for dynamically loading ipython magic commands upon kernel startup',
    autoStart: true,
    requires: [_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0__.INotebookTracker],
    activate: (app, notebookTracker) => {
        console.log('JupyterLab extension iloadmagics is activated!');
        // Code for adding logo to top area widget
        var node;
        // If the node doesn't exist, create it
        node = document.createElement("div");
        node.innerHTML = "<a href='https://www.lambda.joburg' target='_blank'><img src='https://lambda.joburg/assets/images/index/logo/lambda_logo.svg'></a>";
        const widget = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_1__.Widget({ node }); // constructor for creating a widget from a DOM element    
        widget.id = _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__.DOMUtils.createDomID();
        widget.id = "ilambda-logo";
        // provide a class for styling
        widget.addClass(ilambda_Anchor_CSS_CLASS);
        // add the widget to the DOM
        app.shell.add(widget, 'top', { rank: 1000 }); // rank - move widget to right-most position in top area panel    
        // Add the element to the DOM in any case
        let logos = document.getElementsByClassName(ilambda_Anchor_CSS_CLASS);
        // console.log(logos);
        // if there are multiple ilambda extensions installed,
        // each will contribute its own logo, so do the following
        if (logos.length >= 2) {
            // remove all the ilambda-logo widgets from the DOM, except the first
            for (let i = 1; i < logos.length; i++) {
                logos[i].remove();
            }
        }
        // Detect whether a new notebook file has been opened
        notebookTracker.widgetAdded.connect(() => {
            let labShell = app.shell;
            let panel = labShell.currentWidget;
            // Check if panel is defined
            if (panel) {
                // continue if panel is revealed/loaded
                panel.revealed.then(() => {
                    // Detect whether kernel has been loaded in jupyter shell lab
                    panel.context.sessionContext.ready.then(() => {
                        panel.context.sessionContext.session.kernel.connectionStatusChanged.connect(() => {
                            var _a;
                            // retrieve/store all the cells from the notebook panel
                            let cellList = (_a = panel.content.model) === null || _a === void 0 ? void 0 : _a.cells;
                            // get the number of cells in the notebook panel
                            let l = cellList === null || cellList === void 0 ? void 0 : cellList.length;
                            if (l) {
                                console.log("Number of cells" + l);
                                // get the current/open notebook
                                // store current widget as a variable
                                const current = notebookTracker.currentWidget;
                                // console.log(current);
                                // get contents of notebook
                                let notebook = current === null || current === void 0 ? void 0 : current.content;
                                // check if notebook exists
                                if (notebook) {
                                    notebook.activeCellIndex = l;
                                    // insert a new cell at the bottom of the notebook
                                    _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0__.NotebookActions.insertBelow(notebook);
                                    // set the new bottom cell as the active cell
                                    notebook.activeCellIndex = l + 1; // set index to 0
                                    // set the source code for the active cell
                                    if (notebook.activeCell) {
                                        notebook.activeCell.model.sharedModel.setSource(iloadmagics_cell_source);
                                        // run the active cell
                                        app.commands.execute('notebook:run-cell');
                                        // hide/delete the cell
                                        // NotebookActions.deleteCells(notebook);
                                        // Alternative ways to delete cell
                                        app.commands.execute('notebook:delete-cell');
                                        // app.commands.execute('notebook:run-cell-and-insert-below')
                                        // select first cell
                                        notebook.activeCellIndex = 0; // set index to 0
                                        // insert cell above first/top cell
                                        _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0__.NotebookActions.insertAbove(notebook);
                                        // set selected cell to the new cell index
                                        notebook.activeCellIndex = 0; // set index to 0
                                        notebook.activeCell.model.sharedModel.setSource(iloadmagics_dummy_cell_magic);
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
//# sourceMappingURL=lib_index_js.14ef966552e82335a53e.js.map
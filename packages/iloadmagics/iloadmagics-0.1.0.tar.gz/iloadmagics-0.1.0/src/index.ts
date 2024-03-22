import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin,
  LabShell
} from '@jupyterlab/application';

import {
  INotebookTracker,
  NotebookPanel,
  NotebookActions,
} from '@jupyterlab/notebook';

// Import for adding Lumino Widgets to the Notebook Panel
import {
  Widget
} from '@lumino/widgets';

import {
  DOMUtils
} from '@jupyterlab/apputils';

/**
 * Initialization data for the iloadmagics extension.
 */

// CSS class name for top area panel anchor/image widget
const ilambda_Anchor_CSS_CLASS = 'jp-ilambda-Anchor';

let iloadmagics_dummy_cell_magic = "%%iCustomMagic\nprint(\"This is a test\")"; // metadata key

// to be improved - let user specify via jupyter lab menu where to look/find appropriate ipython magic classes
let iloadmagics_cell_source = "import iloadmagics";

const plugin: JupyterFrontEndPlugin<void> = {
  id: 'iloadmagics:plugin',
  description: 'A jupyter lab/notebook front-end extension for dynamically loading ipython magic commands upon kernel startup',
  autoStart: true,
  requires: [INotebookTracker],
  activate: (app: JupyterFrontEnd, notebookTracker: INotebookTracker) => {
    console.log('JupyterLab extension iloadmagics is activated!');

    // Code for adding logo to top area widget
    var node;
    // If the node doesn't exist, create it
    node = document.createElement("div");
    node.innerHTML = "<a href='https://www.lambda.joburg' target='_blank'><img src='https://lambda.joburg/assets/images/index/logo/lambda_logo.svg'></a>";
    const widget = new Widget({node}); // constructor for creating a widget from a DOM element    
    widget.id = DOMUtils.createDomID();
    widget.id = "ilambda-logo";
    // provide a class for styling
    widget.addClass(ilambda_Anchor_CSS_CLASS);
    // add the widget to the DOM
    app.shell.add(widget, 'top', {rank: 1000}); // rank - move widget to right-most position in top area panel    
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
    notebookTracker.widgetAdded.connect(()=>{
      let labShell = app.shell as LabShell;
      let panel = labShell.currentWidget as NotebookPanel;
      // Check if panel is defined
      if (panel) {
        // continue if panel is revealed/loaded
        panel.revealed.then(()=>{
          // Detect whether kernel has been loaded in jupyter shell lab
          panel!.context.sessionContext.ready.then(()=>{
            panel.context.sessionContext.session!.kernel!.connectionStatusChanged.connect(()=>{
              // retrieve/store all the cells from the notebook panel
              let cellList = panel.content.model?.cells;
              // get the number of cells in the notebook panel
              let l = cellList?.length;
              if (l) {
                console.log("Number of cells" + l);
                // get the current/open notebook
                // store current widget as a variable
                const current = notebookTracker.currentWidget;
                // console.log(current);
                // get contents of notebook
                let notebook = current?.content;
                // check if notebook exists
                if (notebook) {
                  notebook.activeCellIndex = l;
                  // insert a new cell at the bottom of the notebook
                  NotebookActions.insertBelow(notebook);
                  // set the new bottom cell as the active cell
                  notebook.activeCellIndex = l+1; // set index to 0
                  // set the source code for the active cell
                  if (notebook.activeCell) {
                    notebook.activeCell.model.sharedModel.setSource(iloadmagics_cell_source);
                    // run the active cell
                    app.commands.execute('notebook:run-cell')
                    // hide/delete the cell
                    // NotebookActions.deleteCells(notebook);
                    // Alternative ways to delete cell
                    app.commands.execute('notebook:delete-cell')
                    // app.commands.execute('notebook:run-cell-and-insert-below')
                    // select first cell
                    notebook.activeCellIndex = 0; // set index to 0
                    // insert cell above first/top cell
                    NotebookActions.insertAbove(notebook);
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

export default plugin;

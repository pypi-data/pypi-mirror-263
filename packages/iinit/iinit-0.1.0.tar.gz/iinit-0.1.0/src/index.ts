import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin,
  LabShell
} from '@jupyterlab/application';

import {
  INotebookTracker,
  NotebookPanel,
  // NotebookActions,
} from '@jupyterlab/notebook';

// Import for adding Lumino Widgets to the Notebook Panel
import {
  Widget
} from '@lumino/widgets';

import {
  DOMUtils
} from '@jupyterlab/apputils';

// CSS class name for top area panel anchor/image widget
const ilambda_Anchor_CSS_CLASS = 'jp-ilambda-Anchor';

/**
 * Initialization data for the iinit extension.
 */

const plugin: JupyterFrontEndPlugin<void> = {
  id: 'iinit:plugin',
  description: 'A jupyter lab/notebook front-end extension for initializing cells upon kernel startup',
  autoStart: true,
  requires: [INotebookTracker],
  activate: (app: JupyterFrontEnd, notebookTracker: INotebookTracker) => {
    
    console.log('JupyterLab extension iinit is activated!');

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
      // console.log("New Notebook File Opened");
      // get the current notebook panel
      let labShell = app.shell as LabShell;
      let panel = labShell.currentWidget as NotebookPanel;
      // get the current/open notebook
      const current = notebookTracker.currentWidget
      let notebook = current?.content;
      // check if panel is defined
      if (panel) {
        panel.revealed.then(()=>{
          // console.log("Panel Revealed");
          // detect whether kernel has been loaded in jupyter shell lab
          panel!.context.sessionContext.ready.then(()=>{
            panel.context.sessionContext.session!.kernel!.connectionStatusChanged.connect(()=>{
              // retrieve all the cells from the notebook panel
              let cellList = panel.content.model?.cells;
              // iterate over all the cells in the notebook panel
              // check for cells having metadata "iinit"
              // if so, execute the cell source at startup, otherwise don't
              let l = cellList?.length; // store the number of cells (at notebook reveal)
              // check if length is defined before iterating
              if (l) {
                for (let i = 0; i < l; i++) {
                  // if cell contains the iinit metadata then run the source code at startup
                  if (cellList?.get(i).getMetadata("iinit")) {
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
                      if (cellList?.get(i).getMetadata("ihide")) {
                        notebook.activeCell?.setHidden(true);
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

export default plugin;

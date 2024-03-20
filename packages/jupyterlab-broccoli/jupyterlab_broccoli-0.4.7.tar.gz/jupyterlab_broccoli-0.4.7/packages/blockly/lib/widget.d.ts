import { DocumentRegistry, DocumentWidget, DocumentModel } from '@jupyterlab/docregistry';
import { IRenderMimeRegistry } from '@jupyterlab/rendermime';
import { JupyterFrontEnd } from '@jupyterlab/application';
import { WidgetTracker } from '@jupyterlab/apputils';
import { CodeCell } from '@jupyterlab/cells';
import { TranslationBundle } from '@jupyterlab/translation';
import { SplitPanel } from '@lumino/widgets';
import { BlocklyLayout } from './layout';
import { BlocklyManager } from './manager';
/**
 * DocumentWidget: widget that represents the view or editor for a file type.
 */
export declare class BlocklyEditor extends DocumentWidget<BlocklyPanel, DocumentModel> {
    private _context;
    private _translator;
    private _manager;
    private _blayout;
    private _dirty;
    constructor(app: JupyterFrontEnd, options: BlocklyEditor.IOptions);
    get trans(): TranslationBundle;
    get blayout(): BlocklyLayout;
    get cell(): CodeCell;
    /**
     * Sets the dirty boolean while also toggling the DIRTY_CLASS
     */
    private dirty;
    save(exiting?: boolean): Promise<void>;
    /**
     * Dispose of the resources held by the widget.
     */
    dispose(): Promise<void>;
    private _onBlockChanged;
}
export declare namespace BlocklyEditor {
    interface IOptions extends DocumentWidget.IOptions<BlocklyPanel, DocumentModel> {
        manager: BlocklyManager;
    }
}
/**
 * Widget that contains the main view of the DocumentWidget.
 */
export declare class BlocklyPanel extends SplitPanel {
    private _tracker;
    private _content;
    private _context;
    private _rendermime;
    private _manager;
    private _editor;
    /**
     * Construct a `BlocklyPanel`.
     *
     * @param context - The documents context.
     */
    constructor(tracker: WidgetTracker<BlocklyEditor>, context: DocumentRegistry.IContext<DocumentModel>, manager: BlocklyManager, rendermime: IRenderMimeRegistry);
    get cell(): CodeCell;
    get rendermime(): IRenderMimeRegistry;
    get context(): DocumentRegistry.IContext<DocumentModel>;
    get content(): any;
    get manager(): BlocklyManager;
    get activeLayout(): BlocklyLayout;
    set activeEditor(editor: BlocklyEditor);
    get activeEditor(): BlocklyEditor;
    /**
     * Dispose of the resources held by the widget.
     */
    dispose(): void;
    private _load;
    private _onSave;
}

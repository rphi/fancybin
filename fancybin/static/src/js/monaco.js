import * as monaco from 'monaco-editor';

self.MonacoEnvironment = {
  getWorkerUrl: function(moduleId, label) {
    if (label === 'json') {
      return '/static/json.worker.js';
    }
    if (label === 'css') {
      return '/static/css.worker.js';
    }
    if (label === 'html') {
      return '/static/html.worker.js';
    }
    if (label === 'typescript' || label === 'javascript') {
      return '/static/ts.worker.js';
    }
    return '/static/editor.worker.js';
  },
};

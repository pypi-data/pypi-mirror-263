const LOCAL_DEV = false;

export let BACKEND_API_URL: string, WEBSOCKET_API_URL: string;
if (LOCAL_DEV) {
  // LOCAL
  BACKEND_API_URL = 'http://localhost:80';
  WEBSOCKET_API_URL = 'ws://localhost:1337/ws';

  // LOCAL W/ GATEWAY
  // BACKEND_API_URL = 'http://localhost:1015';
  // WEBSOCKET_API_URL = 'ws://localhost:1015/ws';

  // TEST NOTO
  // BACKEND_API_URL = 'https://test-noto.epfl.ch/api/unilytics';
  // WEBSOCKET_API_URL = 'ws://test-noto.epfl.ch/api/unilytics/ws';
} else {
  BACKEND_API_URL = 'https://api.unianalytics.ch';
  WEBSOCKET_API_URL =
    'wss://ax5pzl8bwk.execute-api.eu-north-1.amazonaws.com/production/';
}

// adapt the app ids in the schema/*.json if this value is changed
export const APP_ID = 'jupyterlab_unianalytics_dashboard';
// A plugin id has to be of the form APP_ID:<schema name without .json>
export const PLUGIN_ID = `${APP_ID}:plugin`;

export const ACCESS_TOKEN_KEY = `${APP_ID}_access_token`;
export const REFRESH_TOKEN_KEY = `${APP_ID}_refresh_token`;

export const STORAGE_KEY = `${APP_ID}/commondashboard:redux_state`;

export const TOC_DASHBOARD_RENDER_TIMEOUT = 1000;

export namespace CommandIDs {
  export const dashboardOpenVisu = `${APP_ID}:dashboard-open-visu`;

  export const uploadNotebook = `${APP_ID}:dashboard-upload-notebook`;

  export const copyDownloadLink = `${APP_ID}:dashboard-copy-download-link`;
}

export const visuIconClass = 'jp-icon3';

export const notebookSelector =
  '.jp-DirListing-item[data-file-type="notebook"]';

// notebook metadata field names
const SELECTOR_ID = 'unianalytics';
export namespace Selectors {
  export const notebookId = `${SELECTOR_ID}_notebook_id`;

  export const cellMapping = `${SELECTOR_ID}_cell_mapping`;
}

export const DropdownSortingValues = [
  {
    key: 'timeDesc',
    label: 'Time (most recent 1st)',
    method: (a: any, b: any) => {
      return new Date(a.t_finish) < new Date(b.t_finish) ? 1 : -1;
    }
  },
  {
    key: 'timeAsc',
    label: 'Time (oldest 1st)',
    method: (a: any, b: any) => {
      return new Date(a.t_finish) > new Date(b.t_finish) ? 1 : -1;
    }
  },
  {
    key: 'inputAsc',
    label: 'Input (shortest 1st)',
    method: (a: any, b: any) => {
      return a.cell_input.length - b.cell_input.length;
    }
  },
  {
    key: 'inputDesc',
    label: 'Input (longest 1st)',
    method: (a: any, b: any) => {
      return b.cell_input.length - a.cell_input.length;
    }
  },
  {
    key: 'outputAsc',
    label: 'Output (shortest 1st)',
    method: (a: any, b: any) => {
      return a.cell_output_length - b.cell_output_length;
    }
  },
  {
    key: 'outputDesc',
    label: 'Output (longest 1st)',
    method: (a: any, b: any) => {
      return b.cell_output_length - a.cell_output_length;
    }
  }
];

 import { CONFIG } from "./config.js";

document.addEventListener("DOMContentLoaded", () => {

    document.title = CONFIG.APP.NAME;

    console.log(
        `${CONFIG.APP.NAME} ${CONFIG.APP.VERSION} Loaded`
    );

});

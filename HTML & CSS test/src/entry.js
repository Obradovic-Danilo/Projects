// Application entry point

// Load application images
// require.context("./images", true, /\.(png|svg|jpg|gif)$/);

// Load application styles
import './css/style.scss';

// Load application scripts
import './js/scripts.js';

// Don't remove this code
if (module.hot) {
    module.hot.accept();
}
